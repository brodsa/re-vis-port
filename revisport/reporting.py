import os

import pandas as pd
import yaml
from tabulate import tabulate

import revisport as rvp
from revisport.helpers import empty_directory
from revisport.helpers import delete_report_from_sheet
from revisport.colors import WHITE, GREEN, PURPLE, CYAN, YELLOW


def reporting_menu(SHEET, input_data):
    """
    Wraps all functions within the reporting menu.
    Displays the menu, from which a user should
    select from.

    Args:
        SHEET (obj): Object of a Google spreadsheet
            where the FAVOURITES are saved.
        input_data (data frame): Data frame of climate data used to
            create a data summary,
            in case no reports are saved.

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
            print(PURPLE + "Enter your choice: " + WHITE, end='')
            answer = int(input().strip())
        except ValueError:
            print(YELLOW + "You did not enter a number")
            continue

        if answer == 1:
            while True:
                user_table_data = ask_table_questions(input_data)
                save_input = save_table_answers(
                    SHEET=SHEET,
                    user_table_data=user_table_data,
                    input_data=input_data)

                if save_input:
                    return

        elif answer == 0:
            os.system('clear')
            rvp.home.main_menu(SHEET, input_data)
            break

        else:
            print(YELLOW + "Invalid choice, please enter a number 1 or 2!")


def ask_table_questions(input_data):
    """
    Displays all questions, a user has to answer
    in order to generate a report.

    Args:
        input_data(data frame): Data frame with climate data
            used to generate a summary data table.
    Returns:
        user_table_data: User answers to create a summary data table
    """

    # ask for countries
    table_countries = select_country(input_data['countries'])

    # ask for time period
    table_years = select_time_period(input_data['years'])

    # ask for index
    table_index = select_index(input_data['indices'])

    # wrap and save the answer into dictionary
    user_table_data = {
        'countries': table_countries,
        'years': table_years,
        'index': table_index
    }

    return user_table_data


def select_country(countries):
    """
    Asks user to enter countries in the form of iso codes.
    Validates the answer.

    Args:
        countries(data frame): Data frame of all EU countries;
            two columns(iso code; country name).

    Returns:
        Selected iso codes of countries.
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
            for country in selected_countries.split(',')]

        try:
            correct_countries = all(
                [item in countries.country for item in countries_ls])

            if correct_countries:
                return countries_ls

            elif countries_ls[-1] == '':
                txt_error_1 = "Missing country after comma"
                txt_error_2 = "or no country specified at all"
                raise ValueError(f"{txt_error_1} {txt_error_2}")
            else:
                error_1 = "Only valid ISO codes"
                error_2 = "or comma separator are allowed, you wrote"
                raise ValueError(f"{error_1} {error_2} {selected_countries}")

        except (ValueError, IndexError) as e:
            print(YELLOW + f"Invalid input: {e}; please try again.\n")


def select_time_period(years):
    """
    Asks user to enter time period.
    The answer is validated and corresponding
    error message displayed in case of invalid input.

    Args:
        years(data frame): List of available years.

    Retunrs:
        Selected period.
    """
    while True:
        try:
            print(CYAN)
            print(
                "Select a time period from ",
                "years between 2000 and 2020.")
            print(PURPLE + "Enter your choice (yyyy-yyyy): " + WHITE, end='')
            answer = input()

            period = [int(year.strip()) for year in answer.split('-')]
            cond = create_condition_period(period, years)

            if not cond["period"]:
                txt_1 = "Year selection is not in range (2000-2020);"
                txt_2 = " please try again."
                print(YELLOW + txt_1 + txt_2)

            elif cond["missing_year"] or cond["same_years"]:
                message = "Missing year for a valid range; please try again."
                print(YELLOW + message)

            elif cond["period"] and cond["years"] and cond["order_ok"]:
                return period

            elif cond["period"] and cond["years"] and cond["order_nok"]:
                txt_1 = "Invalid format:"
                txt_2 = "a lower bound is larger than an upper bound; "
                txt_3 = "please try again."
                print(YELLOW + txt_1 + txt_2 + txt_3)

            else:
                print(YELLOW + 'Invalid input.')

        except (ValueError, IndexError):
            txt_1 = "You did not enter number or a valid range format; "
            txt_2 = "please try again."
            print(YELLOW + txt_1 + txt_2)


