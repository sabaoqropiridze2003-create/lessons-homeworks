from dotenv import load_dotenv
load_dotenv()

EMBEDDING_MODEL = "gemini-embedding-001"

# from langchain_community.document_loaders import UnstructuredMarkdownLoader

# loader = UnstructuredMarkdownLoader("lesson55/data/company_info.md")

# docs = loader.load()
# print(len(docs))

# print(f"Data: {docs[0].page_content}")
# print(f"Metadata: {docs[0].metadata}")

############################################################################
# Chunking
############################################################################

# from langchain_community.document_loaders import UnstructuredMarkdownLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# loader = UnstructuredMarkdownLoader("lesson55/data/company_info.md")

# docs = loader.load()

# splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=40)

# chunks = splitter.split_documents(docs)
# print(len(chunks))
# print(chunks)

# print(f"Data: {chunks[0].page_content}")
# print(f"Metadata: {chunks[0].metadata}")
# print("=======================================")
# print(f"Data: {chunks[1].page_content}")
# print(f"Metadata: {chunks[1].metadata}")
# print("=======================================")
# print(f"Data: {chunks[2].page_content}")
# print(f"Metadata: {chunks[2].metadata}")

# for i, chunk in enumerate(chunks):
#     print(f"Chunk {i + 1}: ")
#     print(f"Data: {chunk.page_content}")
#     print(f"length: {len(chunk.page_content)}")
#     print("=======================================")

############################################################################
# Embedding
############################################################################

# from google import genai

# client = genai.Client()

# text = "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints."

# result = client.models.embed_content(
#     model=EMBEDDING_MODEL,
#     contents=text
# )

# embeding = result.embeddings[0].values

# print(embeding)
# print(len(embeding))
# print(type(embeding))


# from google import genai
# from langchain_community.document_loaders import UnstructuredMarkdownLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# client = genai.Client()

# loader = UnstructuredMarkdownLoader("lesson55/data/company_info.md")

# docs = loader.load()

# splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=40)

# chunks = splitter.split_documents(docs)

# texts = [chunk.page_content for chunk in chunks]

# result = client.models.embed_content(
#     model=EMBEDDING_MODEL,
#     contents=texts
# )

# embedding = [item.values for item in result.embeddings]

# print(embedding)
# print(len(embedding))

############################################################################
# Semantic Search
############################################################################

from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from google import genai
from sklearn.metrics.pairwise import cosine_similarity

client = genai.Client()

loader = UnstructuredMarkdownLoader("lesson55/data/company_info.md")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=40)

chunks = splitter.split_documents(docs)

texts = [chunk.page_content for chunk in chunks]

result = client.models.embed_content(
    model=EMBEDDING_MODEL,
    contents=texts
)

embedding = [item.values for item in result.embeddings]

question = "რა პროექტს გვთავაზობს კომპანია"

query_result = client.models.embed_content(
    model=EMBEDDING_MODEL,
    contents=question
)

embedding_query = query_result.embeddings[0].values

similarity_scores = cosine_similarity([embedding_query], embedding)[0]

# print(similarity_scores)

results = sorted(zip(chunks, similarity_scores), key=lambda x: x[1], reverse=True)

for i, (chunk, score) in enumerate(results):
    print(f"Chunk {i + 1}:")
    print(f"Score: {score}")
    print(f"Data: {chunk.page_content}")
    print("=======================================")


