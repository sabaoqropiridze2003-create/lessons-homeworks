# lst = [1, 1, 12, 3, 4, 5]
# lst1 = list()

# str_list = ["nino", "giorgi", "mariami"]
# int_lst = [1, 2, 3, 4, 5]
# mixed_lst = ["nino", 1, 2, 1, 1, 2, True, 2.13, [1, 24, 5],
#              "mariami", 2, 3, 4, 5, ["tamari", 1, 2, 3]]

# lst2 = [[1, 2, 3], [5, 6, 7,], [6, 7, 8]]

# nested_lst = [[1, 2, 3], [5, 6, 7,], [6, 7, 8]]

# print(len(mixed_lst))
# print("nino" in mixed_lst)

# print(str_list + int_lst)

# print(int_lst * 2)
# print(str_list[2])
# print(mixed_lst[4])


# print(nested_lst[1][0])

# print(mixed_lst)

# mixed_lst[0] = "elene"
# print(mixed_lst)

# print(mixed_lst[2:])
# print(mixed_lst[:2])
# print(mixed_lst[1:4:2])
# print(mixed_lst[:])

# new_lst = mixed_lst[:]
# print(new_lst)
# print(id(new_lst))
# print(id(mixed_lst))

# mixed_lst.append("lobio")
# mixed_lst.append(["mwnili", "pomidori"])

# print(mixed_lst)


# print(mixed_lst)

# new_lst = mixed_lst
# new_lst = mixed_lst.copy()

# new_lst.append("rame")
# print(new_lst)
# print(mixed_lst)

# mixed_lst.insert(3, "rame2")
# print(mixed_lst)


# print(mixed_lst)

# mixed_lst.append([1, 2, 3, 4])

# print(mixed_lst)

# mixed_lst.extend([1, 2, 3, 4])
# mixed_lst.extend("giorgi")
# print(mixed_lst)

# mixed_lst.remove(2)


# print(mixed_lst.pop())
# print(mixed_lst.pop(2))

# mixed_lst.clear()
# mixed_lst.append("rame")

# print(mixed_lst)


# int_lst.sort()
# int_lst.sort(reverse=True)
# print(int_lst)

# int_lst.reverse()
# print(int_lst)

# lst2 = ["ana", "elene", "merabi", "lana"]

# lst2.sort()
# print(lst2)

# print(mixed_lst.index("nino"))
# print(mixed_lst.count(1))

# count = 0
# for i in mixed_lst:
#     if i == 1 and type(i) == int:
#         count += 1
# print(count)


# lstx = [x for x in range(10)]

# print(lstx)


# fruits = ["apple", "banana", "mango", "chery"]

# for i, j in enumerate(fruits):
#     print(f"{i} => {j}")

# tup = 1, 2, 3, 4, 5, 6
# tup1 = ("string", 1, 2, 2.13, [1, 2, 3], 1, 2, 3, 4, 4, 1, 1)
# print(type(tup))

# print(tup[0])
# print(tup1.count(1))
# print(tup1.index(2.13))
# print(tup1.index(1))

# a, b, c = (1, 2, 3)
# print(a)

# *a, b, c = tup1

# print(a)
# print(b)
# print(c)

# lst = list(tup)

# print(lst)
# print(type(lst))

# lst[1] = 9

# print(lst)
# new_tup = tuple(lst)
# print(lst)
# print(type(new_tup))

# rame = [1, 2, 3, 4, 4, 6, 7]
# print(rame.count(7))

# result = [x*2 for x in range(5) if x > 2]
# print(result)

# for i in range(5):
#     print(i)

result = ["even" if x % 2 == 0 else "odd" for x in range(5)]

print(result)
