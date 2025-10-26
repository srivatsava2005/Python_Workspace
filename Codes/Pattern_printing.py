# Right-Angled Triangle Pattern

rows = 5  # number of rows

for i in range(1, rows + 1):
    print("*" * i)

# Inverted Triangle Pattern

rows = 5

for i in range(rows, 0, -1):
    print("*" * i)

# Pyramid Pattern

rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
