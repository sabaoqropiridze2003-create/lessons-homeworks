from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

MODEL_NAME = "gemini-3.5-flash-lite"

# model = ChatGoogleGenerativeAI(
#     model=MODEL_NAME
# )

# response = model.invoke("what is the capirtal of country georgia?")

# print(response.text)
# print(response.usage_metadata)

#################################################################
# Prompt Templates
#################################################################

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


# model = ChatGoogleGenerativeAI(
#     model=MODEL_NAME
# )

# prompt = ChatPromptTemplate.from_messages(
#     [
#         SystemMessage(content="You are a helpfull Python assistant"),
#         HumanMessage(content="When was Python 3.0 released?"),
#     ]
# )

# prompt = ChatPromptTemplate.from_messages(
#     [
#     ("system", "You are a helpfull {subject} assistant"),
#     ("human", "{question}"),
#     ]
# )

# prompt_input = prompt.invoke(
#     {
#         "subject": "Python",
#         "question": "who created python" 
#     }
# )

# print(prompt_input)

# response = model.invoke(prompt_input)

# print(response.text)

#################################################################
# Chain
#################################################################

# from langchain_core.prompts import ChatPromptTemplate

# model = ChatGoogleGenerativeAI(
#     model=MODEL_NAME
# )

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a helpfull {subject} assistant"),
#         ("human", "{question}"),
#     ]
# )

# chain = prompt | model

# response = chain.invoke(
#     {
#         "subject": "Python",
#         "question": "who created python"
#     }
# )


# print(type(response))

# print(response.text)



#################################################################
# Output Parsers
#################################################################


## StrOutputParser ##

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# model = ChatGoogleGenerativeAI(
#     model=MODEL_NAME
# )

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a helpfull {subject} assistant"),
#         ("human", "{question}"),
#     ]
# )

# parser = StrOutputParser()

# chain = prompt | model | parser

# response = chain.invoke(
#     {
#         "subject": "Python",
#         "question": "When was python invented"
#     }
# )

# print(response)

## JsonOutputParser ##

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import JsonOutputParser

# model = ChatGoogleGenerativeAI(
#     model=MODEL_NAME
# )

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "Tell me about programming languages in JSON format"),
#         ("human", "{question}"),
#     ]
# )

# parser = JsonOutputParser()

# chain = prompt | model | parser

# response = chain.invoke(
#     {
#         "question": "Tell me about Python"
#     }
# )

# print(type(response))
# print(response)

## PydanticOutputParser ##

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

model = ChatGoogleGenerativeAI(
    model=MODEL_NAME
)

class ProducReview(BaseModel):
    score: int = Field(ge=1, le=10)
    comment: str = Field(min_length=10)
    recommend: bool


parser = PydanticOutputParser(pydantic_object=ProducReview)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
        You are a helpfull assistant.
        analize the following product review an provide:
        - a rating from 1 to 10
        - a short summary
        - wheter you recomend the product

        {format_instruction}
        """),
        ("human", "{review}")
    ]
)

chain = prompt | model | parser

response = chain.invoke(
    {
        "review": "the laptop is very good, but battery life is disappointing",
        "format_instruction": parser.get_format_instructions()
    }
)

print(response.score)
print(response.comment)
print(response.recommend)
