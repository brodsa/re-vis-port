from tabulate import tabulate
import pandas as pd
import yaml
import os

import revisport as rvp
from revisport.Reports import Reports
from revisport.colors import *


def reporting_menu(SHEET,input_data):
    """
    Wraps all functions within the reporting menue
    """
    os.system('clear')
    print(WHITE)
    print('---------')
    print('REPORTING')
    print('---------')
    print(
        "You are about to create summary of climate data,",
        "make notes and generate \na report with all standard aspects.")
    print(CYAN)
    print("Are you ready?")
    print(" 1: Yes, continue creating a report.")
    print(" 0: No; go back to HOME MENU.")
    while True:
        try:
            print(PURPLE +"Enter your choice: " + WHITE, end='')
            answer = int(input().strip())
        except ValueError:
            print(YELLOW + "You did not enter a number")
            continue

        if answer == 1:
            while True:
                user_table_data = ask_table_questions(input_data)
                save_input = save_table_answers(SHEET,user_table_data, input_data)
                if save_input:
                    # TODO: still note sure about this
                    return
        elif answer == 0:
            # back to main menu
            os.system('clear')
            rvp.home.main_menu(input_data)
            break
        else:
            print(YELLOW + "Invalid choice, please enter a number 1 or 2!")


def ask_table_questions(input_data):
    """
    Displays all question user has to answer
    in order to generate a report
    """

    # ask for countries
    table_countries = select_country(input_data['countries'])

    # ask for time period
    table_years = select_time_period(input_data['years'])

    # ask for index
    table_index = select_index(input_data['indices'])

    # wrap and save the answer into dictionary
    user_table_data = dict()
    user_table_data['countries'] = table_countries
    user_table_data['years'] = table_years
    user_table_data['index'] = table_index

    return user_table_data


def select_country(countries):
    """
    Asks user to enter countries in the form of iso codes.
    The answer is validated and corresponding error message
    displayed in case of invalid input.
    """

    print(CYAN)
    print(
        "Select ISO codes of EU countries from the list bellow." + 
        WHITE
        )
    print(tabulate(countries, headers=['iso', 'country'], tablefmt="outline"))

    while True:
        print(PURPLE + "Enter your choice (iso1,iso2,etc.): " + WHITE, end='')
        selected_countries = input()
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
                    f"Missing country after comma or no country specified at all")
            else:
                message = "Only valid ISO codes or comma seperator are allowed,you wrote"
                raise ValueError(
                    f"{message} {selected_countries}")
        except (ValueError, IndexError) as e:
            print(YELLOW + f"Invalid input: {e}; please try again.\n")


def select_time_period(years):
    """
    Asks user to enter time period.
    The answer is validated and corresponding
    error message displayed in case of invalid input.
    """
    while True:
        try:
            print(CYAN)
            print(
                "Select a time period from ",
                "years between 2000 and 2020.")
            print(PURPLE + "Enter your choice (yyyy-yyyy): " + WHITE, end='')
            selected_year_txt = input()
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
                print(YELLOW + 
                    "Year selection is not in range (2000-2020); ",
                    "please try again.")

            elif condition_missing_year or condition_same_years:
                print(YELLOW + 'Missing year for a valid range; please try again.')

            elif correct_period and condition_years and condition_order_ok:
                return selected_year_ls

            elif correct_period and condition_years and condition_order_nok:
                print(YELLOW + 
                    "Invalid format:",
                    "a lower bound is larger than an upper bound; ",
                    "please try again.")

            else:
                print(YELLOW + 'Invalid input.')

        except (ValueError,IndexError):
            print(YELLOW + 
                "You did not enter number or a valid range format; ",
                "please try again.")


def select_index(indices):
    print(CYAN)
    print("Please select an index from the list bellow:")
    print(" 1: Population")
    print(" 2: GDP")
    print(" 3: CO2 emmission (million tonnes)")
    print(" 4: Methane emmission (million tonnes of carbon dioxide-equivalents)")
    print(" 5: Energy consumption (terawatt-hours per year)")
    print(" 6: Greenhouse gas emissions (million tonnes of carbon dioxide-equivalents)")

    while True:
        try:
            print(PURPLE + "Enter your choice: " + WHITE, end='')
            answer = int(input())
        except ValueError:
            print(YELLOW + "You did not enter a number\n")
            continue
        if answer in list(range(1, 7)):
            # convert back to the index name
            return indices.iloc[answer-1][0]
        else:
            print(YELLOW + "Invalid choice, please enter a number from 1 to 6!\n")


def save_table_answers(SHEET,user_table_data, input_data):
    print(WHITE)
    print('YOUR SELECTION:')
    print('---------------')
    print(yaml.dump(user_table_data, default_flow_style=False))
    print(CYAN)
    rvp.helpers.question_to_save(
        'save your selection',
        ' generating summary descriptive statistic',
        'make new selection'
    )

    while True:
        try:
            print(PURPLE + "Enter your choice: " + WHITE, end='')
            answer = int(input().strip())
        except ValueError:
            print(YELLOW + "You did not enter a number.\n")
            continue
        if answer == 1:
            report_tables = generate_tables(user_table_data, input_data)
            save_report_menu(SHEET,report_tables,user_table_data)
            return True
        elif answer == 2:
            return False
        else:
            print(YELLOW + "Invalid choice, please enter 1 or 2!\n")


