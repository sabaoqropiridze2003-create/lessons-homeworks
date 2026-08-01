# def get_factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * get_factorial(n - 1)  # 5 * 4 * 3 * 2 * get_factorial(2 - 1)


# print(get_factorial(5))

# def add(a=8):
#     return a


# print(add())

# import string
# word = "hello. rame! rame?"
# # print(word.replace(".", ""))

# print(word.strip(",?!."))


# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
# print(word.strip(string.punctuation))


###########################################################################################
# age: int = 35
# name: str = "otar"
# active: bool = True
# height: float = 10.5
# dcores: list[int] = [10, 20, 30, 40, 50]

# my_tuple: tuple[int,str,float] = (1, "otar", 35.5)

# mytuple = (1, "otar", 3.5, [1, 2])

# mytuple[-1][1] = 3
# print(mytuple)

# student: dict[str, int] = {"name": "saba", "age": 35}
# my_set: set[int] = {1,2,3,4,5,6}

# def add(a: int, b: int):
#     return a + b


# print(add("1", 2))


# def test(a: str, b: str) -> str:
#     return f"{a.upper()} {b.upper()}"


# print(test("hello", "world"))


# from typing import Optional

# ძველი სინტაქსი

# email: Optional[str] = None

# ახალი სინტაქსი

# email: str | None = None


# from typing import Any
# def trest(a: Any):
#     print(a)


# from faker import Faker

# fake = Faker()

# print(fake.first_name())
# print(fake.last_name())
# print(fake.email())
# print(fake.address())
