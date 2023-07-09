from revisport.helpers import prepare_data
from revisport.reporting import reporting_menu
from revisport.favourites import favourites_menu
from revisport.contact import contact_menu
from revisport import SHEET
from revisport.colors import *

def welcome_message():

    """
    Prints welcomming message when the programm starts.
    """

    print("\nWelcome to ReVisPort!\n")
    print("It has never been easy to create simple reports.")
    print(
        "ReVisPort navigates you step by step to explore climate",
        "data for EU-countries and more.")
    print("You can save interesting data instights to come back to them later on.")
    print(GREEN)
    print("ReVisPort is getting ready ...")

    return 

def load_data():
    return prepare_data(SHEET,'owid-co2-data','filter')

def goodbye_message():
    print('\nThank you for using ReVisPort.')
    print('Hope we see you come back soon!')


def main_menu(input_data):

    """
    Prints main/welcome menu, a user should select from.
    """
    print(WHITE)
    print("---------") 
    print("HOME MENU")
    print("---------") 
    print(CYAN)
    print("Please select an option from the menu below:")
    print(" 1: Reporting")
    print(" 2: Favourites")
    print(" 3: Contact")
    print(' 0: Quit')

    while True:
        try:
            print(PURPLE + "Enter your choice: " + WHITE, end='')
            answer = int(input().strip())

        except ValueError:
            print(YELLOW + "You did not enter a number.\n")
            continue
        
        if answer == 1:
            print(GREEN + 'Reporting selected.')
            reporting_menu(SHEET,input_data) # Reporting Menu
            break
        elif answer == 2:
            favourites_menu(SHEET,input_data) # Favourite Menu
            break
        elif answer == 3:
            contact_menu(SHEET,input_data)
            break
        elif answer == 0:
            goodbye_message()
            return True
        else:
            print(
                YELLOW + 
                "Invalid choice, please enter a number from 1, 2, 3!\n"
                )

        return False





