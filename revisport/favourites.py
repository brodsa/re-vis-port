
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

    Args:
        SHEET: Object of a Google spredsheet where the favourites are saved.
        input_data: Dataframe of climate data used to create a data summary,
        in case no reports are saved.
    Raises:
        ValueError: Only numbers are allowed.
    """
    print(WHITE)
    print("----------") 
    print("FAVOURITES")
    print("----------") 
    print("All saved reports are saved here and you can maitain them.")
    report_worksheet = Reports(SHEET)
    n_saved_reports = report_worksheet.display_all()
    if n_saved_reports:
        
        print(CYAN)
        print("Please select an option from the menu below:")
        print(" 1: View a report")
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
                report_id = select_report_id(answer,n_saved_reports)

            if answer == 1:
                print('View')
                return
            elif answer == 2:
                print('Delete')
                return
            elif answer == 0:
                rvp.home.main_menu(input_data)
                return
            else:
                print(YELLOW + "Invalid choice, please enter a number from 0 to 2!\n")
    else:
        go_reporting_or_home(SHEET,input_data)
        return

def go_reporting_or_home(SHEET,input_data):
    """
    Displays menu with options to create a report
    or to go back home. The user input is validated 
    and an action is taken.
    """
    print(CYAN)
    rvp.helpers.question_to_save(
            'create a new report',
            'to REPORTING menu',
            'go back to HOME menu')
    while True:
        try:
            print('go_reporting_or_home')
            print(PURPLE + "Enter your choice: " + WHITE, end='')
            answer = int(input().strip())
        except ValueError:
            print(YELLOW + "You did not enter a number.\n")
            continue

        if answer == 1:
            # move to REPORTING menu
            rvp.reporting.reporting_menu(SHEET,input_data)
            return
        elif answer == 2:
            # move to HOME menu
            rvp.home.main_menu(input_data)
            return
        else:
            print(YELOW + "Invalid choice, please enter 1 or 2!\n")


def select_report_id(answer,n_saved_reports):
    """
    Asks to select report ID and validates user inputs.

    Args:
        n_saved_reports: Number of saved reports in FAVOURITES
    Returns: 
        The selected report ID.
    Raises:
        ValueError: Only numbers are allowed.
    """
    while True:
        action = 'view' if answer==1 else 'delete'
        print(
            PURPLE +
            f"Select ID of the report to {action}: " + WHITE, end='')
        try:  
            report_id = int(input().strip())
        except ValueError:
            print(YELLOW + "You did not enter a number.\n")
            continue
        
        if report_id in list(range(0,n_saved_reports)):
            return report_id
        else:
            print(YELLOW + 
            f"Invalid choice, please enter a number smaller than {n_saved_reports}!\n")
