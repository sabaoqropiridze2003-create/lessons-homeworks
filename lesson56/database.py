from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:paroli@localhost:5432/rag_system"

engine = create_engine(DATABASE_URL)