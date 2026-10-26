from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict, Literal
from pydantic import BaseModel, Field

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, SystemMessage


#===================================
# State
#===================================


class State(TypedDict):
    task: str
    draft: str
    review_decision: str
    review_feedback: str
    revision_count: int

#===================================
# Model
#===================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash"
)


#===================================
# Reviewer Output Schema
#===================================

class ReviewResult(BaseModel):
    decision: Literal["approved", "needs_revision"] = Field(description="the decision of the reviewer")
    feedback: str = Field(description="The feedback from the reviewer")

reviewer_llm = llm.with_structured_output(ReviewResult)

#===================================
# Coder Agent
#===================================

def writer_node(state: State):
    print("Writing...")

    task = state["task"]
    previous_draft = state["draft"]
    feedback = state["review_feedback"]
    revision_count = state["revision_count"]

    if revision_count == 0:
        prompt = [
            SystemMessage(
                content="""
                You are a code writer assistant.
                write a clear, correct, user-friendly code.
                return only the code without any extra additional text.
                """
            ),
            HumanMessage(content=f"Task: {task}")
        ]

    else:
        prompt = [
            SystemMessage(
                content="""
                You are a code writer assistant.
                Improve previous draft based on the reviewer feedback.
                keep the part of code that is already correct.
                return only the code without any extra additional text."""
            ),
            HumanMessage(
                content=f"""
                Tast: {task}
                Previous draft {previous_draft}
                Reviewer feedback: {feedback}
                """
            )
        ]

    response = llm.invoke(prompt)

    return {
        "draft": response.text
    }

#===================================
# Reviewer Agent
#===================================

def review_node(state: State):
    print("Rewieving...")

    task = state['task']
    draft = state["draft"]

    prompt = [
        SystemMessage(
            content="""
            You are a code reviewer assistant.
            Review the following code based on the task description.
            Determine if the code is correct and satisfies the task requirements.
            """
        ),
        HumanMessage(
            content=f"""
            Task: {task}
            Draft: {draft}
            """           
        )
    ]

    review = reviewer_llm.invoke(prompt)

    return {
        "review_decision": review.decision,
        "review_feedback": review.feedback,
        "revision_count": state['revision_count'] + 1
    }

#===================================
# Router
#===================================

def route_to_next_node(state: State):
    if state["review_decision"] == "approved":
        return END

    if state["revision_count"] >=3:
        return END

    return "writer"

#===================================
# Graph
#===================================

builder = StateGraph(State)

builder.add_node("writer", writer_node)
builder.add_node("reviewer", review_node)

builder.add_edge(START, "writer")
builder.add_edge("writer", "reviewer")
builder.add_conditional_edges("reviewer", route_to_next_node)

graph = builder.compile()

#===================================
# Run the graph
#===================================

initial_state = {
    "task": "Write a print function in python.",
    "draft": "",
    "review_decision": "",
    "review_feedback": "",
    "revision_count": 0
}

result = graph.invoke(initial_state)

print(f"Final draft: {result['draft']}")
print("=" * 50)
print(f"Review decision: {result['review_decision']}")
print("=" * 50)
print(f"Review feedback: {result['review_feedback']}")
print("=" * 50)
print(f"Revision count: {result['revision_count']}")