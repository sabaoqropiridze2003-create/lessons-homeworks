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

# system_prompt = """
# You are a Python teacher, use simple examples to explain concepts, use short sentences!
# """

# messages = []

# total_input_tokens = 0
# total_output_tokens = 0

# while True:
#     user_input = input("User: ")

#     if user_input.lower() in ["exit", "quit"]:
#         print("exitting the chat.")
#         break

#     messages.append({
#         "role": "user",
#         "parts": [{"text": user_input}]
#     })

#     messages_to_send = messages[-6:]

#     response = client.models.generate_content(
#         model=MODEL,
#         contents=messages_to_send,
#         config=types.GenerateContentConfig(
#             temperature=0.0,
#             max_output_tokens=1000,
#             system_instruction=system_prompt
#         )
#     )
#     assistant_message = response.text

#     print("=" * 50)
#     print(f"Current input tokens: {response.usage_metadata.prompt_token_count}")
#     print(f"Current output tokens: {response.usage_metadata.candidates_token_count}")
#     print(f"Total tokens for this interaction: {response.usage_metadata.total_token_count}")
#     print("=" * 50)

#     total_input_tokens += response.usage_metadata.prompt_token_count
#     total_output_tokens += response.usage_metadata.candidates_token_count

#     print("=" * 50)
#     print(f"Total input tokens: {total_input_tokens}")
#     print(f"Total output tokens: {total_output_tokens}")
#     print("=" * 50)

#     print(f"Messages Length: {len(messages_to_send)}")

#     print(f"Assistant: {assistant_message}")

#     messages.append({
#         "role": "model",
#         "parts": [{"text": assistant_message}]
#     })

##################################################################################################
# Summarize
##################################################################################################

# SYSTEM_PROMPT = """
# You are a helpful Python instructor.

# Explain Python concepts clearly.
# Use simple language.
# """

# SUMMARY_SYSTEM_PROMPT = """
# You summarize conversations.

# Keep only information required
# to continue the conversation later.

# Include:

# - user's goals
# - important facts
# - technical decisions
# - unresolved questions

# Ignore greetings and small talk.
# """

# conversation_summary = ""
# messages = []

# MAX_HISTORY = 6
# KEEP_LAST_MESSAGES = 4

# def summarize_conversation(summary: str, old_messages: list) -> str:

#     conversation = "\n".join(
#         f"{m['role']}: {m['parts'][0]['text']}"
#         for m in old_messages
#     )

#     response = client.models.generate_content(
#         model=MODEL,
#         contents=f"""
# Previous summary:

# {summary or "No previous summary."}

# New conversation:

# {conversation}

# Update the summary.
# """,
#         config=types.GenerateContentConfig(
#             system_instruction=SUMMARY_SYSTEM_PROMPT,
#             max_output_tokens=400
#         )
#     )

#     return response.text


# while True:

#     user_input = input("\nYou: ")

#     if user_input.lower() == "exit":
#         break

#     if len(messages) >= MAX_HISTORY:

#         old_messages = messages[:-KEEP_LAST_MESSAGES]

#         conversation_summary = summarize_conversation(
#             conversation_summary,
#             old_messages
#         )

#         messages = messages[-KEEP_LAST_MESSAGES:]

#     api_messages = []

#     if conversation_summary:

#         api_messages.append({
#             "role": "user",
#             "parts": [
#                 {
#                     "text": f"""
# Previous conversation summary:

# {conversation_summary}
# """
#                 }
#             ]
#         })

#         api_messages.append({
#             "role": "model",
#             "parts": [
#                 {
#                     "text": "Summary received. I'll use it as context."
#                 }
#             ]
#         })

#     api_messages.extend(messages)

#     api_messages.append({
#         "role": "user",
#         "parts": [
#             {
#                 "text": user_input
#             }
#         ]
#     })

#     response = client.models.generate_content(
#         model=MODEL,
#         contents=api_messages,
#         config=types.GenerateContentConfig(
#             system_instruction=SYSTEM_PROMPT,
#             max_output_tokens=500
#         )
#     )

#     answer = response.text

#     print("\nGemini:", answer)

#     print("\nUsage")
#     print("----------------------------")
#     print("Input :", response.usage_metadata.prompt_token_count)
#     print("Output:", response.usage_metadata.candidates_token_count)
#     print("Summary:", bool(conversation_summary))
#     print("----------------------------")

#     messages.append({
#         "role": "user",
#         "parts": [
#             {
#                 "text": user_input
#             }
#         ]
#     })

#     messages.append({
#         "role": "model",
#         "parts": [
#             {
#                 "text": answer
#             }
#         ]
#     })

##################################################################################################
# Tokenizer
##################################################################################################

# token_info = client.models.count_tokens(
#     model=MODEL,
#     contents="What is the capital of France?"
# )
#
# print(token_info.total_tokens)

