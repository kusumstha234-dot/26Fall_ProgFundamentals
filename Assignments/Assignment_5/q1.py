# Define a function called greet_user.
# This function takes the user's name as a parameter.
def greet_user(name):
    # Print the greeting using an f-string.
    print(f"Hello, {name}! Welcome aboard.")


# Ask the user to enter their name.
user_name = input("Enter your name: ")

# Call the greet_user function using the entered name.
greet_user(user_name)
