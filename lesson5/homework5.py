try:
    number1 = float(input("Enter number1: "))
    number2 = float(input("Enter number2: "))

    result = number1 / number2
except ValueError:
    print("Enter only numbers!!")
except ZeroDivisionError:
    print("You can't divide by zero!!")
except Exception as e:
    print(f"An arror occured {e}")
else:
    print(f"The result of number1 devided by number2 is: {result}")
finally:
    print("End of program")
