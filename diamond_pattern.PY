# VERGEL, CHEAN BERNARD V.
# LAB 1
# DIAMOND PATTERN

# Define a class called DiamondPattern
class DiamondPattern:
    # Define the print_diamond method
    def print_diamond(self, n):  # Add self as the first parameter for methods in a class
        # If the number is even, print an error message
        if n % 2 == 0:
            print("Error! Provide an odd integer.")
        else:
            # Creating the upper part of the diamond
            for i in range(1, n + 1, 2):
                spaces = " " * ((n - i) // 2)
                element = "*" * i
                print(spaces + element)

            # Creating the lower part of the diamond
            for i in range(n - 2, 0, -2):
                spaces = " " * ((n - i) // 2)
                element = "*" * i
                print(spaces + element)
