from revisport.helpers import prepare_data
from revisport.reporting import reporting_menu
from revisport import SHEET

def welcome_message():

    """
    Prints welcomming message when the programm starts.
    """

    print("\nWelcome to ReVisPort!\n")
    print("Your command line reporting tool is getting ready for you to use.\n")
    return 

def welcome_load_data():
    print('Loading data ...\n')
    return prepare_data(SHEET,'owid-co2-data','filter')


def welcome_menu():

    """
    Prints main/welcome menu, a user should select from.
    """
    
    print("MAIN MENU")
    print("---------") 
    print("Please select an option from the menu below:")
    print("1: Reporting")
    print("2: Favourite")
    print("3: References")


def get_answer(input_data):

    """
    Gets and validates the user answer/choice from the menu. 
    The user is navigated to the submenu of his/her choice.
    """

    while True:
        try:
            answer = int(input("\nEnter a number of the menu item: ").strip())
        except ValueError:
            print("You did not enter a number")
            continue
        if answer == 1:
            reporting_menu(input_data) # Reporting Menu
            break
        elif answer == 2:
            print('You select Favourite') # Favourite Menu
            break
        elif answer == 3:
            print('You select Refrences') # Feedback Menu
            break
        else:
            print("Invalid choice, please enter a number from 1, 2, 3!  ")


