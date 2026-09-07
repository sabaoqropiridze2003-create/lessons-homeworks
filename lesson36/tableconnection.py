from sqlalchemy import create_engine, String, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, DeclarativeBase, Session, mapped_column, relationship, sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/lesson36', echo=True)

class Base(DeclarativeBase):
    pass

class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    subject: Mapped[str] = mapped_column(String(50), nullable=False)

    students = relationship("Student", back_populates="teacher")

    def __repr__(self):
        return f"Teacher(id={self.id}, name={self.name}, age={self.age}, subject={self.subject})"

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    grade: Mapped[float] = mapped_column(Float, nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))

    teacher = relationship("Teacher", back_populates="students")

    def __repr__(self):
        return f"Student(id={self.id}, name={self.name}, age={self.age}, grade={self.grade}, teacher_id={self.teacher_id})"

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
teacher = Teacher(name="Mr. Smith", age=40, subject="Math")
session.add(teacher)
session.commit()

student1 = Student(name="Alice", age=15, grade=90.5, teacher_id=teacher.id)
student2 = Student(name="Bob", age=16, grade=85.0, teacher_id=teacher.id)

session.add_all([student1, student2])
session.commit()

print(f"Teacher: {teacher.name}")
for s in teacher.students:
    print(f"Student: {s.name}, Age: {s.age}, Grade: {s.grade}")

print(f"Student: {student1.name}, Teacher: {student1.teacher.name}")

session.close()