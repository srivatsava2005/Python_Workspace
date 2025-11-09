def factorial(n):
    # Base case: if n is 1, return 1
    if n == 1:
        return 1
    
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)

# Taking user input
num = int(input("Enter a number: "))

# Calling the function and printing result
result = factorial(num)
print(f"Factorial of {num} is {result}")
