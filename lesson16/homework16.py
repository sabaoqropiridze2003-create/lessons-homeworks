class BankAccount:

    bank_name = "TBC Bank"
    __total_acounts = 0

    def __init__(self, owner, balance):

        self._owner = owner
        if self.validate_amount(balance):
            self.__balance = balance
        else:
            self.__balance = 0.0

        BankAccount.__total_acounts += 1
        self.__account_number = f"AN{BankAccount.__total_acounts:04d}"

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    @classmethod
    def get_total_acounts(cls):
        return cls.__total_acounts

    def deposit(self, amount):
        if self.validate_amount(amount):
            self.__balance += amount
            print(f"Deposit successful. New balance: {self.__balance}")
        else:
            print("Deposit failed. Amount must be positive.")

    def withdraw(self, amount):
        if not self.validate_amount(amount):
            print("Withdrawal failed. Amount must be positive.")
            return

        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal successful. New balance: {self.__balance}")
        else:
            print("Withdrawal failed. Insufficient funds.")

    def check_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def change_owner(self, new_owner):
        self._owner = new_owner
        print(f"Account owner changed to: {self._owner}")

    def __str__(self):
        return f"Account: {self.__account_number}, Owner: {self._owner}"


acc1 = BankAccount("saba okropiridze", 1000)
acc2 = BankAccount("giorgi okropiridze", 2000)
acc3 = BankAccount("nino okropiridze", 1300)
print(acc1)
print(acc2)
print(acc3)

print("")

print(f"acc1.get_account_number(): {acc1.check_balance()}")
acc1.deposit(500)
acc1.withdraw(200)
print("new balance: ", acc1.check_balance())

print("")

acc2.change_owner("niko nikoladze")
print(acc2)

print("")

print(F"Total accounts created: {BankAccount.get_total_acounts()}")