def create_condition_period(period, years):
    """
    Creates condition to check if the user input for
    time period is valid.

    Args:
        period(ls): List with lower and upper
            bound for time period.
        years(ls): List of available years.

    Returns:
        condition(dict): Dictionary of all condition to
            check the validity of the user input.
    """
    condition = dict()
    condition["period"] = all([year in years for year in period])
    condition["missing_year"] = len(period) == 1
    condition["same_years"] = period[0] == period[1]
    condition["years"] = len(period) == 2
    condition["order_ok"] = period[0] < period[1]
    condition["order_nok"] = period[0] > period[1]

    return condition


def select_index(indices):
    """
    Asks to select index.

    Args:
        indices(data frame): List of indices.

    Returns:
        Selected index.
    """
    print(CYAN)
    print("Please select an index from the list bellow:")
    print(" 1: Population (million)")
    print(" 2: GDP (billion US Dollars)")
    print(" 3: CO2 emission (million tonnes)")
    print(
        " 4: Methane emission",
        "(million tonnes of carbon dioxide-equivalents)")
    print(
        " 5: Energy consumption",
        "(terawatt-hours per year)")
    print(
        " 6: Greenhouse gas emissions",
        "(million tonnes of carbon dioxide-equivalents)")

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
            message = "Invalid choice, please enter a number from 1 to 6!\n"
            print(YELLOW + message)


