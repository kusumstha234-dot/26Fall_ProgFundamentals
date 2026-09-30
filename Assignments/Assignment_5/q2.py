# Define a function called rectangle_stats.
# This function takes length and width as parameters.
def rectangle_stats(length, width):
    # Calculate the area.
    area = length * width

    # Calculate the perimeter.
    perimeter = 2 * (length + width)

    # Return both calculated values.
    return area, perimeter


# Ask the user to enter the length.
length = float(input("Enter the length: "))

# Ask the user to enter the width.
width = float(input("Enter the width: "))

# Call the function and store both returned values.
area, perimeter = rectangle_stats(length, width)

# Print the results rounded to two decimal places.
print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")
