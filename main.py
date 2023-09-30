# VERGEL, CHEAN BERNARD V.
# LAB 1
# DIAMOND PATTERN

# import the class
from diamond_pattern import DiamondPattern
# import pyfiglet
import pyfiglet

# Create a header.
print("")
print("=" * 80)
print("")
welcome = pyfiglet.figlet_format("Welcome to my space".center(57, " "), font = "digital" )
print(welcome)
print("")
print("=" * 80)
print("\033[33mHi, I am Chean Bernard V. Vergel a second year college student at Polytechnic University of the Philippines.\033[0m")
print("")

# Ask for the name of the user.
name_of_user = input("\033[35mHow about you what is your name?\U0001F917\033[0m ")
print("")
print("=" * 80)
print("")

# Make a greeting message for the user.
print("\033[23mGood day,",name_of_user,"this program will ask you to input an odd number and use it to make a diamond.\033[0m")
print("")


# Define the DiamondPattern class
class DiamondPattern:
    def print_diamond(self, n):
        if n % 2 == 0:
            print("Error! Provide an odd integer.")
        else:
            for i in range(1, n + 1, 2):
                spaces = " " * ((n - i) // 2)
                element = "*" * i
                print(spaces + element)

            for i in range(n - 2, 0, -2):
                spaces = " " * ((n - i) // 2)
                element = "*" * i
                print(spaces + element)


# Define the user_interface function
def user_interface():
    while True:
        # Ask if the user wants to continue
        agreement = input("\033[96mDo you want to continue answering this program? Type \033[0m\033[40m\033[33mYES\033[0m\033[96m if you want to continue and type \033[0m\033[40m\033[33mNO\033[0m\033[96m if not.\033[0m ").strip().upper()
        print("=" * 80)

        if agreement == "YES":
            # Ask the user for an odd number
            user_input = input("\U0001F6D1 \033[33mEnter an odd integer: \033[0m")

            try:
                n = int(user_input)
                if n % 2 != 0:
                    diamond = DiamondPattern()
                    diamond.print_diamond(n)
                else:
                    print("\U0001F6A7 \033[31mError! Please provide an odd integer. \033[0m")
            except ValueError:
                print("\U0001F6A7 \033[31mInvalid input. Please enter a valid integer. \033[0m")

        elif agreement == "NO":
            print("\033[32mI hope you are doing well. Thank you for your time, " + name_of_user + ".\U0001F600\033[0m")
            break
        else:
            print("\033[91mInvalid input. Please enter either YES or NO.\033[0m")

# Call the user_interface function to start the program
if __name__ == "__main__":
    user_interface()

# Create a footer.
print("=" * 80)
print("")
goodbye = pyfiglet.figlet_format("Visit me again", font="puffy")
print(goodbye)
print("")
print("=" * 80)
print("")









