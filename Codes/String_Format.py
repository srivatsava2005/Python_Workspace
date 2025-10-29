# String Formatting in Python

# 1️⃣ Using the format() method
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))

# You can also use positional arguments
print("I am {0} and I am {1} years old. {0} loves Python!".format(name, age))

# Or keyword arguments
print("My name is {n} and I am {a} years old.".format(n=name, a=age))

# 2️⃣ Using f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")
print(f"Next year, I will be {age + 1} years old.")

# 3️⃣ Using % formatting (older method)
print("My name is %s and I am %d years old." % (name, age))

# 4️⃣ Formatting numbers
price = 49.9876
print("The price is {:.2f} dollars.".format(price))   # 2 decimal places
print(f"The price is {price:.2f} dollars.")           # f-string version

# 5️⃣ Aligning text
text = "Python"
print("{:<10} is left aligned".format(text))   # Left align
print("{:>10} is right aligned".format(text))  # Right align
print("{:^10} is centered".format(text))       # Center align
