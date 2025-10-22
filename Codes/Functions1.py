# Function to calculate total bill amount
def calculate_total_bill(amount, tax_rate, discount):
    """
    Calculates total amount after applying tax and discount.
    """
    tax = amount * tax_rate / 100
    total = amount + tax - discount
    return total

# Main program
print("🧾 Restaurant Billing System 🧾")
amount = float(input("Enter the bill amount: ₹"))
tax_rate = float(input("Enter tax rate (%): "))
discount = float(input("Enter discount amount: ₹"))

total = calculate_total_bill(amount, tax_rate, discount)
print(f"\nTotal amount to be paid: ₹{total:.2f}")
