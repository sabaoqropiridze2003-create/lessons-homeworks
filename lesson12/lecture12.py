# def outer():
#     def inner():
#         return "I am inner"

#     return inner()


# print(outer())

# x = 8  # Global Variable


# def outer():
#     x = 10 #enclosing variable

#     def inner():
#         x = 5
#         return x # Local variable
#     return(inner())


# print(outer())


# __name__ = "global"


# def outer():
#     __name__ = 10  # enclosing variable

#     def inner():
#         __name__ = 5
#         return __name__  # Local variable
#     return (inner())


# print(outer())

# x = 15


# def outer():
#     x = 10  # enclosing variable

#     def inner():
#         # global x
#         nonlocal x
#         x += 5
#         return x  # Local variable
#     return inner()


# print(outer())


# def outer():

#     def inner(x):
#         return "i am inner"
#     return inner


# # print(outer()())
# i = outer()
# # print(callable(i))
# print(i(4))


# def get_multiplier(a):

#     def inner(b):
#         return a * b
#     return inner


# x = get_multiplier(8)
# print(x(9))


# double = get_multiplier(2)
# multipier_by_five = get_multiplier(5)

# print(double(2))
# print(double(3))
# print(double(4))
# print(double(5))

# print(multipier_by_five(4))


# def my_decorator(func):
#     def wrapper():
#         print("i am before the function")
#         func()
#         print("i am after the function")
#     return wrapper


# @my_decorator
# def add():
#     print("i am add function")

# def add():
#     print("i am add function")


# results = my_decorator(add)
# results()

# my_decorator(add)()

# @my_decorator
# def test():
#     print("i am a test function")


# add()

# test()


# def change_value(func):
#     def wrapper(x, y):
#         x += 2
#         y += 2
#         return func(x, y)
#     return wrapper


# def test(a, b):
#     print(f"a = {a} b = {b}")

# @change_value
# def test(a, b):
#     print(f"a = {a} b = {b}")


# test(5, 8)


# import time


# def test():
#     start_time = time.time()
#     print("i started working")
#     time.sleep(4)
#     input("please enter tu continue")
#     print("i have finished")
#     end_time = time.time()
#     print(f"Time taken: {end_time - start_time: .2f} seconds")


# test()


