try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise Exception("Age must be positive!")


except ValueError:
    print("Enter only integer!")

except Exception as e:
    print(f"Error: {e}")

else:
    if age < 18:
        print("You are not an adult")
    else:
        print("You ar an adult")
