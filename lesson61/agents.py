from dotenv import load_dotenv
load_dotenv()

from schemas import ReviewResult

from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt
from langgraph.checkpoint.memory import InMemorySaver

MAX_ATTEMPTS = 3

#---------------------------------------------
# State
#---------------------------------------------

class CodeReviewState(TypedDict):
    user_request: str
    generated_code: str

    review_status: str
    review_feedback: str

    attempts: int
    human_decision: str
    status: str

#---------------------------------------------
# Model
#---------------------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

reviewer_llm = llm.with_structured_output(ReviewResult)

#---------------------------------------------
# Code Writer Agent
#---------------------------------------------

def code_writer(state: CodeReviewState):
    system_prompt = """
        You are an expert Python developer.

        Your job is to write or improve Python code based on the user's request.

        Follow these rules:
        - Write correct, clean, readable, and maintainable Python code.
        - If a previous code draft and reviewer feedback are provided,
          improve the draft according to the feedback.
        - Preserve parts of the existing code that are already correct.
        - Do not introduce unnecessary changes.
        - Make sure the final code fully satisfies the user's request.
        - Return ONLY Python code.
        - Do not use Markdown code fences.
        - Do not provide explanations or comments outside the code.
        """

    human_prompt = f"""
        User request: {state['user_request']}
        Previous code draft: {state['generated_code']}
        Reviewer feedback: {state['review_feedback']}             
        """

    prompt = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ]

    response = llm.invoke(prompt)

    return {
        "generated_code": response.text,
        "attempts": state['attempts'] + 1,
        "status": "reviewing"
      
    }


#---------------------------------------------
# Code Reviewer Agent
#---------------------------------------------

def reviewer_node(state: CodeReviewState):
    system_prompt = """
        You are a strict and experienced senior Python code reviewer.

        Your job is to evaluate whether the generated code correctly
        satisfies the user's request.

        Review the code for:
        - correctness
        - whether it fully satisfies the user's requirements
        - logical errors
        - Python syntax and runtime issues
        - missing edge cases when relevant
        - unnecessary or problematic implementation choices

        Be objective and do not assume that the code is correct.

        If the code fully satisfies the request, mark it as "approved".

        If there is any significant problem that should be fixed,
        mark it as "rejected" and clearly explain what needs to be changed.

        Do not rewrite the code.
        Do not provide a corrected version of the code.
        """

    human_prompt = f"""
        User request: {state['user_request']}
        Generated code: {state['generated_code']}
        """

    prompt = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ]

    response = reviewer_llm.invoke(prompt)

    return {
        "review_status": response.status,
        "review_feedback": response.feedback,
        "status": "waiting_for_approval" if response.status == "approved" else "needs_revision"       
    }

#---------------------------------------------
# Router
#---------------------------------------------

def review_router(state: CodeReviewState):
    if state["review_status"] == "approved":
        return "human_approval"

    if state["attempts"] < MAX_ATTEMPTS:
        return "code_writer"

    return "human_approval"

#---------------------------------------------
# Human Approval
#---------------------------------------------
def human_approval(state: CodeReviewState):
    if state["attempts"] >= MAX_ATTEMPTS and state["review_status"] == "rejected":
        message = f"The code is rejected after {MAX_ATTEMPTS} attempts. Human Decision Required."
    else:
        message = "The code is approved by the reviewer. Human Approval Required."


    decision = interrupt(
        {
            "message": message,
            "code": state["generated_code"],
            "review_status": state['review_status'],
            "review_feedback": state['review_feedback'],
            "attempts": state['attempts']
        }
    )

    decision = str(decision).lower().strip()

    if decision not in {"approved", "rejected"}:
        raise ValueError("Invalid decision. Please enter 'approved' or 'rejected'.")

    return {
        "human_decision": decision,
        "status": "completed" if decision == "approved" else "rejected"
    }

#---------------------------------------------
# Graph
#---------------------------------------------

def build_graph():
    builder = StateGraph(CodeReviewState)

    builder.add_node("code_writer", code_writer)
    builder.add_node("reviewer", reviewer_node)
    builder.add_node("human_approval", human_approval)

    builder.add_edge(START, "code_writer")
    builder.add_edge("code_writer", "reviewer")
    builder.add_conditional_edges("reviewer", review_router)
    builder.add_edge("human_approval", END)

    checkpointer = InMemorySaver()

    return builder.compile(checkpointer=checkpointer)

graph = build_graph()