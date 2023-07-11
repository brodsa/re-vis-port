import pandas as pd

from revisport.favourites import empty_favourite
from revisport.helpers import question_to_save
from revisport.colors import CYAN, WHITE, YELLOW, PURPLE, GREEN


def quit_menu(SHEET):
    """
    Wraps all function for quiting the app
    """

    print(WHITE)
    print(
        "You are about to quit ReVisPort!",
        "But before that, one last question :).")
    print("All your saved reports are goiging to stay in FAVOURITES")

    delete = ask_delete_favourites()

    if delete:
        worksheet = SHEET.worksheet('report')
        df = pd.DataFrame(worksheet.get_all_records())
        if df.empty:
            print(YELLOW)
            print('There are no saved reports.')
        else:
            print(GREEN)
            print('Deleting all reports ..')
            empty_favourite(SHEET)
            print(GREEN)
            print('Reports deleted successfully.')

    goodbye_message()

def goodbye_message():
    """
    Prints goodbye messages.
    """
    print(WHITE)
    print('Thank you for using ReVisPort.')
    print('Hope you have fun and we see you come back soon!\n')

def ask_delete_favourites():
    """
    Asks to delete all saved reports and 
    if so, deletes them.
    """
    print(CYAN)
    question_to_save(
        'empty saved reports from FAVOURITES?'
        ,' discarding all saved reports'
        ,'quit ReVisPort'
    )
    while True:
        try:
            print(PURPLE +"Enter your choice: " + WHITE, end='')
            answer = int(input().strip())
        except ValueError:
            print(YELLOW + "You did not enter a number.\n")
            continue

        if answer==1:
            return True
        elif answer == 2:
            return False
        else:
            print(YELLOW + "Invalid choice, please enter a number 1 or 2!\n")
