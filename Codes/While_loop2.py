# Empty shopping list
shopping_list = []

print("Welcome to your Python Grocery List!")
print("Type 'done' when you are finished adding items.\n")

# Keep asking for items until the user types "done"
while True:
    item = input("Add an item to your list: ")
    
    if item.lower() == "done":
        break  # exit the loop
    else:
        shopping_list.append(item)
        print(f"'{item}' added to your list!")

# Show final shopping list
print("\nYour final shopping list:")
for i, product in enumerate(shopping_list, start=1):
    print(f"{i}. {product}")
