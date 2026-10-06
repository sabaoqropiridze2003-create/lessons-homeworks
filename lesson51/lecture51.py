from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# response = client.models.generate_content(
#     model="gemini-3.1-flash-lite",
#     contents="what is python",
#     config=types.GenerateContentConfig(
#         system_instruction=(
#             "You are a it academy lecturer, You are explainig the concepts to the students"\
#             "Wich are complete beginers"
#         ),
#         automatic_function_calling=types.AutomaticFunctionCallingConfig(
#             disable=True
#         ),
#         max_output_tokens=300
#     ),
# )

#############################################################################################################################

# prompt="""
# Explain what python is.
# Target audiance: University computer science students who have minimal coding experience.
# Constraints:
# - Maximum 3 sentences.
# - Use Business/real life analogy instead of deep technical jargon/vocabulary.
# """

# response = client.models.generate_content(
#     model="gemini-3.1-flash-lite",
#     contents=prompt,
#     config=types.GenerateContentConfig(

#         automatic_function_calling=types.AutomaticFunctionCallingConfig(
#             disable=True
#         ),
#         max_output_tokens=300
#     ),
# )

#############################################################################################################################

# prompt="""
# Explain what python is, provide the answer strictly byusing the following structure:
# 1.core definition: 1 sentence,
# 2.primary use in Business (one sentence),
# 3. Developer use advantages (two sentences)
# """

# response = client.models.generate_content(
#     model="gemini-3.1-flash-lite",
#     contents=prompt,
#     config=types.GenerateContentConfig(

#         automatic_function_calling=types.AutomaticFunctionCallingConfig(
#             disable=True
#         ),
#         max_output_tokens=300,
#         temperature=0.3
#     ),
# )

#############################################################################################################################

# user_query = input("Enter a question or topic you want explained: ")

# prompt="""
# Question: {user_query}
# """

# response = client.models.generate_content(
#     model="gemini-3.1-flash-lite",
#     contents=prompt,
#     config=types.GenerateContentConfig(

#         system_instruction=(
#             "You are an expert in AI software arcitecturing and engeneering, you are strong"\
#             "comunicator. You should write crisp high signal documentation"\
#             "Context: Explain to future developers and managers, who have decent experience in coding."
#         ),

#         automatic_function_calling=types.AutomaticFunctionCallingConfig(
#             disable=True
#         ),
#         max_output_tokens=500
#     ),
# )

# print("-------------------------------Response from the 3rd version--------------------------")
# print(response.text)


#================================================================================================

chat_history = [
    {
        "role": "user",
        "parts": [{"text": "what is a decorator?"}],
    },
    {
        "role": "model",
        "parts": [
            {
                "text": "A decorator in Python is a design pattern that allows you to modify the behavior of"\
                " a function or class. It is a function that takes another function as an argument, adds some"\
                " functionality to it, and returns it. Decorators are often used for logging, access control, memoization, and other cross-cutting concerns."
            }
            ],

    }
]

chat = client.chats.create(
    model="gemini-3.1-flash-lite",
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are an experienced senior software engineer and programming mentor. "
            "Explain technical concepts clearly, adapt your explanations to the user's level, "
            "and use practical examples when appropriate."
        ),
        max_output_tokens=1000,
        temperature=0.0
    ),
    history=chat_history,
)

user_input = input("You: ").strip()

response = chat.send_message(user_input)
print(f"\nAI: {response.text}\n")