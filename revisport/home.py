from revisport.helpers import prepare_data
from revisport.reporting import reporting_menu
from revisport import SHEET
import revisport.colors as clr

def welcome_message():

    """
    Prints welcomming message when the programm starts.
    """

    clr.prCyan("\nWelcome to ReVisPort!\n")
    clr.prCyan("It has never been easy to create simple reports.")
    clr.prCyan("ReVisPort navigates you step by step to explore climate data and more.")
    clr.prCyan("You can save interesting data instights to come back to them later on.")
    clr.prCyan("\nRevisPort is getting ready for you to use ...")

    return 

def load_data():
    return prepare_data(SHEET,'owid-co2-data','filter')

def goodbye_message():
    clr.prCyan('\nThank you for using ReVisPort.')
    clr.prCyan('Hope we see you come back soon!')


def main_menu(input_data):

    """
    Prints main/welcome menu, a user should select from.
    """
    print("---------") 
    print("HOME MENU")
    print("---------") 
    print("Please select an option from the menu below:")
    print("1: Reporting")
    print("2: Favourites")
    print("3: References & Feedback")
    print('0: Quit')

    while True:
        try:
            clr.inpYellow("Enter your choice: ")
            answer = int(input().strip())
            clr.prWhite('',end='')
        except ValueError:
            print("You did not enter a number")
            continue
        
        if answer == 1:
            reporting_menu(SHEET,input_data) # Reporting Menu
            break
        elif answer == 2:
            print('You select Favourite') # Favourite Menu
            break
        elif answer == 3:
            print('You select References & Feedback') # Quit
            break
        elif answer == 0:
            goodbye_message()
            return True
        else:
            print("Invalid choice, please enter a number from 1, 2, 3!  ")

        return False





