# პირველი ამოცანა
# sentence = input("enter a sentence: ")
# first_word = sentence.split()[0]
# second_word = sentence.split()[1]
# new_sentence = sentence.replace(first_word, second_word)
# print(new_sentence)

# მეორე ამოცანა

# sentence = input("enter a sentence: ")
# words = sentence.split()
# longest_word = max(words, key=len)
# print(longest_word)

# მესამე ამოცანა

# დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ორ სიტყვას შეამოწმებს არის თუ არა ერთმანეთის ანაგრამა
# ანაგრამა არის ერთ სიტყვაში ასოების გადაადგილებით მიღებული მეორე სიტყვა, მაგალითად ("listen", "silent" ), ("Triangle", "Integral")
# და ა.შ. უნდა იყოს case-insensitive, ანუ მომხმარებელი დიდი ასოებით შემოიყვანს თუ არა ტექსტს, არ უნდა ჰქონდეს მნიშვნელობა.

sentence = input("enter two words: ")
word_one = sentence.split()[0].lower()
word_two = sentence.split()[1].lower()
print(sorted(word_one) == sorted(word_two))

# print(word_one[::-1] == word_two)
