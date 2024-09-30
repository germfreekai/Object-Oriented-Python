# Account Class

import sys

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amount, password):
        if password != self.password:
            print("Wrong password!", file=sys.stderr)
            return None
        
        if amount < 0:
            print("Can't deposit a negative amount", file=sys.stderr)
            return None
        
        self.balance += amount

        return self.balance

    def withdraw(self, amount, password):
        if password != self.password:
            print("Wrong password!", file=sys.stderr)
            return None

        if amount < 0:
            print("Can't withdraw a negative amount", file=sys.stderr)
            return None

        if amount > self.balance:
            print("Not enought found", file=sys.stderr)
            return None

        self.balance -= amount

        return self.balance

    def get_balance(self, password):
        if password != self.password:
            print("Wrong password!", file=sys.stderr)
            return None

        return self.balance

    def show(self):
        print("Name: ", self.name)
        print("Balance: ", self.balance)
        print("Password: ", self.password)
        print()

acc = Account("Rene", 100, "test")
print(acc.get_balance("test"))
print(acc.deposit(100, "test"))
print(acc.get_balance("test"))
print(acc.withdraw(50, "test"))
print(acc.get_balance("test"))
acc.show()
