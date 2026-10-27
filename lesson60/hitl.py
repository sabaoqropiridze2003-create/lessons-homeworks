from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Literal
from langchain_core.messages import HumanMessage, SystemMessage


#---------------------------------------------
# State
#---------------------------------------------

class State(TypedDict):
    task: str
    draft: str
    approval_status: Literal["approved", "needs_revision", "pending", "max_revisions_reached"]
    human_feedback: str
    revision_count: int

#---------------------------------------------
# Model
#---------------------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

#---------------------------------------------
# Code Writer Agent
#---------------------------------------------

def code_writer(state: State):
    task = state["task"]
    previous_draft = state["draft"]
    human_feedback = state["human_feedback"]
    revision_count = state["revision_count"]


    if revision_count == 0:
        prompt = [
            SystemMessage(
                content="""
                You are a code writer assistant.
                Write a clear, correct, user-friendly code.
                Return only the code without any extra additional text.                
                """
            ),
            HumanMessage(content=f"Task: {task}")
        ]


    else:
        prompt = [
            SystemMessage(
                content="""
                        You are a code writer assistant.
                        Improve previous draft based on the human feedback.
                        Keep the part of code that is already correct.
                        Return only the code without any extra additional text.
                        """
            ),
            HumanMessage(
                content=f"""
                Task: {task}
                Previous draft: {previous_draft}
                Human feedback: {human_feedback}
            """
            )
        ]

    response = llm.invoke(prompt)

    return {
        "draft": response.text
    }

#---------------------------------------------
# Human Approval
#---------------------------------------------

def human_approval(state: State):
    print("=" * 50)
    print("Human Approval Required...")
    print("=" * 50)
    print(f"Draft: {state['draft']}")
    print("=" * 50)

    decision = input("Is the draft aprooved? (y/n): ")

    while decision not in {"y", "n"}:
        print("invalid input, enter 'y' or 'n'.")
        decision = input("Is the draft aprooved? (y/n): ")

    if decision == "y":
        return{
            "approval_status": "approved",
            "human_feedback": ""
        }

    feedback = input("Enter your feedback: ")

    while not feedback:
        print("feedback can not be empty!!")
        feedback = input("Enter your feedback: ")

    return{
        "approval_status": "needs_revision",
        "human_feedback": feedback,
        "revision_count": state['revision_count'] + 1       
    }

#---------------------------------------------
# Max Revisions Node
#---------------------------------------------

def max_revision(state: State):
    return {
        "approval_status": "max_revisions_reached"
    }

#---------------------------------------------
# Router
#---------------------------------------------

def route_to_next_node(state: State):
    if state["approval_status"] == "approved":
        return END

    if state["revision_count"] >= 3:
        return "max_revision"

    return "code_writer"

#---------------------------------------------
# Graph
#---------------------------------------------

builder = StateGraph(State)


builder.add_node("code_writer", code_writer)
builder.add_node("human_approval", human_approval)
builder.add_node("max_revision", max_revision)


builder.add_edge(START, "code_writer")
builder.add_edge("code_writer", "human_approval")
builder.add_conditional_edges("human_approval", route_to_next_node)
builder.add_edge("max_revision", END)

graph = builder.compile()

#---------------------------------------------
# Run the graph
#---------------------------------------------

initial_state = {
    "task": "Write a function that returns the sum of two numbers in Python.",
    "draft": "",
    "approval_status": "pending",
    "human_feedback": "",
    "revision_count": 0
}

result = graph.invoke(initial_state)

print(f"Final draft: {result['draft']}")
print("=" * 50)
print(f"Approval status: {result['approval_status']}")
print("=" * 50)
print(f"Human feedback: {result['human_feedback']}")
print("=" * 50)
print(f"Revision count: {result['revision_count']}")

if result['approval_status'] == "max_revisions_reached":
    print("Max revisions reached. Code is not approved.")
