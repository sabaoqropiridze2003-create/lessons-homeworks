from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

MODEL = "gemini-3.5-flash-lite"

class State(TypedDict):
    product_text: str
    product_info: str
    marketing_text: str
    final_description: str

def extract(state: State):
    llm = ChatGoogleGenerativeAI(
        model=MODEL
    )

    prompt = f"""
        You are an AI assistant.
        Extract the core product information from the following raw text and format it clearly.
        Text:
        {state['product_text']}
        """   

    response = llm.invoke(prompt)

    return {
        "product_info": response.text
    }

def marketing(state: State):

    llm = ChatGoogleGenerativeAI(
        model=MODEL
    )

    prompt = f"""
    You are a marketing copywriter.
    Create an attractive marketing text for an online store based on the following product information:
    {state['product_info']}
    """

    response = llm.invoke(prompt)

    return {
        "marketing_text": response.text
    }

def format_node(state: State):
    formatted_text = f"""=== PRODUCT DESCRIPTION ===
\n{state['marketing_text']}
\n=== END ==="""

    return {
        "final_description": formatted_text
    }

builder = StateGraph(State)

builder.add_node("extract", extract)
builder.add_node("marketing", marketing)
builder.add_node("format", format_node)

builder.add_edge(START, "extract")
builder.add_edge("extract", "marketing")
builder.add_edge("marketing", "format")
builder.add_edge("format", END)

graph = builder.compile()

result = graph.invoke(
    {
    "product_text": "iphone 15, 6.1 inch oled, 128gb, a16 bionic, 48mp camera, usb-c, battery good, available in black and blue",
    "product_info": "",
    "marketing_text": "",
    "final_description": ""
}
)

print(result['final_description'])