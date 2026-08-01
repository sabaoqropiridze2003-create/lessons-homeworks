# empty_dict = {}
# empty_dict = dict()


# print(empty_dict)
# print(type(empty_dict))


# names = ["saba", "gio", "lasha"]
# ages = [25, 30, 40]

# for i in range(len(names)):
#     print(f"{names[i]} is {ages[i]} years old")


# names = {"john": 25,
#          "jane": 30,
#          "bob": 40,
#          "alice": 52
# }


# my_dict = {
#     "str": "this is a string",
#     1: "this is am integer",
#     3.15: "this is a float",
#     True: "this is a boolean",
#     None: "this is none",
#     (1, 2, 3): "this is a tuple"
# }

# print(my_dict)

# names = {"john": 25,
#          "jane": 30,
#          "bob": 40,
#          "alice": 52,
#          "john": 45
#          }

# print(names)

# my_dict = {
#     "str": "this is a string",
#     1: "this is am integer",
#     3.15: "this is a float",
#     True: "this is a boolean",
#     None: "this is none",
#     (1, 2, 3): "this is a tuple",
#     "list": [1,2,3,4],
#     "dict": {"key", "value"}
# }


# names = {"john": 25,
#          "jane": 30,
#          "bob": 40,
#          "alice": 52,
#          "john": 45,
#          "ana": 29,
#          "davit": 45
#          }

# print(names["davit"])
# print(names["alice"])
# print(names["ana"])
# print(names["bob"])

# names["otar"] = 35
# names["ana"] = 50

# print(names["ana"])

# names = {"john": 25,
#          "jane": 30,
#          "bob": 40,
#          "alice": 52,
#          "John": 45,
#          "ana": 29,
#          "davit": 45,
#          }

# print(names.get("john"))

# print(len(names))

# for name in names:
#     print(names[name])

# for key in names:
#     print(f"{key} is {names[key]} yers old")


# names = {"john": 25,
#          "jane": 30,
#          "bob": 40,
#          "alice": 52,
#          "John": 45,
#          "ana": 29,
#          "davit": 45,
#          }


# print(names.get("otar"))
# print(names.get("otar", "not found"))

# print(list(names.keys()))
# print(list(names.values()))
# print(list(names.items()))

# for key, value in names.items():
#     print(f"{key} is {value} yers old")


# names = {"john": 25,
#          "jane": 30,
#          "bob": 40,
#          "alice": 52,
#          "John": 45,
#          "ana": 29,
#          "davit": 45,
#          }

# names.update({"otar": 35, "lasha": 56})
# print(names)
# poped = names.pop("ana")

# poped = names.popitem()

# print(poped)
# print(names)


# names = ["otar", "saba", "giorgi"]
# new_dict = dict.fromkeys(names, 5)
# print(new_dict)

# print(new_dict.setdefault("sabaaa", 40))
# print(new_dict)

# ქომფრეჰენშენები
# my_dict = {i: "Hello" for i in range(10) if i % 2 == 0}
# print(my_dict)

# products = {
#     "electronics": {
#         "laptops": {"rame": "rume", "price": 200},
#         "laptopa": {"rame": "rume", "price": 200},
#         "laptopb": {"rame": "rume", "price": 200},
#     },
# }

# print(products["electronics"]["laptops"]["price"])
