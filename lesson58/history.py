from dotenv import load_dotenv
load_dotenv()

from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

MODEL = "gemini-3.5-flash-lite"

#=====================================
# State
#=====================================

class State(TypedDict):
    messages: Annotated[list, add_messages]

#=====================================
# Nodes
#=====================================

def chatbot_node(state: State):
    llm = ChatGoogleGenerativeAI(model=MODEL)
    response = llm.invoke(state["messages"])
    return {
        "messages": [response]
    }

#=====================================
# Graph
#=====================================

builder = StateGraph(State)

builder.add_node("chatbot", chatbot_node)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)

graph = builder.compile()

#=====================================
# Manual State Management (Like your image)
#=====================================

chat_state = {
    "messages": [
        SystemMessage(content=(
            "You are a helpful lecturer model assistant."
        ))
    ]
}

print("Chatbot initialized with manual history! Type 'exit' or 'quit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    # 1. Append the new user message manually to our local state list
    chat_state["messages"].append(HumanMessage(content=user_input))

    # 2. Invoke the graph passing the accumulated state dictionary
    result = graph.invoke(chat_state)

    # 3. Update our local state with the graph's returned messages history
    chat_state = result
    print(chat_state)
    print("=" * 50)

    # 4. Print the latest AI response
    ai_response = chat_state["messages"][-1]
    print(f"AI: {ai_response}\n")