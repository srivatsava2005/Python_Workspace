def check_balance(balance):
    print(f"Your current balance is: ₹{balance:.2f}")

def deposit(balance, amount):
    balance += amount
    print(f"₹{amount:.2f} deposited successfully.")
    return balance

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
    return balance

# Main program
balance = 1000.00  # Starting balance
while True:
    print("\n🏧 Simple ATM Menu 🏧")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance(balance)
    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        balance = deposit(balance, amount)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))
        balance = withdraw(balance, amount)
    elif choice == "4":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
