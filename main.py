# VERGEL, CHEAN BERNARD V.
# LAB 1
# DIAMOND PATTERN

# import the class
from diamond_pattern import DiamondPattern

# Define the user_interface function
def user_interface():
    # Ask the user for an odd number
    user_input = input("Enter an odd integer: ")

    # Create a try and except block for handling exceptions
    try:
        n = int(user_input)
        # Create an instance of the DiamondPattern class
        diamond = DiamondPattern()
        diamond.print_diamond(n)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Call the user_interface function to start the program
if __name__ == "__main__":
    user_interface()
