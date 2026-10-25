# from dotenv import load_dotenv
# load_dotenv()

# from typing import TypedDict
# from langgraph.graph import StateGraph, START, END
# from langchain_google_genai import ChatGoogleGenerativeAI

# MODEL = "gemini-3.6-flash"

# llm = ChatGoogleGenerativeAI(
#         model=MODEL
#     )


# #=====================================
# # State
# #=====================================

# class State(TypedDict):
#     text: str
#     detected_language: str
#     translated_text: str


# #=====================================
# # Nodes
# #=====================================

# def detect_language(state: State):

#     prompt = f"""
#     You are a language detection model. Detect the language of the following text.
#     Text:
#     {state['text']}
#     return only the language name!
#     """

#     response = llm.invoke(prompt)

#     return {
#         "detected_language": response.text
#     }

# def translate_text(state: State):


#     prompt = f"""
#     You are a translation model. Translate the following text to English.
#     Text:
#     {state['text']}
#     return only the translated text!
#     """

#     response = llm.invoke(prompt)

#     return {
#         "translated_text": response.text
#     }

# #=====================================
# # Conditional Routing
# #=====================================

# def route_to_next_node(state: State):
#     if state["detected_language"].lower() == "english":
#         return END
#     return "translate"

# # #=====================================
# # # Graph
# # #=====================================


# builder = StateGraph(State)

# builder.add_node("detect", detect_language)
# builder.add_node("translate", translate_text)


# builder.add_edge(START, "detect")
# builder.add_conditional_edges("detect", route_to_next_node)
# builder.add_edge("translate", END)

# graph = builder.compile()

# while True:
#     text_to_translate = input("Enter the text to translate: ")

#     if text_to_translate.lower() in ["exit", "quit"]:
#         break

#     result = graph.invoke({
#         "text": text_to_translate
#     })

#     print(f"Detected language: {result.get('detected_language', 'Cannot detect language.')}")
#     print(f"Translated text: {result.get('translated_text', 'Text arleady in english')}")

############################### Cyclic Graph ################################

# from dotenv import load_dotenv
# load_dotenv()

# from typing import TypedDict
# from langgraph.graph import StateGraph, START, END
# from langchain_google_genai import ChatGoogleGenerativeAI

# MODEL = "gemini-3.6-flash"

# llm = ChatGoogleGenerativeAI(
#         model=MODEL
#     )

# #=====================================
# # State
# #=====================================

# class State(TypedDict):
#     original_text: str
#     current_text: str
#     attempts: int
#     is_short_enough: bool

# #=====================================
# # Nodes
# #===================================== 


# def summarize_text(state: State):
#     prompt = f"""
#     Summarize the following text while keeping the original meaning.

#     Text:
#     {state['current_text']}
#     """

#     response = llm.invoke(prompt)

#     return {
#         'current_text': response.text
#     }

# def check_length(state: State):

#     text = state['current_text']

#     is_short = len(text) <= 400

#     return {
#         'is_short_enough': is_short,
#         'attempts': state['attempts'] + 1
#     }

# #=====================================
# # Conditional Routing
# #=====================================

# def should_continue(state: State):
#     if state['is_short_enough']:
#         return END

#     if state['attempts'] >= 3:
#         return END

#     return 'summarize_text'

# #=====================================
# # Graph
# #=====================================

# builder = StateGraph(State)

# builder.add_node('summarize_text', summarize_text)
# builder.add_node('check_length', check_length)

# builder.add_edge(START, 'summarize_text')
# builder.add_edge('summarize_text', 'check_length')
# builder.add_conditional_edges('check_length', should_continue)

# graph = builder.compile()

# #=====================================
# # Run the graph
# #=====================================

# initial_text = """
#     Python is a powerful programming language that allows developers to build dynamic and interactive web applications.
#     Python is widely used in web development, data science, machine learning, and many other fields.
#     It is a versatile and easy-to-learn language that is suitable for both beginners and experienced developers.
#     Python is a popular choice for both beginners and experienced developers because of its simplicity, readability, and flexibility.
#     Python is widely used in a wide range of applications, from small business websites to large-scale enterprise systems.
#     """

# # print(len(initial_text))

# result = graph.invoke({
#     'original_text': initial_text,
#     'current_text': initial_text,
#     'attempts': 0,
#     'is_short_enough': False
# })


# print(result['current_text'])
# print(f"Attempts: {result['attempts']}")
# print(f"Is short enough: {result['is_short_enough']}")

############################### Agents Graph ################################

from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict, Annotated

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.tools import tool

from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    BaseMessage,
    ToolMessage,
    SystemMessage
)

# Tools
@tool
def calculator(expression: str) -> str:
    """Calculate a simple math expression."""

    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

@tool
def search_info(query: str) -> str:
    """Search simple builtin knowledge for basic topics."""

    base_knowledge = {
        "python": "Python is a programming language.",
        "langchain": "Langchain is a framework for building AI agents.",
        "langgraph": "Langgraph is a library for building stateful AI agents.",
        "postgres": "Postgres is a relational database management system.",
        "django": "Django is a high-level Python web framework."
    }

    query_lower = query.lower()

    for key, value in base_knowledge.items():
        if key in query_lower:
            return value

    return "Sorry, I don't know anything about that."

tools = [calculator, search_info]
tools_by_name = {tool.name: tool for tool in tools}

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

llm_with_tools = llm.bind_tools(tools)

class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def model_node(state: State):
    response = llm_with_tools.invoke(state['messages'])

    return {"messages": [response]}

def tool_node(state: State):
    last_message = state['messages'][-1]
    tool_messages = []

    for tool_call in last_message.tool_calls:
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        print(f"Invoking tool: {tool_name} with args: {tool_args}")

        result = tools_by_name[tool_name].invoke(tool_args)

        tool_messages.append(
            ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"]
            )
        )

    return {"messages": tool_messages}

def should_continue(state: State):
    last_message = state['messages'][-1]

    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return "tool_node"

    return END

builder = StateGraph(State)

builder.add_node("model_node", model_node)
builder.add_node("tool_node", tool_node)

builder.add_edge(START, "model_node")
builder.add_conditional_edges("model_node", should_continue)
builder.add_edge("tool_node", "model_node")

graph = builder.compile()

state: State = {
    "messages": [
        SystemMessage(content=(
            "You are a helpful assistant. "
            "Use calculator for math questions."
            "Use search_info for basic knowledge questions."
            "When you use search_info, answer with only tool result."
            "Don't add extra information."
        ))
    ]
}

print("Chat started. Type 'exit' to quit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    state = graph.invoke({"messages": state["messages"] + [HumanMessage(content=user_input)]})

    last_ai = None

    for message in reversed(state["messages"]):
        if isinstance(message, AIMessage):
            last_ai = message
            break

    if last_ai:
        print(f"Assistant: {last_ai.text}")