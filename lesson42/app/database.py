from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_session
from sqlalchemy.ext.asyncio import AsyncSession

DATABASE_URL = "postgresql+psycopg2://postgres:paroli@localhost:5432/PP-39"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass

ASYNC_DATABASE_URL = "postgresql+asyncpg://postgres:paroli@localhost:5432/PP-39"

async_engine = create_async_engine(ASYNC_DATABASE_URL)

AsyncSessionLocal = async_sessionmaker(bind=async_engine)

async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session

class AsyncBase(DeclarativeBase):
    pass

