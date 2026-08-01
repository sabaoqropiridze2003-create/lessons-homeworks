# პირველი ამოცანა

# lst = [1, 2, 3, 4, 5, 6, 7]
# count = 0

# for i in lst:
#     count += i
# mean = count / len(lst)
# print(f"sum of numbers is {count}")
# print(f"arithmetic mean is {mean}")

# მეორე ამოცანა

# lst = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]

# for i in lst[:]:
#     if lst.count(i) != 1:
#         lst.remove(i)
# print(lst)

# მესამე ამოცანა

# from random import randint

# lst1 = [randint(-50, 50) for i in range(20)]
# lst2 = [x for x in lst1[:] if x % 2 == 0]
# print(lst1)
# print(lst2)

# მეოთხე ამოცანა

persons = [
    ('Kelly', 'Simpson', 26),
    ('Erika', 'Stephens', 24),
    ('Cheryl', 'Dunn', 30),
    ('Amy', 'Larsen', 49),
    ('Christine', 'Gordon', 23),
    ('Monica', 'Huff', 38),
    ('David', 'Nixon', 36),
    ('Cindy', 'Escobar', 41),
    ('Cindy', 'White', 33),
    ('Joel', 'Hall', 43),
    ('Steven', 'Winters', 28),
    ('Alex', 'Cole', 68),
    ('Alex', 'Smith', 32),
    ('Alex', 'White', 42),
    ('Brittany', 'Thompson', 18),
    ('Ernest', 'Young', 43),
    ('Traci', 'Wells', 38),
    ('Andrew', 'Flores', 61),
    ('Christopher', 'Lewis', 29),
    ('Kevin', 'Willis', 57),
    ('Kayla', 'Lucas', 28),
    ('Michelle', 'Rush', 43),
    ('Thomas', 'Mason', 37)
]


while True:
    name = input("Please enter a name: ")

    if name.lower() == "stop":
        print("End of program!!")
        break

    name_exist = False
    for i in persons:
        if i[0].lower() == name.lower():
            name_exist = True
            break

    if not name_exist:
        print("This name does not exist!!")
        continue

    surname = input("please enter a surname: ")

    if surname.lower() == "stop":
        print("end of program!!")
        break

    person = None
    for i in persons:
        if i[0].lower() == name.lower() and i[1].lower() == surname.lower():
            person = i
            break
    if person:
        print(f"{person[0]} {person[1]} is {person[2]} years old!!")
    else:
        print("This person does not exist")
