from revisport.home import welcome_message
from revisport.home import load_data
from revisport.home import main_menu

def main():
    """ 
    Wraps all functions to start the app.
    First the title and welcome message - welcome_message(),
    than loding data - loading_data(),
    finally starting the actuall program
    with the main menu - main_menu().
    """
    # display the introduction text only at the begining
    welcome_message()

    # load data only once when starting the program
    input_data = load_data()

    # starts the actuall programm
    while True:
        if main_menu(input_data):
            break

main()
