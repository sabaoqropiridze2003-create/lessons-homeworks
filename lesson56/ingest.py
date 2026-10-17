from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from google import genai
from models import DocumentChunk
from sqlalchemy.orm import Session
from database import engine

from dotenv import load_dotenv
load_dotenv()

EMBEDDING_MODEL = "gemini-embedding-001"

client = genai.Client()

loader = UnstructuredMarkdownLoader("lesson56/data/company_info.md")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=30)

chunks = splitter.split_documents(docs)

texts = [chunk.page_content for chunk in chunks]

result = client.models.embed_content(
    model=EMBEDDING_MODEL,
    contents=texts
)

embeddings = [item.values for item in result.embeddings]

# print(len(embeddings))

with Session(engine) as session:

    for chunk, embedding in zip(chunks, embeddings):

        document_chunk = DocumentChunk(
            content=chunk.page_content,
            chunk_metadata=chunk.metadata,
            embedding=embedding
        )

        session.add(document_chunk)

    session.commit()

