#SET

# Creating a set
numbers = {1, 2, 3, 4, 5}
print("\nOriginal Set:", numbers)

# Sets do not allow duplicates
numbers = {1, 2, 2, 3, 4}
print("No duplicates in set:", numbers)

# Adding elements
numbers.add(6)
print("After add:", numbers)

# Removing elements
numbers.remove(3)   # removes 3, error if not found
print("After remove:", numbers)

numbers.discard(10) # no error if element not found
print("After discard(10):", numbers)

popped_item = numbers.pop() # removes random element
print("Popped item:", popped_item)
print("After pop:", numbers)

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("\nSet A:", A)
print("Set B:", B)
print("Union (A ∪ B):", A.union(B))
print("Intersection (A ∩ B):", A.intersection(B))
print("Difference (A - B):", A.difference(B))
print("Symmetric Difference (A Δ B):", A.symmetric_difference(B))