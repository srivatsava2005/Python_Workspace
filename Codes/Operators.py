a = 10
b = 3

# Arithmetic Operators
print("Arithmetic:")
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

# Relational Operators
print("\nRelational:")
print(a == b, a != b, a > b, a < b, a >= b, a <= b)

# Logical Operators
print("\nLogical:")
print(True and False, True or False, not True)

# Bitwise Operators
print("\nBitwise:")
print(a & b, a | b, a ^ b, ~a, a << 1, a >> 1)

# Assignment Operators
print("\nAssignment:")
c = 5
c += 2; print(c)
c -= 1; print(c)

# Membership Operators
print("\nMembership:")
text = "hello"
print("h" in text, "x" not in text)

# Identity Operators
print("\nIdentity:")
x = [1, 2]
y = [1, 2]
z = x
print(x is y, x is z, x is not y)
