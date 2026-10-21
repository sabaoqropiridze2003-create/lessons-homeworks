from typing import TypedDict
from langgraph.graph import StateGraph, START, END


#=====================================
# State
#=====================================

class State(TypedDict):
    text: str
    analysis:str
    answer: str

#=====================================
# Nodes
#=====================================

def analyze(state: State):
    return {
        "analysis": f"The length of the text is {len(state['text'])}"
    }

def answer(state: State):
    return {
        "answer": f"The answer is: {state['analysis'].upper()}"
    }