# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from revisport import helpers
from revisport import SHEET

# data preparation
# data = helpers.prepare_data(SHEET,'owid-co2-data','filter')
# print(data.head())


def main_menu():
    # welcome message
    print("Welcome to ReVisPort!\n")
    print("Your command line reporting tool is ready for you to use.\n")
    print("Please reade carefully and follow the instructions.\n")
    print("\n")

    # welcome qustion
    print("MAIN MENU \n") 
    print("Please select an option from the menu below")
    print("1: Reporting")
    print("2: Favourite")
    print("3: References")

    # select from the menu
    while True:
        try:
            answer = int(input("\nEnter a number of the menu item: "))
        except ValueError:
            print("You did not enter a number")
            continue
        if answer == 1:
            print('You select Reporting') # Reporting Menu
            break
        elif answer == 2:
            print('You select Favourite') # Favourite Menu
            break
        elif answer == 3:
            print('You select Refrences') # Feedback Menu
            break
        else:
            print("Invalid choice, please enter a number from 1, 2, 3!  ")


def report

main_menu()