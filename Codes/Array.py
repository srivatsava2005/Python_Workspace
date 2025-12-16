# =========================
# 1. LISTS – BASIC "ARRAYS"
# =========================

# Create a list
numbers = [10, 20, 30, 40]      # a simple list of numbers [web:21]
fruits = ["apple", "banana", "cherry"]  # a list of strings [web:21]

print("Numbers:", numbers)
print("Fruits:", fruits)

# Get single items (indexing)
print("First number:", numbers[0])      # 10 [web:21]
print("Last fruit:", fruits[-1])        # "cherry" [web:21]

# Change an item
numbers[1] = 25                         # change 20 to 25 [web:24]
print("After change:", numbers)

# Add items
numbers.append(50)                      # add to the end [web:21]
print("After append:", numbers)

fruits.insert(1, "mango")               # add at position 1 [web:24]
print("After insert:", fruits)

# Remove items
numbers.remove(30)                      # remove value 30 [web:29]
print("After remove:", numbers)

last = fruits.pop()                     # remove last and get it [web:29]
print("After pop:", fruits, "| removed:", last)

# Length of a list
print("How many numbers?", len(numbers))  # 3 items now [web:29]

# Loop through a list
print("Loop through fruits:")
for f in fruits:                        # print each fruit [web:2]
    print(f)

# Slicing (getting a part of the list)
print("First two numbers:", numbers[0:2])  # from index 0 to 1 [web:24]

# =========================
# 2. array MODULE – SIMPLE TYPED ARRAY
# =========================

from array import array                 # built‑in array module [web:32]

# Create an integer array
int_array = array('i', [1, 2, 3, 4])    # 'i' means integer [web:32]
print("int_array:", int_array)

# Access and change values
print("First element:", int_array[0])   # 1 [web:30]
int_array[1] = 20
print("After change:", int_array)

# Add elements
int_array.append(5)                     # add at end [web:30]
print("After append:", int_array)

# =========================
# 3. NUMPY ARRAYS – VERY BASIC
# =========================
# You must install numpy once in your system:
#   pip install numpy    (run this in terminal/command prompt) [web:33]

import numpy as np                      # common short name [web:33]

# Create a NumPy array
np_numbers = np.array([1, 2, 3, 4, 5])  # 1D numeric array [web:12]
print("NumPy array:", np_numbers)

# Simple operations
print("Add 10 to each:", np_numbers + 10)  # element‑wise add [web:16]
print("Double each:", np_numbers * 2)      # element‑wise multiply [web:16]

# 2D array (like a small table)
np_matrix = np.array([[1, 2, 3],
                      [4, 5, 6]])       # 2D array [web:16]
print("Matrix:\n", np_matrix)
print("Shape of matrix:", np_matrix.shape)  # (2, 3) [web:16]
