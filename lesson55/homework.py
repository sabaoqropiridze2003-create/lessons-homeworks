from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from google import genai
from sklearn.metrics.pairwise import cosine_similarity

EMBEDDING_MODEL = "gemini-embedding-001"
client = genai.Client()

loader = UnstructuredMarkdownLoader("lesson55/data/hotel_info.md")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=40)

chunks = splitter.split_documents(docs)

texts = [chunk.page_content for chunk in chunks]

result = client.models.embed_content(
    model=EMBEDDING_MODEL,
    contents=texts
)

embeddings = [item.values for item in result.embeddings]

question = input("შეიყვანე კითხვა: ")

query_result = client.models.embed_content(
    model=EMBEDDING_MODEL,
    contents=question
)

embedding_query = query_result.embeddings[0].values

similarity_score = cosine_similarity([embedding_query], embeddings)[0]

results = sorted(zip(chunks, similarity_score), key=lambda x: x[1], reverse=True)[:3]

print("####ტოპ 3 შედეგი####")
for i, (chunk, score) in enumerate(results):
    print(f"top {i + 1}")
    print(f"score: {score}")
    print(f"data: {chunk.page_content}")
    print("=" * 100)



