from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import ToolMessage
from langchain.tools import tool

MODEL = "gemini-3.5-flash-lite"

@tool
def search_hotel(city: str):
    """Returns a list of available hotels in a given city with prices in GEL."""
    hotels_data = {
        "tbilisi": "Rooms Hotel Tbilisi — 350 GEL/night, Stamba Hotel — 400 GEL/night, Radisson Blu Iveria Hotel — 450 GEL/night",
        "batumi": "Radisson Blu Hotel Batumi — 320 GEL/night, Hilton Batumi — 380 GEL/night",
        "paris": "Hotel Eiffel — 350 GEL/night, Hotel Louvre — 400 GEL/night"
    }
    return hotels_data.get(city.lower(), "No hotel data available for this city.")

@tool
def get_exchange_rate(currency: str):
    """Returns the exchange rate of a given currency against GEL."""
    rates_data = {
        "usd": "1 USD → 2.70 GEL",
        "eur": "1 EUR → 3.15 GEL",
        "gbp": "1 GBP → 3.60 GEL"
    }
    return rates_data.get(currency.lower(), "Exchange rate not available for this currency.")

@tool
def search_attractions(city: str):
    """Returns a list of popular attractions in a given city."""
    attractions_data = {
        "tbilisi": "Narikala Fortress, Old Tbilisi, Mtatsminda Park, Sameba Cathedral",
        "batumi": "Batumi Boulevard, Piazza Square, Argo Cable Car",
        "paris": "Eiffel Tower, Louvre Museum, Notre-Dame Cathedral"
    }
    return attractions_data.get(city.lower(), "Attractions data not available for this city.")

llm = ChatGoogleGenerativeAI(
    model=MODEL
)

tools = [search_hotel, get_exchange_rate, search_attractions]

llm_with_tools = llm.bind_tools(tools)

question = input("enter your question: ")

response = llm_with_tools.invoke(question)

tool_results = []

for tool_call in response.tool_calls:
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    print(f"Executing tool: {tool_name}")
    print(f"Tool argument: {tool_args}")

    selected_tool = next(tool for tool in tools if tool_name == tool.name)

    result = selected_tool.invoke(tool_args)

    tool_results.append(ToolMessage(
        tool_call_id=tool_call["id"],
        content=str(result)
    ))

messages = [
    {
        "role": "user",
        "content": question
    },
    response,
    *tool_results
]

final_response = llm_with_tools.invoke(messages)

print("Final answer")
print(final_response.text)