def save_table_answers(SHEET, user_table_data, input_data):
    """
    Asks to save the answers to generate summary statistics.

    Args:
        user_table_data(dict): Selection of countries,
            time period and index.
        input_data(data frame): Basis climate data to
            generate the tables.
    """
    print(WHITE)
    print('YOUR SELECTION:')
    print('---------------')
    print(yaml.dump(user_table_data, default_flow_style=False))
    print(CYAN)
    rvp.helpers.question_to_save(
        'save your selection',
        ' generating summary descriptive statistics',
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
            save_report_menu(SHEET, report_tables, user_table_data)
            return True
        elif answer == 2:
            return False
        else:
            print(YELLOW + "Invalid choice, please enter 1 or 2!\n")


def generate_tables(user_table_data, input_data):
    """
    Generates report tables based on the user selection
    and climate data.

    Args:
        user_table_data(data frame): User inputs from the questionary.
        input_data(data frame): Basis data to generate the report table.

    Returns:
        report_tables(dict): Dictionary of two tables
            (raw data and summary data).
    """

    selected_columns = ['iso_code', 'country', 'year']
    selected_columns.append(user_table_data['index'])
    selected_rows_years = input_data['data'].year.between(
        user_table_data["years"][0], user_table_data["years"][1])
    selected_rows_iso = input_data['data'].iso_code.isin(
        user_table_data["countries"])

    report_data = input_data['data'][selected_rows_years & selected_rows_iso]
    raw_df = report_data[selected_columns]
    raw_df = raw_df.reset_index(drop=True)
    raw_df_index = raw_df[['iso_code', 'country', user_table_data['index']]]

    # check if the data frame contains missing values
    condition_missing = '' in raw_df_index.values
    if condition_missing:
        raw_df_index, warning_1, warning_2 = remove_missing_data(raw_df_index)

    agg_functions = ['min', 'max', 'mean', 'median']
    summary_df = raw_df_index.groupby(
        ['iso_code', 'country']).agg(agg_functions)
    summary_df = summary_df.reset_index()

    report_tables = {
        'raw': raw_df,
        'summary': summary_df}

    display_tables(
        raw_df=raw_df,
        summary_df=summary_df,
        index_name=user_table_data['index'])

    if condition_missing:
        print(YELLOW + warning_1)
        print(YELLOW + warning_2)

    return report_tables


def remove_missing_data(raw_df_index):
    """
    Removes missing values from the raw data table
    used to create a descriptive summary statistics.

    Args:
        raw_df_index(data frame): Raw data frame of climate data.

    Returns:
        raw_df_index(data frame): A clean data frame.
        warning_1/warning_2: Warning messages in case
            missing data were removed.
    """
    ind_s = raw_df_index.iloc[:, -1]
    missing = ind_s.where(ind_s != '').isna()
    warning_1 = 'Warning: Missing data are removed for summary table!'
    warning_2 = f'Missing data at rows: {missing[missing].index.values}'
    raw_df_index = raw_df_index[[not item for item in missing]]

    return raw_df_index, warning_1, warning_2


def display_tables(raw_df, summary_df, index_name):
    """
    Displays tables of raw data and summary data.

    Args:
        raw_df(data frame): Raw data.
        summary_df(data frame): Summary descriptive statistics.
        index_name(str): Name of the selected index.

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


def save_report_menu(SHEET, report_tables, user_table_data):
    """
    Wraps all functions to save the report and
    shows the menu.

    Args:
        SHEET: Google Sheet object, where the report information
            are stored
        report_tables(dict): Two tables (raw and summary).
        user_table_data(dict): Selection of countries,
            time period and index.
    """
    print(CYAN)
    print("Would you like to save the tables?")
    print(" 1: Yes, save and finish creating the report.")
    print(" 0: No, go back to HOME MENU.")
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
    """
    Asks user to fill in the report information,
    such as title, author, notes.

    Args:
        SHEET: Google Sheet, used to get all report titles
            which must be unique.

    Returns:
        user_report_data(dict): Title, author, and notes.
    """
    saved_reports = rvp.helpers.get_data_from_worksheet(SHEET, 'report')
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


def save_report_answers(SHEET, user_report_d, report_tables, user_table_d):
    """
    Asks to save report.

    Args:
        SHEET (obj): Object of a Google spreadsheet
            where the FAVOURITES are saved.
        user_report_data(dict): User selection of countries,
            time period and index.
        report_tables(dict): Created tables: raw and summary
            descriptive statistics.
        user_table_data(dict): User data to save the report,
            like title, author, and notes.
    """
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
                user_table_d,
                report_tables,
                user_report_d
            )
            return True

        elif answer == 2:
            print(GREEN)
            print('Discarding entries ...')
            return False

        else:
            message = "Invalid choice, please enter a number from 0 to 1!\n"
            print(YELLOW + message)


class Reports():
    """
    Reports is an object describing and maintaining
    all reports and related information
    filled in by user.
    """
    def __init__(self, SHEET):
        """
        Initializes the object Reports.

        Vars:
            SHEET(obj): Google sheet object.
        """
        self.SHEET = SHEET
        self.worksheet_name = 'report'
        self.worksheet = SHEET.worksheet('report')

    def save_new_report(self, user_tab_data, report_tables, user_report_data):
        """
        Saves a new created report into Google sheet and csv files.

        Args:
            user_report_data(dict): User selection of countries,
                time period and index.
            report_tables(dict): Created tables: raw and summary
                descriptive statistics.
            user_tab_data(dict): User data to save the report,
                like title, author, and notes.
        """
        self.user_tab_data = user_tab_data
        self.report_tables = report_tables
        self.user_report_data = user_report_data

        print(GREEN)
        print(f'Saving {self.worksheet_name} ...')

        # save tables into csv
        filename = user_report_data['title'].replace(' ', '_') + '.csv'
        filepath_raw = f'./report/raw_tables/raw_{filename}'
        filepath_summary = f'./report/summary_tables/summary_{filename}'
        report_tables['raw'].to_csv(filepath_raw)
        report_tables['summary'].to_csv(filepath_summary)

        # save information in worksheet
        country_txt = ' '.join(self.user_tab_data['countries'])
        period_txt = '-'.join(str(r) for r in self.user_tab_data['years'])
        index_txt = self.user_tab_data['index']
        row_data = [
            user_report_data['title'],
            user_report_data['author'],
            user_report_data['notes'],
            filepath_raw,
            filepath_summary,
            country_txt,
            period_txt,
            index_txt
        ]
        self.worksheet.append_row(row_data)

        print(GREEN)
        message_end = "saved in FAVOURITES successfully"
        print(f"{self.worksheet_name.capitalize()} {message_end}.\n")

    def display_all(self):
        """
        Displays all saved reports.
        """
        df = pd.DataFrame(self.worksheet.get_all_records())
        self.report_df = df

        if df.empty:
            print(YELLOW)
            print('There are no saved reports.')
            return 0

        else:
            print(GREEN)
            print(f'Loading saved {self.worksheet_name}s ...')

            reports_df = df[['title', 'author', 'notes']]
            table_to_show = reports_df
            table_to_show = table_to_show.applymap(
                lambda x: x[:17]+'..' if len(x) > 17 else x)
            table_headers = table_to_show.columns.insert(0, 'ID')

            print(WHITE)
            print(tabulate(
                table_to_show,
                headers=table_headers,
                tablefmt="outline"))

            return reports_df.shape[0]

    def display_one_report(self, report_id):
        """
        Displays a report based on the given report ID.

        Args:
            report_id(int): Report ID to be displayed.
        """
        print(GREEN)
        print(f'Loading the report of ID={report_id} ...')

        display_report_information(self.report_df, report_id)
        display_summary_table(self.report_df, report_id)
        display_raw_table(self.report_df, report_id)

    def delete_report(self, report_id=None):
        """
        Deletes all data related to the specified report (described
        by input parameters)

        Args:
            folder(str): Folder path of report tables.
            filename(str): Report title to be deleted.
            report_id: Report ID of report to be deleted.
        """

        print(GREEN)
        delete_obj = 's' if report_id is None else f" of ID={report_id}"
        print(f'Deleting report{delete_obj} ...')

        filename = self.report_df[['title']].iloc[report_id][0]
        empty_directory(
            folder='./report/raw_tables',
            filename=f"raw_{filename}.csv")
        empty_directory(
            folder='./report/summary_tables',
            filename=f"summary_{filename}.csv")
        delete_report_from_sheet(
            SHEET=self.SHEET,
            report_id=report_id)

        print(GREEN)
        print('Deleted successfully.')


def display_report_information(report_df, report_id):
    """
    Displays report information.

    Args:
        report_df(data frame): Data Frame of all reports
            and related information.
        report_id(int): Report ID to be displayed.
    """
    print(WHITE)
    print(f'Title: {report_df[["title"]].iloc[report_id][0]}')
    print(f'\nAuthor: {report_df[["author"]].iloc[report_id][0]}')
    print('\nReport specifications')
    print(f'  Country: {report_df[["country"]].iloc[report_id][0]}')
    print(f'  Time period: {report_df[["period"]].iloc[report_id][0]}')
    print(f'  Index: {report_df[["index"]].iloc[report_id][0]}')
    print(f'\nFindings: {report_df[["notes"]].iloc[report_id][0]}')


def display_summary_table(report_df, report_id):
    """
    Displays table of summary descriptive data.

    Args:
        report_df(data frame): Data Frame of all reports
            and related information.
        report_id(int): Report ID to be displayed.
    """
    print(f'\nDescriptive data summary')

    summary_table = pd.read_csv(
        report_df[['summary_table']].iloc[report_id][0],
        header=1,
        index_col=0)

    summary_table_col = summary_table.columns[2:].insert(0, 'iso_code')
    summary_table_col = summary_table_col.insert(1, 'country')

    print(tabulate(
        summary_table,
        headers=summary_table_col,
        tablefmt="outline"))


def display_raw_table(report_df, report_id):
    """
    Displays table of raw data.

    Args:
        report_df(data frame): Data Frame of all reports
            and related information.
        report_id(int): Report ID to be displayed.
    """
    print(f'\nRaw data')

    raw_table = pd.read_csv(
        report_df[['raw_table']].iloc[report_id][0],
        header=0,
        index_col=0)

    print(tabulate(
        raw_table,
        headers=raw_table.columns,
        tablefmt="outline"))
