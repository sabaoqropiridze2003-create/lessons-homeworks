# from dotenv import load_dotenv
# load_dotenv()
#
# from typing import TypedDict
# from langgraph.graph import StateGraph, START, END
# from langchain_google_genai import ChatGoogleGenerativeAI
#
# MODEL = "gemini-3.5-flash-lite"
#
# #=====================================
# # State
# #=====================================
#
# class State(TypedDict):
#     text: str
#     detected_language: str
#     translated_text: str
#
# #=====================================
# # Nodes
# #=====================================
#
# def detect_language(state: State):
#
#     llm = ChatGoogleGenerativeAI(
#         model=MODEL
#     )
#
#     prompt = f"""
#     You are a language detection model. Detect the language of the following text.
#     Text:
#     {state['text']}
#     return only the language name!
#     """
#
#     response = llm.invoke(prompt)
#
#     return {
#         "detected_language": response.text
#     }
#
# def translate_text(state: State):
#
#     llm = ChatGoogleGenerativeAI(
#         model=MODEL
#     )
#
#     prompt = f"""
#     You are a translation model. Translate the following text to Georgian.
#     Text:
#     {state['text']}
#     return only the translated text!
#     """
#
#     response = llm.invoke(prompt)
#
#     return {
#         "translated_text": response.text
#     }
#
#
# # #=====================================
# # # Graph
# # #=====================================
#
# builder = StateGraph(State)
#
# builder.add_node("detect_language", detect_language)
# builder.add_node("translate_text", translate_text)
#
# builder.add_edge(START, "detect_language")
# builder.add_edge("detect_language", "translate_text")
# builder.add_edge("translate_text", END)
#
# graph = builder.compile()
#
# while True:
#     text_to_translate = input("Enter the text to translate: ")
#
#     result = graph.invoke({
#         "text": text_to_translate
#     },
#     config={
#         "run_name": "Translation",
#         "tags": ["translation", "detection"],
#         "metadata": {
#             "version": "1.0.0",
#             "author": "Otar"
#         }
#     }
#     )
#
#     print(f"Detected language: {result.get('detected_language', 'Cannot detect language.')}")
#     print(f"Translated text: {result.get('translated_text', 'Translation failed.')}")

# from dotenv import load_dotenv
# load_dotenv()
#
# from langsmith import traceable
#
# @traceable(
#     name="Text Validator",
#     run_type="tool",
#     tags=["validation", "text-processing"],
#     metadata={
#         "version": "1.0"
#     }
# )
# def validate_text(text: str):
#     return len(text) >= 10
#
# print(validate_text("Hello, LangSmith!"))

# @traceable
# def validate_text(text: str):
#     if len(text) < 10:
#         return False
#     return True
#
# @traceable
# def count_words(text: str):
#     return len(text.split())
#
# @traceable
# def process_text(text: str):
#     is_valid = validate_text(text)
#     if not is_valid:
#         return "Invalid text"
#     words = count_words(text)
#     return {"status": "success", "word_count": words}
#
# result = process_text("Learning LangSmith is interesting")
# print(result)


from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from langsmith import Client, evaluate


MODEL = "gemini-3.5-flash-lite"
DATASET_NAME = "Language Translation Dataset"


# =====================================
# LLM
# =====================================

llm = ChatGoogleGenerativeAI(
    model=MODEL
)


# =====================================
# State
# =====================================

class State(TypedDict):
    text: str
    detected_language: str
    translated_text: str


# =====================================
# Nodes
# =====================================

def detect_language(state: State):

    prompt = f"""
    You are a language detection model.
    Detect the language of the following text.

    Text:
    {state['text']}

    Return only the language name!
    """

    response = llm.invoke(prompt)

    return {
        "detected_language": response.text.strip()
    }


def translate_text(state: State):

    prompt = f"""
    You are a translation model.
    Translate the following text to Georgian.

    Text:
    {state['text']}

    Return only the translated text!
    """

    response = llm.invoke(prompt)

    return {
        "translated_text": response.text.strip()
    }


# =====================================
# Graph
# =====================================

builder = StateGraph(State)

builder.add_node("detect_language", detect_language)
builder.add_node("translate_text", translate_text)

builder.add_edge(START, "detect_language")
builder.add_edge("detect_language", "translate_text")
builder.add_edge("translate_text", END)

graph = builder.compile()


# =====================================
# LangSmith Dataset
# =====================================

client = Client()

examples = [
    {
        "inputs": {
            "text": "Hello, how are you?"
        },
        "outputs": {
            "detected_language": "English",
            "translated_text": "გამარჯობა, როგორ ხარ?"
        }
    },
    {
        "inputs": {
            "text": "Bonjour, comment allez-vous?"
        },
        "outputs": {
            "detected_language": "French",
            "translated_text": "გამარჯობა, როგორ ხართ?"
        }
    },
    {
        "inputs": {
            "text": "Guten Morgen, wie geht es dir?"
        },
        "outputs": {
            "detected_language": "German",
            "translated_text": "დილა მშვიდობისა, როგორ ხარ?"
        }
    }
]

if client.has_dataset(dataset_name=DATASET_NAME):

    dataset = client.read_dataset(
        dataset_name=DATASET_NAME
    )

    print("Using existing Dataset.")

else:

    dataset = client.create_dataset(
        dataset_name=DATASET_NAME,
        description="Dataset for testing language detection and Georgian translation"
    )

    client.create_examples(
        dataset_id=dataset.id,
        examples=examples
    )

    print("New Dataset created with examples.")


existing_examples = list(
    client.list_examples(dataset_id=dataset.id)
)

if not existing_examples:

    client.create_examples(
        dataset_id=dataset.id,
        examples=examples
    )

    print("Examples added to existing Dataset.")


# =====================================
# Target Function
# =====================================

def target(inputs: dict) -> dict:

    result = graph.invoke(
        {
            "text": inputs["text"]
        },
        config={
            "run_name": "Language Detection and Translation",
            "tags": ["language_detection", "translation"],
            "metadata": {
                "version": "1.0",
                "model": MODEL
            }
        }
    )

    return {
        "detected_language": result["detected_language"],
        "translated_text": result["translated_text"]
    }


# =====================================
# Evaluator
# =====================================

def language_detection_correct(
    outputs: dict,
    reference_outputs: dict
) -> bool:

    actual = outputs["detected_language"].strip().lower()
    expected = reference_outputs["detected_language"].strip().lower()

    return actual == expected


# =====================================
# Evaluation
# =====================================

results = evaluate(
    target,
    data=DATASET_NAME,
    evaluators=[language_detection_correct],
    experiment_prefix="language-translation-test",
    max_concurrency=1
)

print("Evaluation completed!")