from tabulate import tabulate
import pandas as pd
import yaml

import revisport as rvp
from revisport import SHEET


def reporting_menu(input_data):
    """
    Wraps all functions within the reporting menue
    """

    print("\nYou are going to create a simple report.")
    print(
        "The report contains a table with the ",
        "information about EU countries and climate indices.")
    print("The programm navigates you to generate the report.\n")

    print("Are you ready?")
    print("1: yes, continue creating the report")
    print("0: no; go back to MAIN MENU")
    while True:
        try:
            answer = int(input("Enter your choice: ").strip())
        except ValueError:
            print("You did not enter a number")
            continue

        if answer == 1:
            while True:
                report_input = ask_table_questions(input_data)
                save_input = save_table_answers(report_input, input_data)
                if save_input:
                    # TODO: still note sure about this
                    return
        elif answer == 0:
            # back to main menu
            rvp.main_menu.main_menu(input_data)
            break
        else:
            print("Invalid choice, please enter a number 1 or 2!")


def ask_table_questions(input_data):
    """
    Displays all question user has to answer
    in order to generate a report
    """

    # ask for countries
    report_countries = select_country(input_data['countries'])

    # ask for time period
    report_years = select_time_period(input_data['years'])

    # ask for index
    report_index = select_index(input_data['indices'])

    # wrap and save the answer into dictionary
    report_input = dict()
    report_input['countries'] = report_countries
    report_input['years'] = report_years
    report_input['index'] = report_index

    return report_input


def select_country(countries):
    """
    Asks user to enter countries in the form of iso codes.
    The answer is validated and corresponding error message
    displayed in case of invalid input.
    """

    print("\nSelect countries for which you want to the report.")
    print(
        "Enter iso code of selected countries, ",
        "use comma as a separator (iso1,iso2,...):")
    print(tabulate(countries, headers=['iso', 'country'], tablefmt="outline"))

    while True:
        selected_countries = input('Enter your choice:')
        countries_ls = [
            country.upper().strip()
            for country in selected_countries.split(',')
            ]

        try:
            correct_countries = all(
                [item in countries.country for item in countries_ls])

            if correct_countries:
                return countries_ls

            elif countries_ls[-1] == '':
                raise ValueError(
                    "Missing country after comma ",
                    "or no country specified at all")
            else:
                raise ValueError(f"Only valid ISO codes or comma seperator are allowed,you wrote {selected_countries}")
        except (ValueError, IndexError) as e:
            print(f"Invalid input: {e}; please try again.\n")


def select_time_period(years):
    """
    Asks user to enter time period.
    The answer is validated and corresponding
    error message displayed in case of invalid input.
    """
    while True:
        try:
            print(
                "\nSelect a time period from ",
                "years 2000 and 2020 (yyyy-yyyy).")
            selected_year_txt = input("Enter your choice:")
            selected_year_ls = [
                int(year.strip())
                for year in selected_year_txt.split('-')
                ]
            correct_period = all([
                year in years for year in selected_year_ls
                ])

            # conditions for error messages
            condition_missing_year = len(selected_year_ls) == 1
            condition_same_years = selected_year_ls[0] == selected_year_ls[1]
            condition_years = len(selected_year_ls) == 2
            condition_order_ok = selected_year_ls[0] < selected_year_ls[1]
            condition_order_nok = selected_year_ls[0] > selected_year_ls[1]

            if not correct_period:
                print(
                    "Year selection is not in range (2000-2020); ",
                    "please try again.")

            elif condition_missing_year or condition_same_years:
                print('Missing year for a valid range; please try again.')

            elif correct_period and condition_years and condition_order_ok:
                return selected_year_ls

            elif correct_period and condition_years and condition_order_nok:
                print(
                    "Invalid format, ",
                    "a lower bound is larger than an upper bound; ",
                    "please try again.")

            else:
                print('Invalid input.')

        except ValueError:
            print(
                "You did not enter number nor a valid range format; ",
                "please try again.")


def select_index(indices):
    print("\nPlease select an index from the list bellow:")
    print("1: GDP")
    print("2: Population")
    print("3: CO2 emmission (million tonnes)")
    print("4: Methane emmission (million tonnes of carbon dioxide-equivalents)")
    print("5: Energy consumption (terawatt-hours per year)")
    print("6: Greenhouse gas emissions (million tonnes of carbon dioxide-equivalents)")

    while True:
        try:
            answer = int(input("Enter your choice: ").strip())
        except ValueError:
            print("You did not enter a number")
            continue
        if answer in list(range(1, 7)):
            # covert back to the index name
            return indices.iloc[answer-1][0]
        else:
            print("Invalid choice, please enter a number from 1 to 6!")


