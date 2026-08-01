# ამოცანა პირველი

# dict1 = {i: i**2 for i in range(1, 11)}
# print(dict1)

# მეორე ამოცანა

# products = [
#     {"cola": {
#         "price": 1.5,
#         "quantity": 10
#     }},
#     {"fanta": {
#         "price": 2.5,
#         "quantity": 5
#     }},
#     {"snickers": {
#         "price": 3.5,
#         "quantity": 12
#     }},
#     {"water": {
#         "price": 4.5,
#         "quantity": 8
#     }},
#     {"beer": {
#         "price": 6.5,
#         "quantity": 5
#     }}
# ]

# for item in products:
#     for name in item:
#         print(f"product name: {name}")


# total_value = 0
# for item in products:
#     for i in item.values():
#         x = i["price"] * i["quantity"]
#         total_value += x
# print(f"Total value is {total_value} dollars!!")


# მესამე ამოცანა

# fruits = {}

# while True:
#     user_input = input("Enter the name of the fruit: ").strip()

#     if user_input.lower() == "stop":
#         print("end of program")
#         break

#     if user_input in fruits:
#         fruits[user_input] += 1
#     else:
#         fruits[user_input] = 1

# print(fruits)
