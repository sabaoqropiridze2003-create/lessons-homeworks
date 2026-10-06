# import os
# from dotenv import load_dotenv
# from google import genai
# from google.genai import types

# load_dotenv()

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# chat_history = []

# chat = client.chats.create(
#     model="gemini-3.1-flash-lite",
#     config=types.GenerateContentConfig(
#         system_instruction=(
#             "You are an experienced senior software engineer and programming mentor. "
#             "Explain technical concepts clearly, adapt your explanations to the user's level, "
#             "and use practical examples when appropriate."
#         ),
#     ),
#     history=chat_history,
# )

# while True:
#     user_input = input("You: ").strip()

#     if not user_input:
#         continue

#     if user_input.lower() == "exit":
#         print("\nGoodbye!")
#         break

#     if user_input.lower() == "history":
#         print("\n--- Conversation History ---")
#         if not chat_history:
#             print("No history yet.")
#         else:
#             for item in chat_history:

#                 if item["role"] == "user":
#                     role_label = "USER"
#                 else:
#                     role_label = "ASSISTANT"

#                 text = item["parts"][0]["text"]

#                 print()
#                 print(f"{role_label}:")
#                 print(text)

#             print("----------------------------\n")
#             continue

#     response = chat.send_message(user_input)
#     print(f"\nAI: {response.text}\n")

#     chat_history.append({
#         "role": "user",
#         "parts": [{"text": user_input}]
#     })
#     chat_history.append({
#         "role": "model",
#         "parts": [{"text": response.text}]
#     })