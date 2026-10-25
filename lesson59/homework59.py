from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

MODEL = "gemini-3.5-flash-lite"

llm = ChatGoogleGenerativeAI(
    model=MODEL
)

class State(TypedDict):
    ingredients: str
    recipe: str
    feedback: str
    approved: bool
    attempts: int


def generate_recipe(state: State):
    prompt = f"""
    You are a professional chef. Create a simple and clear recipe using the following ingredients:
    {state['ingredients']}
    
    Provide a clear title, ingredients list, and step-by-step cooking instructions.
    """

    response = llm.invoke(prompt)

    return {
        "recipe": response.text,
        "attempts": state["attempts"] + 1
    }


def check_recipe(state: State):
    prompt = f"""
    You are a strict food critic and recipe reviewer. Check the following recipe based on these ingredients:
    {state['ingredients']}
    
    Recipe to check:
    {state['recipe']}
    
    Evaluate whether:
    1. The specified ingredients are used.
    2. The recipe is clear and understandable.
    3. It has cooking steps.
    4. Ingredient quantities/proportions are logical.
    
    Respond strictly in the following format (Python boolean for approved, and string for feedback):
    APPROVED: True (or False)
    FEEDBACK: Your detailed feedback here.
    """

    response = llm.invoke(prompt)
    content = response.text

    approved = False
    if "APPROVED: True" in content:
        approved = True

    return {
        "feedback": content,
        "approved": approved
    }


def improve_recipe(state: State):
    prompt = f"""
    You are a professional chef. Improve the existing recipe based on the feedback provided.
    
    Ingredients: {state['ingredients']}
    Current Recipe: {state['recipe']}
    Feedback: {state['feedback']}
    
    Rewrite the recipe fixing the issues mentioned in the feedback.
    """

    response = llm.invoke(prompt)

    return {
        "recipe": response.text,
        "attempts": state["attempts"] + 1
    }

MAX_ATTEMPTS = 3

def should_continue(state: State):
    if state["approved"]:
        return END
    
    if state["attempts"] >= MAX_ATTEMPTS:
        return END
        
    return "improve"


builder = StateGraph(State)

builder.add_node("generate_recipe", generate_recipe)
builder.add_node("check_recipe", check_recipe)
builder.add_node("improve", improve_recipe)

builder.add_edge(START, "generate_recipe")
builder.add_edge("generate_recipe", "check_recipe")

builder.add_conditional_edges("check_recipe", should_continue)

builder.add_edge("improve", "check_recipe")

graph = builder.compile()

initial_state = {
    "ingredients": "chicken, rice, onion, tomato",
    "recipe": "",
    "feedback": "",
    "approved": False,
    "attempts": 0
}

result = graph.invoke(initial_state)

print("=== final recipe ===")
print(result["recipe"])

print("\n=== final Feedback ===")
print(result["feedback"])

print(f"\nAttempts: {result['attempts']}")
print(f"Aprooved: {result['approved']}")