# my_lst = [5, 2, 6, 7, 4]
# result = 0

# for i in my_lst:
#     result += i

# print(result)
# for i in range(1, 6):
#     print(i)
# from random import randint
# nums = [randint(-50, 50) for _ in range(20)]
# even_numbers = [num for num in nums if num % 2 == 0]

# print(nums)
# print(even_numbers)


# persons = [
#     ('Kelly', 'Simpson', 26),
#     ('Erika', 'Stephens', 24),
#     ('Cheryl', 'Dunn', 30),
#     ('Amy', 'Larsen', 49),
#     ('Christine', 'Gordon', 23),
#     ('Monica', 'Huff', 38),
#     ('David', 'Nixon', 36),
#     ('Cindy', 'Escobar', 41),
#     ('Cindy', 'White', 33),
#     ('Joel', 'Hall', 43),
#     ('Steven', 'Winters', 28),
#     ('Alex', 'Cole', 68),
#     ('Alex', 'Smith', 32),
#     ('Alex', 'White', 42),
#     ('Brittany', 'Thompson', 18),
#     ('Ernest', 'Young', 43),
#     ('Traci', 'Wells', 38),
#     ('Andrew', 'Flores', 61),
#     ('Christopher', 'Lewis', 29),
#     ('Kevin', 'Willis', 57),
#     ('Kayla', 'Lucas', 28),
#     ('Michelle', 'Rush', 43),
#     ('Thomas', 'Mason', 37)
# ]

# while True:
#     first_name = input("enter your first name: ")

#     if first_name == "stop":
#         break

#     found_list = []

#     for person in persons:
#         if first_name == person[0]:
#             found_list.append(person)

#     if found_list:
#         last_name = input("enter your lastname")


# set1 = {2, 4, 8, 4, 7}

# print(type(set1))
# print(set1)


# set1 = {"otar"}
# print(type(set1))

# set2 = set()
# print(type(set2))

# set1 = {2, True, "otar", 2.5, None, (1, 2, 3)}
# print(set1)

# set1 = {2, True, "otar", 2.5, None, (1, 2, 3), {"key": "value"}}
# print(set1)


# names = {"otar", "saba", "davit", "nino", "gio", "ana"}
# print(len(names))
# print(names)

# nums = {2, 4, 1, 7, 9, -100, 187}

# for name in names:
#     print(name)
# print(nums)

# სეტები შედარებით უდრო ჩქარია შესაბამისად დიდ მონაცემებთან მუშაობის დროს უმჯობესია სეტეპის გამოყენება

# names = ["otar", "saba", "davit", "nino", "gio", "ana"]
# names_set = set(names)

# name = input("enter your name")

# if name in names_set:
#     print("hello", name)
# else:
#     print("this name does not exist")

# num1 = int(input("enter a number1: "))
# num2 = int(input("enter a number2: "))

# print(num1 + num2)


# print("something code executed......")

# num1 = int(input("enter a number1: "))
# num2 = int(input("enter a number2: "))

# print(num1 + num2)

# print("another code executed......")


# def add():
#     num1 = int(input("enter a number1: "))
#     num2 = int(input("enter a number2: "))

#     print(num1 + num2)


# print("something code executed......")

# print("another code executed......")

# add()


# def greet(name):
#     print(f"Hello, {name}")


# greet("otar")
# greet("saba")
# greet("naan")

# def greet(name, age):
#     print(f"Hello, {name}! you are {age} years old")


# greet("otar", 25)


# print()
# print("hello")
# print("world", "something")

# greet(35, "otar")


# def greet(first_name, last_name, age):
#     print(f"Hello, {first_name} {last_name} you are {age} years old")


# greet("otar", "tumanishvili", 25)
# greet(last_name="okropiridze", first_name="saba", age=35)

# def greet(first_name, last_name, age):
#     print(f"Hello, {first_name} {last_name} you are {age} years old")


# greet("otar", last_name="tumanishvili", age=35)

# greet("tumanishvili", first_name="otar", age=35)


def greet(first_name, last_name, age):
    print(f"Hello, {first_name} {last_name} you are {age} years old")


greet("otar", age=35, last_name="tumanishvili")

# greet(age=35, "otar", last_name="tumanishvili")


# def add(num1, num2):
#     return num1 + num2


# add(7, 8)
# print(add(7, 8))

# result = add(4, 8)

# a = result + add(5, 10)
# print(result)
# print(a)

# first_name = input("enter your first name: ")
# print(first_name)


#


# print("fadsfdfs")


# print(add)


# def test():
#     return "Hello", 8, 87, 54, 65


# a, b, *c = test()
# print(a)
# print(b)
# print(c)
