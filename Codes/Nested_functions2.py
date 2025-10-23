def rectangle_calculator(length, width):
    # Outer function to calculate both area and perimeter

    def calculate_area():
        # Inner function to calculate area
        return length * width

    def calculate_perimeter():
        # Inner function to calculate perimeter
        return 2 * (length + width)

    # Calling inner functions
    area = calculate_area()
    perimeter = calculate_perimeter()

    return area, perimeter


# Example usage
l = float(input("Enter the length of the rectangle: "))
w = float(input("Enter the width of the rectangle: "))

area, perimeter = rectangle_calculator(l, w)

print(f"\nArea of Rectangle: {area:.2f}")
print(f"Perimeter of Rectangle: {perimeter:.2f}")
