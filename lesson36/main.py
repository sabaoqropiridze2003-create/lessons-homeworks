from models import Student, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, and_, or_

SesionLocal = sessionmaker(bind=engine)
session = SesionLocal()

# new_student = Student(name = "nino", age = 23, grade = 93.5)

# session.add(new_student)
# session.commit()
# print(f"ID: {new_student.id}")


# students = [
#     Student(name="lasha", age=20, grade= 90),
#     Student(name="ani", age=24, grade= 93),
#     Student(name="giorgi", age=22, grade= 92),
#     Student(name="lazare", age=23, grade= 75),
#     Student(name="dato", age=21, grade= 85)
# ]

# session.add_all(students)
# session.commit()

# stmt = select(Student)
# students = session.scalars(stmt).all()

# for s in students:
#     print(s)

# stmt = select(Student).where(Student.age >22)
# students = session.scalars(stmt).first()
# print(students)

# stmt = select(Student).where(and_(Student.age >21,Student.grade >90))
# students = session.scalars(stmt).all()
# for s in students:
#     print(s)

# stmt = select(Student).where(or_(Student.age >21,Student.grade >90))
# students = session.scalars(stmt).all()
# for s in students:
#     print(s)

# stmt = select(Student).order_by(Student.grade.desc())
# students = session.scalars(stmt).all()
# for s in students:
#     print(s)

# student = session.get(Student, 1)
# print(student)

# student = session.get(Student,3)
# print(f"old grade: {student.grade}")
# student.grade = 100
# print(f"new grade: {student.grade}")
# session.commit()

# student = session.get(Student,6)
# session.delete(student)
# session.commit()

student = session.get(Student, 1)
print(f"old greade: {student.grade}")
student.grade = 40
print(f"new greade: {student.grade}")
session.rollback()
print(f"greade after rollback {student.grade}")

session.close()