from abc import ABC, abstractmethod

# Abstract Class
class BankAccount(ABC):

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance   # protected variable (hidden from user)

    @abstractmethod
    def account_type(self):
        pass

    # Common methods
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn {amount}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        return self._balance


# Child class implementing the abstract method
class SavingsAccount(BankAccount):

    def account_type(self):
        return "Savings Account"


# Another child class
class CurrentAccount(BankAccount):

    def account_type(self):
        return "Current Account"


# ----------------------------
# USING THE CLASSES
# ----------------------------

s1 = SavingsAccount("John", 1000)
print(s1.account_type())
s1.deposit(500)
s1.withdraw(300)
print("Balance:", s1.check_balance())

print()

c1 = CurrentAccount("Mike", 2000)
print(c1.account_type())
c1.deposit(1000)
c1.withdraw(2500)
print("Balance:", c1.check_balance())