# SYSTEM_PROMPT = """
# You are a helpful Python instructor.
#
# Explain concepts clearly.
# Use simple language.
# """
#
# SUMMARY_SYSTEM_PROMPT = """
# You summarize conversations.
#
# Keep only important information.
#
# Include:
#
# - user goals
# - important facts
# - technical decisions
# - unresolved questions
#
# Ignore greetings and small talk.
# """
#
# MAX_INPUT_TOKENS = 1000
# KEEP_LAST_MESSAGES = 4
#
# conversation_summary = ""
# messages = []
#
#
# def summarize_conversation(summary: str, old_messages: list) -> str:
#
#     conversation = "\n".join(
#         f"{m['role']}: {m['parts'][0]['text']}"
#         for m in old_messages
#     )
#
#     response = client.models.generate_content(
#         model=MODEL,
#         contents=f"""
# Previous Summary:
#
# {summary or "No summary"}
#
# New Conversation:
#
# {conversation}
#
# Create an updated summary.
# """,
#         config=types.GenerateContentConfig(
#             system_instruction=SUMMARY_SYSTEM_PROMPT,
#             max_output_tokens=400
#         )
#     )
#
#     return response.text
#
#
# while True:
#
#     user_input = input("\nYou: ")
#
#     if user_input.lower() == "exit":
#         break
#
#     api_messages = []
#
#     if conversation_summary:
#
#         api_messages.append({
#             "role": "user",
#             "parts": [
#                 {
#                     "text": f"""
# Previous Conversation Summary:
#
# {conversation_summary}
# """
#                 }
#             ]
#         })
#
#         api_messages.append({
#             "role": "model",
#             "parts": [
#                 {
#                     "text": "Summary received."
#                 }
#             ]
#         })
#
#     api_messages.extend(messages)
#
#     api_messages.append({
#         "role": "user",
#         "parts": [
#             {
#                 "text": user_input
#             }
#         ]
#     })
#
#     token_info = client.models.count_tokens(
#         model=MODEL,
#         contents=api_messages
#     )
#
#     print(f"\nCurrent Input Tokens: {token_info.total_tokens}")
#
#     if token_info.total_tokens > MAX_INPUT_TOKENS:
#
#         print("\n[Creating Conversation Summary]\n")
#
#         old_messages = messages[:-KEEP_LAST_MESSAGES]
#
#         conversation_summary = summarize_conversation(
#             conversation_summary,
#             old_messages
#         )
#
#         messages = messages[-KEEP_LAST_MESSAGES:]
#
#         api_messages = []
#
#         if conversation_summary:
#
#             api_messages.append({
#                 "role": "user",
#                 "parts": [
#                     {
#                         "text": f"""
# Previous Conversation Summary:
#
# {conversation_summary}
# """
#                     }
#                 ]
#             })
#
#             api_messages.append({
#                 "role": "model",
#                 "parts": [
#                     {
#                         "text": "Summary received."
#                     }
#                 ]
#             })
#
#         api_messages.extend(messages)
#
#         api_messages.append({
#             "role": "user",
#             "parts": [
#                 {
#                     "text": user_input
#                 }
#             ]
#         })
#
#     response = client.models.generate_content(
#         model=MODEL,
#         contents=api_messages,
#         config=types.GenerateContentConfig(
#             system_instruction=SYSTEM_PROMPT,
#             max_output_tokens=500
#         )
#     )
#
#     answer = response.text
#
#     print("\nGemini:")
#     print(answer)
#
#     messages.append({
#         "role": "user",
#         "parts": [
#             {
#                 "text": user_input
#             }
#         ]
#     })
#
#     messages.append({
#         "role": "model",
#         "parts": [
#             {
#                 "text": answer
#             }
#         ]
#     })
#
#     print("\n---------- Usage ----------")
#     print(
#         "Input Tokens :",
#         response.usage_metadata.prompt_token_count
#     )
#     print(
#         "Output Tokens:",
#         response.usage_metadata.candidates_token_count
#     )
#     print(
#         "Summary      :",
#         bool(conversation_summary)
#     )
#     print("---------------------------")

#########################################################################################################
# Structured Output
#########################################################################################################


from pydantic import BaseModel, Field

class ProductReview(BaseModel):
    score: int = Field(ge=1, le=10)
    comment: str = Field(min_length=10)

review = """
The laptop is very fast and the screen is excellent.
The keyboard is comfortable, but the battery life
is disappointing.
"""
response = client.models.generate_content(
    model=MODEL,
    contents=review,

    config = types.GenerateContentConfig(
        system_instruction="""
        You are a product review analyzer.

        Analyze the user's review and provide:
        - a score from 1 to 10
        - a short explanation of the score
        """,

        response_mime_type="application/json",
        response_schema=ProductReview
    )
)

result = response.parsed

print(result)
print(type(result))


print("*" * 50)
print(result.score)
print(result.comment)
print("*" * 50)

print(result.model_dump_json(indent=2))