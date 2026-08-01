# ამოცანა პირველი

# weight = input("Enter your weight in kilograms: ")
# height = input("Enter your height in meters: ")
# bmi = float(weight) / (float(height) ** 2)

# if bmi < 19:
#     print("You are underweight, your bmi is", round(bmi, 2))
# elif bmi <= 25:
#     print("You are normal weight, your bmi is", round(bmi, 2))
# else:
#     print("You are overweight, your bmi is", round(bmi, 2))

# ამოცანა მეორე


# f_number = float(input("Enter a number: "))
# s_number = float(input("Enter second number: "))
# operator = input("Enter an operator (+, -, *, /): ")
# result = "You enterd an invalid opperator!"

# if operator == "+":
#     result = f_number + s_number
#     print(f"The result is", result)
# elif operator == "-":
#     result = f_number - s_number
#     print(f"The result is", result)
# elif operator == "*":
#     result = f_number * s_number
#     print("The result is", result)
# elif operator == "/":
#     if s_number != 0:
#         result = f_number / s_number
#         print("The result is", result)
#     else:
#         print("Division by zero is not allowed!!!")
# else:
#     print(result)


# ამოცანა მესამე

# print("Enter 3 different numbers to find the largest one.")
# fnumber = float(input("Enter a number: "))
# snumber = float(input("Enter second number: "))
# tnumber = float(input("Enter third number: "))
# if fnumber == snumber or fnumber == tnumber or snumber == tnumber:
#     print("Enter different numbers")
# elif fnumber > snumber and fnumber > tnumber:
#     print("The largest number is", fnumber)
# elif snumber > fnumber and snumber > tnumber:
#     print("The largest number is", snumber)
# else:
#     print("The largest number is", tnumber)


# წინა დავალების მესამე ამოცანა

# word_one = input("enter first word: ").lower()
# word_two = input("enter second word: ").lower()
# if sorted(word_one) == sorted(word_two):
#     print("The words are anagrams")
# else:
#     print("The words are not anagrams")
