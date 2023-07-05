
import revisport as rvp

from revisport.Reports import Reports
from revisport import SHEET
from revisport.colors import *

from revisport.helpers import empty_directory
from revisport.helpers import empty_report_sheet

def empty_favourite():
    empty_directory('./report/raw_tables')
    empty_directory('./report/summary_tables')
    empty_report_sheet(SHEET,sheetname='report')


def favourites_menu(SHEET,input_data):
    """
    Prints favourites menu, a user should select from.
    """
    print(WHITE)
    print("----------") 
    print("FAVOURITES")
    print("----------") 
    print("All your intereting reports are saved here.")
    print(CYAN)
    print("Please select an option from the menu below:")
    print(" 1: View saved reports")
    print(" 2: Delete a report")
    print(" 0: Go back to HOME MENU")

    while True:
        try:
            print(PURPLE +"Enter your choice: " + WHITE, end='')
            answer = int(input().strip())
        except ValueError:
            print(YELLOW + "You did not enter a number.\n")
            continue

        if answer in [1,2]:
            report_worksheet = Reports(SHEET)
            saved_reports = report_worksheet.display_all()
            print(GREEN + 'Loading reports ...')

            # if saved_reports:
            #     print('Display list of reports')
            # else:
            #     rvp.helpers.question_to_save('create report','to REPORTING menu')
            #     rvp.reporting.reporting_menu(SHEET,input_data)
        if answer == 1:
            print('Select report ID')
        elif answer == 2:
            print('Delete reports')
        elif answer == 0:
            rvp.home.main_menu(input_data)
            break
        else:
            print(YELLOW + "Invalid choice, please enter a number from 0 to 2!\n")