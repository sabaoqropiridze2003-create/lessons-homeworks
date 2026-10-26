from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, SystemMessage


class State(TypedDict):
    user_request: str
    destination_info: str
    food_info: str
    budget_info: str
    final_plan: str



llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)


def destination_node(state: State):

    prompt = [
        SystemMessage(
            content="""
            You are a destination expert. 
            Analyze the destination from the user request,
            determine interesting activities, museums, and sights,
            and return recommendations.
            """
        ),
        HumanMessage(content=state["user_request"])
    ]

    response = llm.invoke(prompt)

    return {
        "destination_info": response.text
        }


def food_node(state: State):

    prompt = [
        SystemMessage(
            content="""
            You are a culinary expert. 
            Provide food and local restaurant recommendations. 
            Take into account the user's budget and preferences.
            Do not plan the whole trip, focus only on food.
            """
        ),
        HumanMessage(content=state["user_request"])
    ]

    response = llm.invoke(prompt)

    return {
        "food_info": response.text
        }



def budget_node(state: State):

    prompt = [
        SystemMessage(
            content="""
            You are a travel financial advisor. 
            Analyze the estimated travel costs based on the user request. 
            Break down the expenses into key categories:
            hotel, food, transport, and activities.
            """
        ),
        HumanMessage(content=state["user_request"])
    ]

    response = llm.invoke(prompt)

    return {
        "budget_info": response.text
        }


def planner_node(state: State):

    prompt = [
        SystemMessage(
            content="""
            You are a master travel planner. 
            Take the outputs from the destination, food, and budget agents,
            and combine them into a single, cohesive travel plan. 
            Do not generate information from scratch;
            synthesize the provided agent outputs into a final structured response.
            """
        ),
        HumanMessage(
            content=f"""
            User Request: {state['user_request']}
            Destination Recommendations: {state['destination_info']}
            Food Recommendations: {state['food_info']}
            Budget Breakdown: {state['budget_info']}
            """
        )
    ]

    response = llm.invoke(prompt)

    return {
        "final_plan": response.text
        }


builder = StateGraph(State)

builder.add_node("destination_agent", destination_node)
builder.add_node("food_agent", food_node)
builder.add_node("budget_agent", budget_node)
builder.add_node("planner_agent", planner_node)

builder.add_edge(START, "destination_agent")
builder.add_edge(START, "food_agent")
builder.add_edge(START, "budget_agent")

builder.add_edge("destination_agent", "planner_agent")
builder.add_edge("food_agent", "planner_agent")
builder.add_edge("budget_agent", "planner_agent")


builder.add_edge("planner_agent", END)

graph = builder.compile()


initial_state = {
    "user_request": "I want to go to Paris for 4 days. I am interested in museums, good local food, and I have a medium budget.",
    "destination_info": "",
    "food_info": "",
    "budget_info": "",
    "final_plan": ""
}

result = graph.invoke(initial_state)

print("=" * 50)
print("FINAL TRAVEL PLAN:")
print("=" * 50)
print(result["final_plan"])