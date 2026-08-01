# def main(a=5, b=6):
#     return a + b


# print(main(10, 15))

# def main(a, b, *args, name):

#     return sum(args)/len(args)


# print(main(1, 2, 3, 4, 5, 100, 67, name="raime"))


# def main(greeting, *args):

#     for i in args:
#         print(f"{greeting} {i}")


# main("hello", "nino", "mariami", "giorgi")

# def main(**kwargs):
#     return kwargs


# print(type(main()))
# print(main(name="nini", city="tbilisi", phone=555443322))


# def main(**kwargs):
#     if "city" in kwargs:
#         print("aseti parametri moidzebna")


# main(name="nini", city="tbilisi", phone=555443322)

# def main(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# print(main(name="nini", city="tbilisi", phone=555443322))

# def main(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# print(main(name="nini", city="tbilisi", phone=555443322))

# def main(a, b, *args, z):
#     print(f"a:{a}, b:{b}, args: {args}, z:{z}")


# main(1, 2, 3, 4, 5, z=4)
# main(1, 2, 3, 4, 5, z=4)

# def factorial(n):
#     return n * factorial(n)


# factorial(5)

# def factorial(n):
#     if n == 0:
#         return 1
#     print(n)
#     return n * factorial(n-1)


# print(factorial(5))
# print(factorial(9))

# def countdown(n):
#     if n <= 0:
#         print("end")
#     else:
#         print(n)
#         countdown(n-1)


# countdown(5)

# square = lambda x : x**2

# print(square(5))

# mimateba = lambda x, y : x + y
# print(mimateba(5,6))

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# def square(x):
#     return x ** 2


# z = map(square, lst)
# print(z)
# print(list(z))

# z = map(lambda x: x**2, lst)

# print(list(z))

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# name = ["giorgi", "vano", "nini", "elene", "ia", "gela"]

# z = map(lambda x: x.upper(), name)
# z = map(lambda x: x.capitalize(), name)
# print(list(z))

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 25, 15]

# y = filter(lambda x: x % 2 == 0, lst)
# y = filter(lambda x: x > 4, lst)

# print(list(y))

# from functools import reduce
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# x = reduce(lambda a, b: a + b, lst)
# x = reduce(lambda a, b: a if a > b else b, lst)
# print(x)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# name = ["giorgi", "vano", "nini", "elene", "ia", "gela"]

# pairs = zip(lst, name)
# print(list(pairs))

# for x, y in zip(name, lst):
#     print(f"first{x} :: second{y}")

# lst = [1, 15, 2, 3, 4, 4, 5, 6, 7, 8, 19, 9]
# name = ["giorgi", "vano", "nini", "elene", "ia", "gela"]

# print(sorted(lst, reverse=True))
# print(sorted(name, key=lambda x: len(x)))

# def sum():


# def add(a, b):
#     return a + b


# def sub(a, b):
#     return a - b


# def mul(a, b):
#     return a * b


# def div(a, b):
#     return a / b


# def test(func, y, z):
#     if callable(func):
#         return func(y, z)
#     return "Not callable"


# print(test("add", 2, 3))
# print(test(sub, 2, 3))
# print(test(mul, 2, 3))
# print(test(div, 2, 3))

# def register_user(**kwargs):
#     if "email" in kwargs:
#         print(f"ელფოსტა: {kwargs['email']}")
#     else:
#         print("ელფოსტა არარის მითითებული!")
#     if "phone" in kwargs:
#         print(f" {kwargs['phone']}")
#     else:
#         print("ტელეფონი არაა მითითებული")

# register_user(email="nino@mail.com", phone="555123456")
# register_user(email="gio@mail.com")
# register_user(phone="555999888")
