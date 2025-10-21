# Initial balance in the account
balance = 1000  

print("Welcome to Python Bank ATM!")

# While there is money in the account
while balance > 0:
    print(f"\nYour current balance is: ${balance}")
    amount = int(input("Enter amount to withdraw: $"))
    
    if amount > balance:
        print("Insufficient balance! Try a smaller amount.")
    else:
        balance -= amount
        print(f"Withdrawal successful! New balance: ${balance}")

print("\nYour account is empty. Thank you for using Python Bank!")
