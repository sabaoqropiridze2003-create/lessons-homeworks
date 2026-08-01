# file = open("test.txt", "r")
# data = file.read()
# file.close()
# print(data)

# data1 = file.read()
# print(data1)

# file = open("inner/inner.txt", "r")

# data = file.read()

# file.close()

# print(data)

# try:
#     file = open("../inner.txt", "r")
#     data = file.read()
#     file.close()
# except FileNotFoundError:
#     data = "file not found"

# print(data)


# f = open("test.txt", "rt")

# data = f.read()

# f.close()
# print(data)
# print(type(data))

# f = open("test.txt", "rt")

# print(f.readable())
# print(f.writable())

# f.close()

# f = open("test.txt", "rt")

# data = f.read(18)

# f.close()

# print(data)


# f = open("test.txt")

# data = f.read()
# data1 = f.read()

# f.close()

# print(data)
# print(data1)


# f = open("test.txt")

# data = f.read()

# f.seek(0)

# data1 = f.read()

# f.close()

# print(data)
# print(data1)


# f = open("test.txt")

# line1 = f.readline().strip("\n")
# line2 = f.readline().strip("\n")
# line3 = f.readline().strip("\n")
# line4 = f.readline().strip("\n")

# f.close()

# print(line1)
# print(line2)
# print(line3)
# print(line4)

# f = open("test.txt")

# lines = f.readlines()

# new_lines = [i.strip("\n") for i in lines]

# f.close()
# print(lines)
# print(new_lines)

# f = open("test1.txt", "w")

# print(f.readable())
# print(f.writable())

# f.close()

# f = open("test.txt", "w+")

# print(f.readable())
# print(f.writable())

# f.close()

# f = open("test.txt", "x")

# f.close()


# f = open("test1.txt", "w")
# f.write("Hello World")
# f.write("\n")
# f.write("Hello Python")

# f.close()

# f = open("test1.txt", "a")

# f.write("\n25")

# f.close()


# with open("test1.txt", "a") as f:
#     f.write("\n30")
#     f.write("\n20")


# names = ["saba", "gio", "salome", "ani", "eka"]

# with open("test1.txt", "a") as f:
#     for name in names:
#         f.write(f"{name}\n")


# names = ["Otar", "Ana", "John", "Davit", "Nino"]

# new_names = [f"{name}\n" for name in names]

# with open("test1.txt", "a")as f:
#     f.writelines(new_names)


# name = "Otar"

# binary_name = name.encode("utf-8")

# # print(binary_name)


# # with open("name.bin", "wb") as f:
# #     f.write(binary_name)

# with open("name.bin", "rb") as f:
#     data = f.read()

# name = data.decode("utf-8")
# print(name)


# import csv

# with open("companies.csv", "r") as f:
#     reader = csv.reader(f)

#     for row in reader:
#         print(row)

# with open("companies.csv", "r") as f:
#     dict_reader = csv.DictReader(f)

#     for row in dict_reader:
#         print(row)


# person = {
#     "name": "Otar",
#     "age": 25,
#     "city": "Istanbul",
#     "country": "Turkey"
# }


# headers = ["name", "age", "city", "country"]
# headers = person.keys()


# with open("person.csv", "w") as f:
#     writer = csv.DictWriter(f, fieldnames=headers)
#     writer.writeheader()
#     writer.writerow(person)

# import csv
# from faker import Faker

# fake = Faker()

# person = [{"first_name": fake.first_name(), "last_name": fake.last_name(),
#            "company": fake.company()} for _ in range(50)]

# headers = person[0].keys()

# with open('lesson14/person.csv', 'w') as file:
#     dict_writer = csv.DictWriter(file, fieldnames=headers)
#     dict_writer.writeheader()
#     dict_writer.writerows(person)


# with open("test.txt", "w") as f:
#     data = f.write("rame")
