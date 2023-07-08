import yaml
import os
import pandas as pd
from tabulate import tabulate


from revisport.helpers import empty_directory
from revisport.helpers import delete_report_from_sheet
from revisport.colors import *


class Reports():
    def __init__(self, SHEET):
        self.SHEET = SHEET
        self.worksheet_name = 'report'
        self.worksheet = SHEET.worksheet('report')

    def save_new_report(self, user_tab_data, report_tables, user_report_data):

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
        period_txt = '-'.join(str(item) for item in self.user_tab_data['years'])
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
        df = pd.DataFrame(self.worksheet.get_all_records())
        self.report_df = df
        if df.empty:
            print(YELLOW)
            print('There are no saved reports.')
            return 0
        else:
            print(GREEN)
            print(f'Loading saved {self.worksheet_name}s ...')
            reports_df = df[['title', 'author', 'country', 'period', 'index']]
            print(WHITE)
            table_headers = reports_df.columns.insert(0, 'ID')
            print(tabulate(
                reports_df,
                headers=table_headers,
                tablefmt="outline"))
            return reports_df.shape[0]

    def display_one_report(self, report_id):
        self.r_id = report_id

        print(GREEN)
        print(f'Loading the report of ID={self.r_id} ...')

        os.system('clear')
        print(WHITE)
        print(f'Title: {self.report_df[["title"]].iloc[report_id][0]}')
        print(f'\nAuthor: {self.report_df[["author"]].iloc[report_id][0]}')
        print('\nReport specifications')
        print(f'  Country: {self.report_df[["country"]].iloc[report_id][0]}')
        print(
            f'  Time period: {self.report_df[["period"]].iloc[self.r_id][0]}')
        print(f'  Index: {self.report_df[["index"]].iloc[report_id][0]}')
        print(f'\nFindings: {self.report_df[["notes"]].iloc[report_id][0]}')

        print(f'\nDescriptive data summary')
        summary_table = pd.read_csv(
            self.report_df[['summary_table']].iloc[report_id][0],
            header=1,
            index_col=0)
        summary_table_col = summary_table.columns[2:].insert(0, 'iso_code')
        summary_table_col = summary_table_col.insert(1, 'country')
        print(tabulate(
            summary_table,
            headers=summary_table_col,
            tablefmt="outline"))

        print(f'\nRaw data')
        raw_table = pd.read_csv(
            self.report_df[['raw_table']].iloc[report_id][0],
            header=0,
            index_col=0)
        print(tabulate(
            raw_table,
            headers=raw_table.columns,
            tablefmt="outline"))

    def delete_report(self, report_id=None):
        """
        Deletes all data related to the specified report (described
        by input paramters)

        Vars:
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