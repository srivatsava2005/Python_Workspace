#LIST

# Creating a list
fruits = ["apple", "banana", "cherry", "mango"]

print("Original List:", fruits)

# Accessing elements
print("First element:", fruits[0])       # index 0
print("Last element:", fruits[-1])       # negative index

# List functions/methods
fruits.append("orange")                  # add at end
print("After append:", fruits)

fruits.insert(1, "grape")                # insert at index 1
print("After insert:", fruits)

fruits.remove("banana")                  # remove specific item
print("After remove:", fruits)

popped = fruits.pop()                    # removes last element
print("Popped element:", popped)
print("After pop:", fruits)

print("List length:", len(fruits))       # length of list
print("Is 'apple' in fruits?", "apple" in fruits)

fruits.sort()                            # sort alphabetically
print("Sorted List:", fruits)

fruits.reverse()                         # reverse order
print("Reversed List:", fruits)