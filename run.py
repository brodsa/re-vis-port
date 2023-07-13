from revisport.home import welcome_message
from revisport.home import load_data
from revisport.home import main_menu

from revisport import SHEET

def main(SHEET):
    """ 
    Wraps all functions to start the app.
    First the title and welcome message - welcome_message(),
    than loading data - loading_data(),
    finally starting the actual program
    with the main menu - main_menu().
    """
    # display the introduction text only when starting app
    welcome_message()

    # load data only once when starting the program
    input_data = load_data(SHEET)

    # starts the actual program
    while True:
        if main_menu(SHEET,input_data):
            break

main(SHEET)