def save_table_answers(report_input, input_data):
    print('\nYour choices:')
    print(yaml.dump(report_input, default_flow_style=False))
    # ask to save 1: yes; 2: no
    rvp.helpers.question_to_save()

    while True:
        try:
            answer = int(input("Enter your choice: ").strip())
            print(answer, answer == 1)
        except ValueError:
            print("You did not enter a number")
            continue
        if answer == 1:
            generate_tables(report_input, input_data)
            save_report_menu()
            return True
        elif answer == 2:
            return False
        else:
            print("Invalid choice, please enter 1 or 2!")


def generate_tables(report_input, input_data):
    """
    report_input = user inputs from the questionary
    input_data = basis data to generate the report table
    """

    selected_columns = ['iso_code', 'country', 'year']
    selected_columns.append(report_input['index'])
    selected_rows_years = input_data['data'].year.between(
        report_input["years"][0], report_input["years"][1]
        )
    selected_rows_iso = input_data['data'].iso_code.isin(
        report_input["countries"]
        )

    report_data = input_data['data'][selected_rows_years & selected_rows_iso]
    raw_df = report_data[selected_columns]
    raw_df = raw_df.reset_index(drop=True)

    summary_df = raw_df[['iso_code', 'country', report_input['index']]].groupby(
        ['iso_code', 'country']).agg(['min', 'max', 'mean', 'median'])
    summary_df = summary_df.reset_index()

    report_tables = {
        'raw': raw_df,
        'summary': summary_df
    }


    display_tables(
        raw_df=raw_df,
        summary_df=summary_df,
        index_name=report_input['index'])

    return report_tables


def display_tables(raw_df, summary_df, index_name):
    """
    Displays tables from the data frames.

    """
    # TODO: color blue
    print('\nRaw data:')
    print(tabulate(
        raw_df,
        headers=raw_df.columns,
        tablefmt="outline"
        ))

    print(f"\nData sumary: {index_name}")
    print(tabulate(
        summary_df,
        headers=['iso', 'country', 'min', 'max', 'mean', 'median'],
        tablefmt="outline"
        ))


def save_report_menu():
    print("Would you like to save the tables?")
    print("1: Yes; save and continue to create the report")
    print("0: No; go back to MAIN MENU")
    while True:
        try:
            answer = int(input("Enter your choice: ").strip())
        except ValueError:
            print("You did not enter a number")
            continue

        if answer == 1:
            while True:
                user_report_data = ask_report_questions()
                save_report = save_report_answers(user_report_data)
                if save_report:

                    return
        elif answer == 0:
            # back to main menu
            return
        else:
            print("Invalid choice, please enter a number 1 or 2!")


def ask_report_questions():

    saved_reports = rvp.helpers.get_data_from_worksheet(SHEET,'report')
    used_titles = [title for title in saved_reports.title]
    print("\nPlease fill in following to save the report.")
    while True:
        title = input("Enter title*: ")
        condition_empty = all([item != ' ' for item in title])
        if title in used_titles:
            print('Title not available, please try again.')
        elif title and condition_empty:
            break
        else:
            print('Title must be specified.')

    author = input("Enter author: ")
    notes = input("Enter findings or notes: ")

    user_report_data = {
        'title': title,
        'author': author,
        'notes': notes,
    }

    return user_report_data


def save_report_answers(user_report_data):
    print()
    rvp.helpers.question_to_save()

    while True:
        try:
            answer = int(input("Enter your choice: ").strip())
            print(answer, answer == 1)
        except ValueError:
            print("You did not enter a number")
            continue

        if answer == 1:
            save_report(user_report_data)
            return True
        elif answer == 2:
            return False
        else:
            print("Invalid choice, please enter a number from 0 to 1!")


def save_report(user_report_data):
    """
    Saves the report.
    """
    print('Saving report ...')
    print(user_report_data)
    #tables
    #path_to_tables
    #tables_answers
    #update_worksheet(SHEET,sheetname='report',row_data)
    print(f"Report saved successfully.\n")