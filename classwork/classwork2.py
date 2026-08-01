from random import randrange


number = randrange(1, 100)
attempts = 5

while attempts > 0:
    user_input = int(input("Pleas enter a number: "))
    if user_input == number:
        print("You won!!")
        break
    elif user_input > number:
        print("try lower number!!")
        attempts -= 1
    elif user_input < number:
        print("Try higher number")
        attempts -= 1
else:
    print("Unfortunately you lost")
