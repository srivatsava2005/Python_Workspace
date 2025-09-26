# Creating a tuple
fruits = ("apple", "banana", "cherry")

# Accessing elements
print(fruits[0])   # apple
print(fruits[-1])  # cherry

# Tuple with different data types
mixed = (1, "hello", 3.5, True)
print(mixed)

# Nested tuple
nested = (1, (2, 3), (4, 5))
print(nested[1])   # (2, 3)

# Tuple operations
print(len(fruits))          # length of tuple
print(fruits + ("orange",)) # concatenation
print(fruits * 2)           # repetition
