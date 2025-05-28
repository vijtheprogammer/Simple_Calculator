import time
import os
import platform

# Constants
SLEEP_TIME_SHORT = 0.75
SLEEP_TIME_LONG = 1

def clear_terminal():
    # Check the operating system and clear accordingly
    current_os = platform.system().lower()
    
    if current_os == "windows":
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux or macOS

def loading_animation(duration=SLEEP_TIME_SHORT, dots = 3):
    for _ in range(dots):
        print(".", end='', flush=True)
        time.sleep(0.75)

def main():
    flag = 0
    flag2 = 0

    print()
    print('Welcome to my Calculator!')
    print('------------------------\n')
    
    print('Loading', end='', flush=True)

    loading_animation(SLEEP_TIME_LONG, 3)

    # Clear the line and replace with a new message
    print('\r' + ' ' * 10, end='', flush=True)  # Clear the line by overwriting with spaces
    print('\rLoading complete!', flush=True)
    
    while (flag == 0):
        time.sleep(SLEEP_TIME_SHORT)
        print('\nPlease enter 2 numbers!\n')
        
        # Ensure valid input for both numbers
        while True:
            try:
                time.sleep(SLEEP_TIME_SHORT)
                one = float(input('1. '))
                two = float(input('2. '))
                break  # If valid input, exit the loop
            except ValueError:
                loading_animation(duration=0.75, dots=3)

                # Clear the line and replace with a new message
                print('\r' + ' ' * 10, end='', flush=True)  # Clear the line by overwriting with spaces
                print("Invalid input. Please enter valid numbers.")

            time.sleep(0.5)
            
        # Start the operation menu loop
        try:
            while (flag2 == 0):
                print()
                time.sleep(0.5)
                print('Options')
                print('-------')
                time.sleep(0.75)
                print('1. Add')
                time.sleep(0.75)
                print('2. Subtract')
                time.sleep(0.75)
                print('3. Multiply')
                time.sleep(0.75)
                print('4. Divide')
                time.sleep(0.75)
                print('5. Modulus')
                time.sleep(0.75)
                print()

                # Ensure valid operation choice
                while True:
                    user_choice = input("Please choose an option (1-5): ")
                    if user_choice in ['1', '2', '3', '4', '5']:
                        break  # Exit the loop if valid input
                    else:
                        loading_animation(duration=1, dots=3)

                        # Clear the line and replace with a new message
                        print('\r' + ' ' * 3, end='', flush=True)  # Clear the line by overwriting with spaces
                        print("\rInvalid choice. Please choose a number between 1 and 5.\n", end='', flush=True)

                time.sleep(0.5)
                
                if (user_choice == '1'):  # Addition
                    sum = float(one) + float(two)
                    time.sleep(0.5)
                    print(f"\nThe sum of {one} and {two} is {sum:.2f}.\n")
                    flag2 = 1

                elif (user_choice == '2'):  # Subtraction
                    diff = float(one) - float(two)
                    time.sleep(0.5)
                    print(f"\nThe difference between {one} and {two} is {diff:.2f}.\n")
                    flag2 = 1

                elif (user_choice == '3'):  # Multiplication
                    mult = float(one) * float(two)
                    time.sleep(0.5)
                    print(f"\nThe product of {one} and {two} is {mult:.2f}.\n")
                    flag2 = 1

                elif (user_choice == '4'):  # Division
                    try:
                        quot = float(one) / float(two)
                        remainder = float(one) % float(two)
                        time.sleep(0.75)
                        print(f"\nThe quotient of {one} and {two} is {quot:.2f}.")
                        time.sleep(0.75)
                        print(f"The remainder of {one} and {two} is {remainder:.2f}.\n")
                        flag2 = 1
                    except ZeroDivisionError:
                        print("\nCannot divide by zero. Please try again.")
                        continue  # Re-ask the user for valid input
                
                elif (user_choice == '5'):  # Modulus
                    mod = float(one) % float(two)
                    time.sleep(0.75)
                    print(f"\nThe remainder of {one} and {two} is {mod}.\n")
                    flag2 = 1

        except ValueError:
            print("\nThis program only accepts real numbers between 0-9.\n")
            print("Please enter a real number.\n")

        # Ask if the user wants to continue or exit
        print("Would you like to continue?\n")
        print("1. Continue")
        choice = input("2. Exit\n")

        if (choice == '1'):
            flag = 0  # Continue running
        else:
            print("\nThank you for using my calculator!")
            flag = 1  # Exit the program

            print('Exiting', end='', flush=True)

            loading_animation(duration=1, dots=3)

            # Clear the line and replace with a new message
            print('\r' + ' ' * 10, end='', flush=True)  # Clear the line by overwriting with spaces
            print('\rGoodbye!', flush=True)

    print("\nThis is the output before clearing the terminal.")
    input("Press Enter to clear the terminal...")

    clear_terminal()


if __name__ == '__main__':
    main()
