# Built-in Functions in Python (Beginner Example)

# 1. Print function - to display output
print("Welcome to Built-in Functions in Python!")

# 2. Input function - to take user input
name = input("Enter your name: ")

# 3. Type function - to check data type
age = input("Enter your age: ")
print("Type of age before conversion:", type(age))

# Convert age to integer using int() function
age = int(age)
print("Type of age after conversion:", type(age))

# 4. Len function - to find length of a string
print("Your name has", len(name), "characters.")

# 5. Abs function - to get absolute (positive) value
number = -10
print("Absolute value of -10 is:", abs(number))

# 6. Max and Min functions - to find maximum and minimum
numbers = [3, 7, 2, 9, 5]
print("Numbers:", numbers)
print("Maximum number is:", max(numbers))
print("Minimum number is:", min(numbers))

# 7. Sum function - to add all numbers in a list
print("Sum of all numbers is:", sum(numbers))

# 8. Round function - to round off decimal values
decimal_number = 3.756
print("Rounded value of 3.756 is:", round(decimal_number, 2))

# 9. Sorted function - to sort a list
print("Sorted numbers:", sorted(numbers))

# 10. Help function - to get information about any function
print("\nUse 'help(print)' to learn more about print function:")
help(print)
