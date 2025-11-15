class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance     # Private variable

    # Getter method for balance
    def get_balance(self):
        return self.__balance

    # Setter method for balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds!")

# Using the class
acc = BankAccount("Alice", 5000)

print("Account Owner:", acc.owner)
print("Current Balance:", acc.get_balance())  # Accessing private variable through getter

acc.deposit(2000)
acc.withdraw(1500)

# Trying to access private variable directly
try:
    print(acc.__balance)
except AttributeError:
    print("Cannot access private variable '__balance' directly!")
