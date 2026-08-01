
# ხანდახან გაშვების დროს რაღაც ხარვეზი აქვს და თუ პიეველივე ჯერზე არ იმუშავა მეორედაც რომ სცადოთ

# def addition(a=5):
#     count = 0

#     for _ in range(a):
#         user_input = int(input("Please enter a number: "))
#         count += user_input
#     return count


# # result = addition(10)
# # print(result)
# result = addition()
# print(result)

# მეორე ამოცანა

# def odd_even(*args):
#     odd_lst = []
#     even_lst = []

#     for i in args:
#         if i % 2 == 0:
#             even_lst.append(i)
#         else:
#             odd_lst.append(i)
#     return odd_lst, even_lst


# odd, even = odd_even(1, 2, 3, 4, 5, 6, 7, 8, 10)

# print(odd)
# print(even)

# მესამე ამოცანა

# def word_count(text):
#     cleaned_text = text.lower()

#     punctuation = [".", ',', ":", ":", "!", "?"]
#     for char in punctuation:
#         cleaned_text = cleaned_text.replace(char, " ")

#     words = cleaned_text.split()
#     count = {}

#     for word in words:
#         if word in count:
#             count[word] += 1
#         else:
#             count[word] = 1
#     return count


# text = input("Please enter a sentence: ")
# result = word_count(text)

# print(result)

# მეოთხე ამოცანა

# from functools import reduce
# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 15},
#     {"name": "Keyboard", "price": 25},
#     {"name": "Monitor", "price": 150},
#     {"name": "Power", "price": 100},
#     {"name": "Pad", "price": 10},
# ]

# cheap_products = list(filter(lambda p: p["price"] < 100, products))
# print("1. products cheaper than 100$")
# print(cheap_products)

# prod_info = list(map(lambda p: f"{p["name"]} - {p["price"]}$", products))
# print("2. products information")
# print(prod_info)

# sorted_prod = sorted(products, key=lambda p: p["price"])
# print("3. sorted products")
# print(sorted_prod)


# price_sum = reduce(lambda total, p: total + p["price"], products, 0)
# print(f"4. sum of all product price: {price_sum}$")


# მეხუთე ამოცანა

# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum(n-1)


# print(sum(5))
