from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

MODEL_NAME = "gemini-3.5-flash-lite"

# model = ChatGoogleGenerativeAI(
#     model=MODEL_NAME
# )

# response = model.invoke("What is the capital of France?")
#
# print(response.text)
# print(response.usage_metadata)

#################################################################
# Prompt Templates
#################################################################

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
#

# model = ChatGoogleGenerativeAI(
#     model=MODEL_NAME
# )

# # prompt = ChatPromptTemplate.from_messages(
# #     [
# #         SystemMessage(content="You are a helpful Python assistant."),
# #         HumanMessage(content="When was the Python 3.0 released?"),
# #     ]
# # )
#
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a helpful {subject} assistant."),
#         ("human", "{question}"),
#     ]
# )
#
# prompt_input = prompt.invoke(
#     {
#         "subject": "Python",
#         "question": "When was the Python 3.0 released?"
#     }
# )
#
# # print(prompt_input)
#
# response = model.invoke(prompt_input)
#
# print(response.text)

#################################################################
# Chain
#################################################################

# from langchain_core.prompts import ChatPromptTemplate
#
# model = ChatGoogleGenerativeAI(
#     model=MODEL_NAME
# )
#
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a helpful {subject} assistant."),
#         ("human", "{question}"),
#     ]
# )
#
# chain = prompt | model
#
# response = chain.invoke(
#     {
#         "subject": "Python",
#         "question": "When was the Python 3.0 released?"
#     }
# )
#
# # print(type(response))
#
# print(response.text)


#################################################################
# Output Parsers
#################################################################

## StrOutputParser ##

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
#
# model = ChatGoogleGenerativeAI(
#     model=MODEL_NAME
# )
#
#
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a helpful {subject} assistant."),
#         ("human", "{question}"),
#     ]
# )
#
# parser = StrOutputParser()
#
# chain = prompt | model | parser
#
#
# response = chain.invoke(
#     {
#         "subject": "Python",
#         "question": "When was the Python 3.0 released?"
#     }
# )
#
# print(response)

## JsonOutputParser ##

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import JsonOutputParser
#
# model = ChatGoogleGenerativeAI(
#     model=MODEL_NAME
# )
#
#
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "Tell me about programming languages in JSON format. "),
#         ("human", "{question}"),
#     ]
# )
#
# parser = JsonOutputParser()
#
# chain = prompt | model | parser
#
# response = chain.invoke(
#     {
#         "question": "Tell me about Python"
#     }
# )
#
# print(type(response))


## PydanticOutputParser ##

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

model = ChatGoogleGenerativeAI(
    model=MODEL_NAME
)

class ProductReview(BaseModel):
    score: int = Field(ge=1, le=10)
    comment: str = Field(min_length=10)
    recommend: bool

parser = PydanticOutputParser(pydantic_object=ProductReview)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
        You are a helpful assistant.
        Analyze the following product review and provide:
        - a rating from 1 to 10
        - a short summary
        - whether you recommend the product

        {format_instructions}
        """),


        ("human", "{review}")
    ]
)

chain = prompt | model | parser


response = chain.invoke(
    {
        "review": "The Laptop is very good, but battery life is disappointing.",
        "format_instructions": parser.get_format_instructions()
    }
)

print(response)
print(type(response))