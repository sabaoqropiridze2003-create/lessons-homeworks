# პირველი ამოცანა

# number = int(input("Please enter a whole number to calculate factorial: "))
# factorial = 1

# for i in range(1, number + 1):
#     factorial *= i

# print(f"result is: {factorial}")


# მეორე ამოცანა

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i * j}")


# მესამე ამოცანა

# payment = 50

# print(f"""           თქვენი დავალიანებაა {payment} ლარი.
#     აპარატი იღებს მხოლოდ 5, 10 და 20 ლარიან კუპიურებს.""")

# while payment > 0:

#     try:
#         user_input = int(input("გთხოვთ მოათავსოთ კუპიურა: "))
#     except ValueError:
#         print("შეიყვანეთ მხოლოდ ციფრები!!")
#         continue

#     if user_input != 5 and user_input != 10 and user_input != 20:
#         print("გთხოვთ შეიტანეთ ვალიდური კუპიურა!!")
#         continue

#     else:
#         payment -= user_input

#         if payment > 0:
#             print(f"გადასახდელი დარჩა {payment} ლარი.")
#         else:
#             change = abs(payment)
#             print(f"თქვენ გეკუთვლით ხურდა {change} ლარი")

# else:
#     print("მადლობა ჩვენი ბანკომატით სარგებლობისათვის!!")
