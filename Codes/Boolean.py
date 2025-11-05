# Current time in 24-hour format
current_time = 14  # 2 PM

# Shop timings
is_shop_open = current_time >= 9 and current_time <= 21

print("Is the shop open?", is_shop_open)

marks = 75
is_passed = marks >= 40

print("Did the student pass?", is_passed)

age = 17
can_vote = age >= 18

print("Can the user vote?", can_vote)
 
items_in_stock = ["apple", "banana", "mango"]

item_to_buy = "orange"
is_available = item_to_buy in items_in_stock

print("Is the item available?", is_available)
