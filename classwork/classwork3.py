from faker import Faker
from typing import Any

fake = Faker()


def generate_student(number: int) -> dict:
    student: dict = {
        "ID": number,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "age": fake.random_int(min=18, max=80)
    }
    return student


def generate_students(count: int) -> list:
    students_lst = []
    for i in range(1, count + 1):
        student = generate_student(i)
        students_lst.append(student)

    return students_lst


my_students = generate_students(3)
print(my_students)
