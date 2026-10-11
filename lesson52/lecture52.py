from dotenv import load_dotenv
load_dotenv() 

from google import genai
from google.genai import types

client = genai.Client()
MODEL = "gemini-3.5-flash-lite"

# system_prompt= """
# you are a helpful assistant that provides concise answers to questions, explaining concepts clearly so everyone can understand, even if they are not experts.
# """

# response = client.models.generate_content(
#     model=MODEL,
#     contents="what is the capital of france, and what is the population of the country? also, please provide a brief history of the country.",
#     config=types.GenerateContentConfig(
#         temperature=0.2,
#         max_output_tokens=100,
#         system_instruction=system_prompt,
#     )
# )

# print(response.text)
# print(response.usage_metadata.prompt_token_count)
# print(response.usage_metadata.candidates_token_count)
# print(response.usage_metadata.total_token_count)


#####################################################################################################
# History
#####################################################################################################

system_prompt = """
You are a Python teacher, use simple examples to explain concepts, use short sentences!
"""

messages = []

total_input_tokens = 0
total_output_tokens = 0

while True:
    user_input = input("User: ")

    if user_input.lower() in ["exit", "quit"]:
        print("exitting the chat.")
        break

    messages.append({
        "role": "user",
        "parts": [{"text": user_input}]
    })

    messages_to_send = messages[-4:]

    response = client.models.generate_content(
        model=MODEL,
        contents=messages_to_send,
        config=types.GenerateContentConfig(
            temperature=0.0,
            max_output_tokens=1000,
            system_instruction=system_prompt
        )
    )
    assistant_message = response.text

    print("=" * 50)
    print(f"Current input tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Current output tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Total tokens for this interaction: {response.usage_metadata.total_token_count}")
    print("=" * 50)

    total_input_tokens += response.usage_metadata.prompt_token_count
    total_output_tokens += response.usage_metadata.candidates_token_count

    print("=" * 50)
    print(f"Total input tokens: {total_input_tokens}")
    print(f"Total output tokens: {total_output_tokens}")
    print("=" * 50)

    print(f"Messages Length: {len(messages_to_send)}")

    print(f"Assistant: {assistant_message}")

    messages.append({
        "role": "model",
        "parts": [{"text": assistant_message}]
    })