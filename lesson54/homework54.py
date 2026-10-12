from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field


MODEL_NAME = "gemini-3.5-flash-lite"
model = ChatGoogleGenerativeAI(
    model=MODEL_NAME
)


class ProductAnalysis(BaseModel):
    sentiment: str = Field(
        description="The sentiment must be strictly one of: 'positive', 'negative', or 'neutral'."
    )
    pros: list[str] = Field(description="A list of positive aspects of the product.")
    cons: list[str] = Field(description="A list of negative aspects of the product.")
    summary: str = Field(description="A brief summary of the product review.")
    recommend: bool = Field(description="Whether the reviewer recommends purchasing the product (True or False).")


parser = PydanticOutputParser(pydantic_object=ProductAnalysis)


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a helpful product review analysis assistant. 
            Analyze the provided product review and extract the required structured information.
            For the 'sentiment' field, you must choose strictly between: 'positive', 'negative', or 'neutral'.

            {format_instructions}
            """
        ),
        ("human", "{review}")
    ]
)


chain = prompt | model | parser


test_reviews = [
    "This laptop is fast, lightweight, and has an excellent display. However, its battery life could be better.",
    "The phone is slow, overheats frequently, and the camera quality is disappointing.",
    "The headphones have average sound quality. They are comfortable, but the price is relatively high."
]


for i, review_text in enumerate(test_reviews, 1):
    print(f"\nTest {i}")
    print(f"Review: {review_text}\n")
    
    response = chain.invoke(
        {
            "review": review_text,
            "format_instructions": parser.get_format_instructions()
        }
    )
    
    print("Result")
    data = response.model_dump()
    for key, value in data.items():
        print(f"  {key}: {value}")
        
    print(f"Data type: {type(response)}")