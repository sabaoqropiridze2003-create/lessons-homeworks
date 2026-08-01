# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# new_list = [str(num) for num in lst]

# text = ', '.join(new_list)

# with open("lesson20/numbers.txt", "w") as f:
#     f.writelines(text)


# with open("lesson20/numbers.txt", "r") as f:
#     data = f.read()

# new_list = data.split(', ')

# deserialized_list = [int(num) for num in new_list]
# print(deserialized_list)


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"student({self.name}, {self.age})"


# s1 = Student("Alice", 20)


# def student_serializer(student):
#     if isinstance(student, Student):
#         return {
#             "name": student.name,
#             "age": student.age
#         }
#     return "Not a Student instance"


# serialized_data = student_serializer(s1)


# print(student_serializer(s1))


# def student_deserializer(data):
#     if isinstance(data, dict):
#         return Student(data["name"], data["age"])
#     return "Not a valid Student data format"


# print(student_deserializer(serialized_data))


import json
# student = {
#     "name": "Alice",
#     "age": 20,
#     "grades": [90, 85, 92],
#     "address": {
#         "city": "New York",
#         "street": "123 Main St",
#     },
#     "is_active": True,
#     "float": 3.14,
#     "tuple": (1, 2, 3),
#     "none": None
# }

# serialized_student = json.dumps(student, indent=4)

# print(serialized_student)

# deserialized_student = json.loads(serialized_student)
# print(type(deserialized_student))

# from datetime import datetime

# student1 = {
#     "name": "Alice",
#     "age": 20,
#     "grades": [90, 85, 92],
#     "address": {
#         "city": "New York",
#         "street": "123 Main St",
#     },
#     "is_active": True,
#     "float": 3.14,
#     "tuple": (1, 2, 3),
#     "none": None
# }

# student2 = {
#     "name": "Bob",
#     "age": 22,
#     "grades": [88, 79, 95],
#     "address": {
#         "city": "Los Angeles",
#         "street": "456 Elm St",
#     },
#     "is_active": False,
#     "float": 2.71,
#     "tuple": (4, 5, 6),
#     "none": None
# }

# students = [student1, student2]

# students_data = {
#     "count": len(students),
#     "created_at": str(datetime.now()),
#     "students": students,
# }

# with open("lesson20/student.json", "w") as f:
#     json.dump(students_data, f, indent=4)


# with open("lesson20/student.json", "r") as f:
#     data = json.load(f)

# print(data)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"student({self.name}, {self.age})"


# s1 = Student("Alice", 20)


# def student_serializer(student):
#     if isinstance(student, Student):
#         return {
#             "name": student.name,
#             "age": student.age
#         }
#     return "Not a Student instance"


# with open("lesson20/student1.json", "w") as f:
#     json.dump(s1, f, default=student_serializer, indent=4)

# def student_deserializer(data):
#     if isinstance(data, dict):
#         return Student(data["name"], data["age"])
#     return "Not a valid Student data format"


# with open("lesson20/student1.json", "r") as f:
#     student = json.load(f, object_hook=student_deserializer)


# print(student)

import pickle


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"student({self.name}, {self.age})"


# s1 = Student("Alice", 20)

# serialized_student = pickle.dumps(s1)
# print(serialized_student)
# deserialized_student = pickle.loads(serialized_student)
# print(deserialized_student)


# with open("lesson20/student2.pkl", "wb") as f:
#     pickle.dump(s1, f)


# with open("lesson20/student2.pkl", "rb") as f:
#     student = pickle.load(f)

# print(student)


student1 = {
    "name": "Alice",
    "age": 20,
    "grades": [90, 85, 92],
    "address": {
        "city": "New York",
        "street": "123 Main St",
    },
    "is_active": True,
    "float": 3.14,
    "tuple": (1, 2, 3),
    "none": None
}

with open("lesson20/student2.pkl", "wb") as f:
    pickle.dump(student1, f)

with open("lesson20/student2.pkl", "rb") as f:
    student = pickle.load(f)
print(student)
