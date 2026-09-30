# Define a function called check_number.
# This function checks whether a number is even or odd.
def check_number(number):
    # Check if the number is divisible by 2.
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


# Ask the user to enter a whole number.
number = int(input("Enter a whole number: "))

# Call the function and store the returned result.
result = check_number(number)

# Print the final result using an f-string.
print(f"{number} is an {result} number.")
