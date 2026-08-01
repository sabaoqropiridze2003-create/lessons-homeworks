import json

# პიეველი დავალება

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Person: ({self.name}, {self.age})"


# p1 = Person("Otar", 35)


# def student_serializer(student):
#     if isinstance(student, Person):
#         return {"Name": student.name, "Age": student.age
#                 }
#     return "Not a Person instance"


# with open("lesson20/persons.txt", "w") as file:
#     json.dump(p1, file, default=student_serializer)


# def student_deserializer(data):
#     if isinstance(data, dict):
#         return Person(data["Name"], data["Age"])
#     return "not a valid data format"


# with open("lesson20/persons.txt", "r") as file:
#     student = json.load(file, object_hook=student_deserializer)

# print(student)


# მეორე დავალება

def add_multiple_persons(count):

    with open("lesson20/persons.json", "r") as file:
        persons = json.load(file)

    if persons:
        next_id = persons[-1]["id"] + 1
    else:
        next_id = 1

    for _ in range(count):
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        new_person = {
            "id": next_id,
            "name": name,
            "age": age
        }

        persons.append(new_person)
        next_id += 1

    with open("lesson20/persons.json", "w") as file:
        json.dump(persons, file, indent=4)

    print(f"Successfully added {count} new records!")


add_multiple_persons(2)
