# Expense Tracker Program (Intermediate Level)

def add_expense(expenses, category, amount):
    """Add a new expense to the dictionary."""
    if category in expenses:
        expenses[category].append(amount)
    else:
        expenses[category] = [amount]
    print(f"Added ₹{amount} to '{category}' category.")

def calculate_total(expenses):
    """Calculate total spending."""
    total = 0
    for category in expenses:
        total += sum(expenses[category])
    return total

def category_summary(expenses):
    """Show total spent in each category."""
    print("\n--- Category-wise Summary ---")
    for category, amounts in expenses.items():
        print(f"{category}: ₹{sum(amounts)}")

def get_highest_spending_category(expenses):
    """Find category with the highest spending."""
    highest_category = max(expenses, key=lambda c: sum(expenses[c]))
    return highest_category, sum(expenses[highest_category])

def main():
    expenses = {}

    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View Total Spending")
        print("3. View Category Summary")
        print("4. View Highest Spending Category")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter category (e.g., food, travel, bills): ").capitalize()
            amount = float(input("Enter amount: ₹"))
            add_expense(expenses, category, amount)

        elif choice == '2':
            print(f"\nTotal Spending: ₹{calculate_total(expenses)}")

        elif choice == '3':
            category_summary(expenses)

        elif choice == '4':
            if expenses:
                category, amount = get_highest_spending_category(expenses)
                print(f"\nHighest spending in '{category}' category: ₹{amount}")
            else:
                print("\nNo expenses added yet.")

        elif choice == '5':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
