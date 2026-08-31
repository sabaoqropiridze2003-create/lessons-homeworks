from sqlalchemy import create_engine, String, Integer, Boolean
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column

engine = create_engine(
    'postgresql+psycopg2://postgres:paroli@localhost:5432/school_db')


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = 'student'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    grade: Mapped[float] = mapped_column(nullable=True)

    def __repr__(self):
        return f"Student id = {self.id} name = {self.name} age = {self.age} grade = {self.grade}"


class Teacher(Base):
    __tablename__ = 'teacher'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    subject: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(
        String(200), unique=True, nullable=False)
    is_active: Mapped[mapped_column] = mapped_column(Boolean, default=True)

    def __repr__(self):
        return f"Teacher(id={self.id}, name={self.name}, subject={self.subject})"


Base.metadata.create_all(engine)
