# Squares of even numbers from 1 to 20
squares = []  # empty list

for i in range(1, 21):
    if i % 2 == 0:   # check if the number is even
        squares.append(i * i)
        print("Square of", i, "is", i * i)

print("All even squares:", squares)
# Output: All even squares: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
