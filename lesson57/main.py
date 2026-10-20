# from dotenv import load_dotenv
# load_dotenv()

# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.tools import tool
# from langchain_core.messages import ToolMessage

# MODEL = "gemini-3.5-flash-lite"

# @tool
# def calculate(a: int, b: int):
#     """Calculate just the sum of two numbers!"""

#     return a + b

# llm = ChatGoogleGenerativeAI(
#     model=MODEL
# )

# llm_with_tools = llm.bind_tools([calculate])

# question = "what is 8 + 2?"

# answer = llm_with_tools.invoke(question)

# # print(answer)
# # print(answer.tool_calls)

# tool_call = answer.tool_calls[0]

# result = calculate.invoke(tool_call["args"])

# # print(result)
# # print(type(result))

# tool_message = ToolMessage(
#     tool_call_id=tool_call["id"],
#     content=str(result),
# )

# messages = [
#     {
#         "role": "user",
#         "content": question
#     },
#     answer,
#     tool_message
# ]

# final_answer = llm_with_tools.invoke(messages)
# # print(final_answer)
# print(final_answer.text)

##########################################################
# Several Tools
##########################################################

# from dotenv import load_dotenv
# load_dotenv()

# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import ToolMessage
# from langchain.tools import tool

# MODEL = "gemini-3.5-flash-lite"

# @tool
# def calculate(a: int, b: int):
#     """Calculate just the sum of two numbers!"""
#     return a + b

# @tool
# def get_weather(city: str):
#     """Get the weather in a given city"""
#     weather_data = {
#         "tbilisi": "Sunny, 25 degrees Celsius",
#         "new york": "Cloudy, 18 degrees Celsius",
#         "london": "Rainy, 12 degrees Celsius",
#         "paris": "Sunny, 20 degrees Celsius"
#     }
#     return weather_data.get(city.lower(), "Weather data not available for this city")

# @tool
# def search_product(product_name: str):
#     """Search for a product and return its price"""
#     product_data = {
#         "laptop": "$999",
#         "smartphone": "$699",
#         "headphones": "$199",
#         "camera": "$499"
#     }

#     product_price = product_data.get(product_name.lower(), "product not found") 

#     if product_price:
#         return f"The price of {product_name} is {product_price}"

#     return "Product not found"

# llm = ChatGoogleGenerativeAI(
#     model=MODEL
# )

# tools = [calculate, get_weather, search_product]

# llm_with_tools = llm.bind_tools(tools)

# question = input("Enter your question: ")

# response = llm_with_tools.invoke(question)

# # print(response.tool_calls)

# tool_results = []

# for tool_call in response.tool_calls:
#     tool_name = tool_call["name"]
#     tool_args = tool_call["args"]

#     print(f"Executing tool: {tool_name}")
#     print(f"Tool argument: {tool_args}")

#     selected_tool = next(tool for tool in tools if tool_name ==tool.name)

#     result = selected_tool.invoke(tool_args)

#     tool_results.append(ToolMessage(
#         tool_call_id=tool_call["id"],
#         content=str(result)
#     ))

# messages = [
#     {
#         "role": "user",
#         "content": question
#     },
#     response,
#     *tool_results
# ]

# final_response = llm_with_tools.invoke(messages)

# print("Final answer")
# print(final_response.text)

##########################################################
# Agent with Several Tools
##########################################################

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_agent

MODEL = "gemini-3.5-flash-lite"

@tool
def calculate(a: int, b: int):
    """Calculate just the sum of two numbers!"""
    return a + b


@tool
def get_weather(city: str):
    """Get the weather in a given city"""

    weather_data = {
        "tbilisi": "Sunny, 25 degrees Celsius",
        "new york": "Cloudy, 18 degrees Celsius",
        "london": "Rainy, 12 degrees Celsius",
        "paris": "Sunny, 20 degrees Celsius"
    }

    return weather_data.get(city.lower(), "Weather data not available for this city.")

@tool
def search_product(product_name: str):
    """Search for a product and return its price"""

    product_data = {
        "laptop": "$999",
        "smartphone": "$699",
        "headphones": "$199",
        "camera": "$499"
    }

    product_price = product_data.get(product_name.lower(), "Product not found.")

    if product_price:
        return f"The price of {product_name} is {product_price}."

    return "Product not found."


llm = ChatGoogleGenerativeAI(
    model=MODEL
)

tools = [calculate, get_weather, search_product]

agent = create_agent(
    model=llm,
    tools=tools
)

question = input("Enter your question: ")

result = agent.invoke({
    "messages": {
        "role": "user",
        "content": question
    }
})

print(result["messages"][-1].text)

