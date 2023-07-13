import os

import art

from revisport.reporting import reporting_menu
from revisport.favourites import favourites_menu
from revisport.contact import contact_menu
from revisport.quit import quit_menu
from revisport.helpers import prepare_data
from revisport.colors import GREEN, WHITE, CYAN, PURPLE, YELLOW


def welcome_message():
    """
    Prints welcoming message when the program starts.
    """
    print(art.text2art('ReVisPort'))
    print("Welcome to ReVisPort!\n")
    print("It has never been easy to create simple reports.")
    print(
        "ReVisPort navigates you step by step to explore climate",
        "data for EU-countries.")
    print(
        "You can save interesting data",
        "insights to come back to them later on.")
    print(GREEN)
    print("ReVisPort is getting ready ...")

    return


def load_data(SHEET):
    """
    Loads climate data which are used to generate a report.

    Args:
        SHEET(obj): Google sheet object where data are stored.
    """
    return prepare_data(SHEET, 'owid-co2-data', 'filter')


def main_menu(SHEET, input_data):
    """
    Prints main/welcome menu, a user should select from.

    Args:
        SHEET(obj): Google sheet object where data are stored.
        input_data(data frame): Data which are used to
        generate a report.

    Returns:
        False/True: True when the app should be closed.
        False when the app should return HOME.
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
            os.system('clear')
            print(GREEN + 'Reporting selected.')
            reporting_menu(SHEET, input_data)
            break
        elif answer == 2:
            os.system('clear')
            favourites_menu(SHEET, input_data)
            break
        elif answer == 3:
            os.system('clear')
            contact_menu(SHEET, input_data)
            break
        elif answer == 0:
            quit_menu(SHEET)
            return True
        else:
            print(
                YELLOW +
                "Invalid choice, please enter a number from 1, 2, 3!\n"
                )

        return False
