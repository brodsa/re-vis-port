import os

import revisport as rvp
from revisport.reporting import Reports
from revisport.reporting import reporting_menu
from revisport.helpers import empty_directory
from revisport.helpers import delete_report_from_sheet
from revisport.colors import WHITE, GREEN, PURPLE, CYAN, YELLOW


def empty_favourite(SHEET):
    empty_directory('./report/raw_tables')
    empty_directory('./report/summary_tables')
    delete_report_from_sheet(SHEET)


def favourites_menu(SHEET, input_data):
    """
    Wraps all functions for FAVOURITES menu and
    displays the menu which a user should select from.

    Args:
        SHEET (obj): Object of a Google spreadsheet
            where the FAVOURITES are saved.
        input_data (data frame): Data frame of climate data used to
            create a data summary,
            in case no reports are saved.
    Raises:
        ValueError: Only numbers are allowed.
    """
    print(WHITE)
    print("----------")
    print("FAVOURITES")
    print("----------")
    print("All saved reports are saved here and you can maintain them.")
    while True:
        report_worksheet = Reports(SHEET)
        n_reports = report_worksheet.display_all()
        if n_reports:

            while True:
                print(CYAN)
                print("Please select an option from the menu below:")
                print(" 1: View a report")
                print(" 2: Delete a report")
                print(" 3: Create a report")
                print(" 0: Go back to HOME MENU")

                try:
                    print(PURPLE + "Enter your choice: " + WHITE, end='')
                    answer = int(input().strip())
                except ValueError:
                    print(YELLOW + "You did not enter a number.\n")
                    continue

                if answer in [1, 2]:
                    report_id = select_report_id(answer, n_reports)

                if answer == 1:
                    report_worksheet.display_one_report(report_id)
                    input(CYAN + 'Press any key to close report ...')
                    break
                elif answer == 2:
                    report_worksheet.delete_report(report_id)
                    break
                elif answer == 3:
                    reporting_menu(SHEET, input_data)
                    return
                elif answer == 0:
                    os.system('clear')
                    rvp.home.main_menu(SHEET, input_data)
                    return
                else:
                    txt_print = "please enter a number from 0 to 2!\n"
                    print(YELLOW + f"Invalid choice, {txt_print}")
        else:
            go_reporting_or_home(SHEET, input_data)
            return


def go_reporting_or_home(SHEET, input_data):
    """
    Displays menu with options to create a report
    or to go back home. The user input is validated
    and an action is taken.

    Args:
        SHEET (obj): Object of a Google spreadsheet where
            the FAVOURITES are saved.
        input_data (data frame): Data frame of climate data
            used to create a data summary,
            in case no reports are saved.
    """
    print(CYAN)
    rvp.helpers.question_to_save(
            'create a new report',
            'to REPORTING menu',
            'go back to HOME menu')
    while True:
        try:
            print(PURPLE + "Enter your choice: " + WHITE, end='')
            answer = int(input().strip())
        except ValueError:
            print(YELLOW + "You did not enter a number.\n")
            continue

        if answer == 1:
            # move to REPORTING menu
            rvp.reporting.reporting_menu(SHEET, input_data)
            return
        elif answer == 2:
            # move to HOME menu
            rvp.home.main_menu(SHEET, input_data)
            return
        else:
            print(YELLOW + "Invalid choice, please enter 1 or 2!\n")


def select_report_id(answer, n_reports):
    """
    Asks to select report ID and validates user inputs.

    Args:
        answer(str): either view or delete.
        n_reports: Number of saved reports in FAVOURITES

    Returns:
        The selected report ID.
    """
    while True:
        action = 'view' if answer == 1 else 'delete'
        print(
            PURPLE +
            f"Select ID of the report to {action}: " + WHITE, end='')
        try:
            report_id = int(input().strip())
        except ValueError:
            print(YELLOW + "You did not enter a number.\n")
            continue

        if report_id in list(range(0, n_reports)):
            return report_id
        else:
            txt_print = "please enter a number smaller than or equal to "
            print(YELLOW + f"Invalid choice,{txt_print} {n_reports-1}!\n")