def generate_tables(user_table_data, input_data):
    """
    user_table_data = user inputs from the questionary
    input_data = basis data to generate the report table
    """

    selected_columns = ['iso_code', 'country', 'year']
    selected_columns.append(user_table_data['index'])
    selected_rows_years = input_data['data'].year.between(
        user_table_data["years"][0], user_table_data["years"][1]
        )
    selected_rows_iso = input_data['data'].iso_code.isin(
        user_table_data["countries"]
        )

    report_data = input_data['data'][selected_rows_years & selected_rows_iso]
    raw_df = report_data[selected_columns]
    raw_df = raw_df.reset_index(drop=True)
    raw_df_index = raw_df[['iso_code', 'country', user_table_data['index']]]
    
    # check if the data frame contains missing values and remove them
    condition_missing = '' in raw_df_index.values
    if condition_missing:
        ind_s = raw_df_index.iloc[:,-1]
        missing = ind_s.where(ind_s !='').isna()
        warning_1 = 'Warning: Missing data are removed for summary table!'
        warning_2 = f'Missing data at rows: {missing[missing].index.values}'
        raw_df_index = raw_df_index[[not item for item in missing]]

    agg_functions = ['min', 'max', 'mean', 'median']
    summary_df = raw_df_index.groupby(['iso_code', 'country']).agg(agg_functions)
    summary_df = summary_df.reset_index()

    report_tables = {
        'raw': raw_df,
        'summary': summary_df
    }

    display_tables(
        raw_df=raw_df,
        summary_df=summary_df,
        index_name=user_table_data['index'])

    if condition_missing:
        print(YELLOW + warning_1)
        print(YELLOW + warning_2)

    return report_tables


def display_tables(raw_df, summary_df, index_name):
    """
    Displays tables from the data frames.

    """
    os.system('clear')
    print(WHITE + 'RAW DATA:')
    print(tabulate(
        raw_df,
        headers=raw_df.columns,
        tablefmt="outline"
        ))

    print(f"\nDATA SUMMARY: {index_name}")
    print(tabulate(
        summary_df,
        headers=['iso', 'country', 'min', 'max', 'mean', 'median'],
        tablefmt="outline"
        ))


def save_report_menu(SHEET,report_tables,user_table_data):
    print(CYAN)
    print("Would you like to save the tables?")
    print(" 1: Yes, save and finish creating the report.")
    print(" 0: No, go back to MAIN MENU.")
    while True:
        try:
            print(PURPLE + "Enter your choice: " + WHITE, end='')
            answer = int(input().strip())
        except ValueError:
            print(YELLOW + "You did not enter a number.\n")
            continue

        if answer == 1:
            print(GREEN)
            print('Saving tables ...')
            while True: 
                user_report_data = ask_report_questions(SHEET)
                save_report = save_report_answers(
                    SHEET,
                    user_report_data,
                    report_tables,
                    user_table_data)
                if save_report:
                    return
        elif answer == 0:
            # back to main menu
            return
        else:
            print("Invalid choice, please enter a number 1 or 2!")
    


def ask_report_questions(SHEET):

    saved_reports = rvp.helpers.get_data_from_worksheet(SHEET,'report')
    print(CYAN)
    print("Please fill in following to complete the report.")
    
    if not saved_reports.empty:
        used_titles = [title for title in saved_reports.title]
    else:
        used_titles = [None]
        
    while True:
        print(PURPLE + "Enter report title*: " + WHITE, end='')
        title = input()
        condition_empty = all([item == ' ' for item in title])
        if title in used_titles:
            print(YELLOW + 'Title not available, please try again.\n')
        elif title and not condition_empty:
            break
        else:
            print(YELLOW + 'Title must be specified.\n')

    print(PURPLE + "Enter report author: " + WHITE, end='')
    author = input()
    print(PURPLE + "Enter findings or notes: " + WHITE, end='')
    notes = input()

    user_report_data = {
        'title': title,
        'author': author,
        'notes': notes,
    }

    return user_report_data


def save_report_answers(SHEET,user_report_data,report_tables,user_table_data):
    print(CYAN)
    rvp.helpers.question_to_save(
        'save provided information',
        ' saving the report in FAVOURITES and go back HOME')

    while True:
        try:
            print(PURPLE + "Enter your choice: " + WHITE, end='')
            answer = int(input().strip())
        except ValueError:
            print(YELLOW + "You did not enter a number.\n")
            continue

        if answer == 1:
            report_worksheet = Reports(SHEET)
            report_worksheet.save_new_report(
                user_table_data,
                report_tables,
                user_report_data
            )
            return True
        elif answer == 2:
            print(GREEN)
            print('Discarding entries ...')
            return False
        else:
            print(YELLOW + "Invalid choice, please enter a number from 0 to 1!\n")
