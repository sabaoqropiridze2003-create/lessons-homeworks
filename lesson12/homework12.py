# პირველი ამოცანა

# def comition_fee(func):
#     def wrapper(balance, amount):
#         fee = 1
#         total = amount + fee

#         if balance < total:
#             return "There is not enough money on your account"
#         return func(balance - fee, amount)
#     return wrapper


# @comition_fee
# def transaction(balance, amount):
#     new_balance = balance - amount
#     return f"transaction was sucsesfull! new balance: {new_balance} dollars."


# print(transaction(50, 20))
# print(transaction(20, 50))
# print(transaction(21, 20))
# print(transaction(20, 20))

# მეორე ამოცანა

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"function {func.__name__} was called {wrapper.calls} times")
        return (func(*args, **kwargs))
    wrapper.calls = 0
    return wrapper


@count_calls
def add(a, b):
    return a + b


print(add(5, 6))
print(add(10, 20))
print(add(80, 30))
print(add(70, 40))

print(f"function was called {add.calls} times in total")
