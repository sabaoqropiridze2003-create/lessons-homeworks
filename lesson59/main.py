from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

MODEL = "gemini-3.6-flash"

llm = ChatGoogleGenerativeAI(
        model=MODEL
    )

#=====================================
# State
#=====================================

class State(TypedDict):
    text: str
    detected_language: str
    translated_text: str

#=====================================
# Nodes
#=====================================

def detect_language(state: State):

    print("Detecting language...")

    prompt = f"""
    You are a language detection model. Detect the language of the following text.
    Text:
    {state['text']}
    return only the language name!
    """

    response = llm.invoke(prompt)

    return {
        "detected_language": response.text
    }

def translate_text(state: State):

    print("Translating...")

    prompt = f"""
    You are a translation model. Translate the following text to English.
    Text:
    {state['text']}
    return only the translated text!
    """

    response = llm.invoke(prompt)

    return {
        "translated_text": response.text
    }

#=====================================
# Conditional Routing
#=====================================

def route_to_next_node(state: State):
    if state["detected_language"].lower() == "english":
        return END
    return "translate_text"

# #=====================================
# # Graph
# #=====================================

builder = StateGraph(State)

builder.add_node("detect_language", detect_language)
builder.add_node("translate_text", translate_text)

builder.add_edge(START, "detect_language")
builder.add_conditional_edges('detect_language', route_to_next_node)
builder.add_edge("translate_text", END)

graph = builder.compile()

while True:
    text_to_translate = input("Enter the text to translate: ")

    result = graph.invoke({
        "text": text_to_translate
    })

    print(f"Detected language: {result.get('detected_language', 'Cannot detect language.')}")
    print(f"Translated text: {result.get('translated_text', 'Text already in English.')}")