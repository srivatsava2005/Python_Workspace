# Simple Bank Account Management System (Intermediate Level)

def create_account(accounts, name, initial_balance=0.0):
    """Create a new bank account."""
    if name in accounts:
        print(f"Account for '{name}' already exists.")
    else:
        accounts[name] = {"balance": initial_balance, "transactions": []}
        print(f"Account created for {name} with initial balance ₹{initial_balance}")

def deposit(accounts, name, amount):
    """Deposit money into an account."""
    if name in accounts:
        accounts[name]["balance"] += amount
        accounts[name]["transactions"].append(f"Deposited ₹{amount}")
        print(f"₹{amount} deposited successfully. New balance: ₹{accounts[name]['balance']}")
    else:
        print(f"No account found for '{name}'")

def withdraw(accounts, name, amount):
    """Withdraw money from an account."""
    if name not in accounts:
        print(f"No account found for '{name}'")
        return

    if accounts[name]["balance"] >= amount:
        accounts[name]["balance"] -= amount
        accounts[name]["transactions"].append(f"Withdrew ₹{amount}")
        print(f"₹{amount} withdrawn successfully. New balance: ₹{accounts[name]['balance']}")
    else:
        print("Insufficient balance!")

def check_balance(accounts, name):
    """Display current balance."""
    if name in accounts:
        print(f"Current balance for {name}: ₹{accounts[name]['balance']}")
    else:
        print(f"No account found for '{name}'")

def transaction_history(accounts, name):
    """Show all transactions for a specific user."""
    if name in accounts:
        print(f"\nTransaction history for {name}:")
        for t in accounts[name]["transactions"]:
            print(f"- {t}")
        print(f"Current Balance: ₹{accounts[name]['balance']}")
    else:
        print(f"No account found for '{name}'")

def main():
    accounts = {}

    while True:
        print("\n=== Bank Management System ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter account holder name: ").capitalize()
            initial = float(input("Enter initial deposit (₹): "))
            create_account(accounts, name, initial)

        elif choice == "2":
            name = input("Enter account holder name: ").capitalize()
            amount = float(input("Enter amount to deposit (₹): "))
            deposit(accounts, name, amount)

        elif choice == "3":
            name = input("Enter account holder name: ").capitalize()
            amount = float(input("Enter amount to withdraw (₹): "))
            withdraw(accounts, name, amount)

        elif choice == "4":
            name = input("Enter account holder name: ").capitalize()
            check_balance(accounts, name)

        elif choice == "5":
            name = input("Enter account holder name: ").capitalize()
            transaction_history(accounts, name)

        elif choice == "6":
            print("\nThank you for using the Bank Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
