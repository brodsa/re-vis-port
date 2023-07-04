import pandas as pd
from tabulate import tabulate

import revisport.helpers as rvp_helpers

class Reports():
    def __init__(self,SHEET):
        self.SHEET = SHEET
        self.worksheet_name = 'report'
        self.worksheet = SHEET.worksheet('report')

    def save_new_report(self,user_table_data,report_tables,user_report_data):
        
        self.user_table_data = user_table_data
        self.report_tables = report_tables
        self.user_report_data = user_report_data

        print(f'\nSaving {self.worksheet_name} ...')

        # save tables into csv
        filename = user_report_data['title'].replace(' ','_') + '.csv'
        filepath_raw = f'./report/raw_tables/raw_{filename}'
        filepath_summary = f'./report/summary_tables/summary_{filename}'
        report_tables['raw'].to_csv(filepath_raw)
        report_tables['summary'].to_csv(filepath_summary)
        
        # save information in worksheet
        country_txt = ' '.join(user_table_data['countries'])
        period_txt = '-'.join(str(item) for item in user_table_data['years'])
        index_txt = user_table_data['index']
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
            
        print(f"\n{self.worksheet_name.capitalize()} saved successfully.\n")

    def display_all(self):
        print(f'Loading {self.worksheet_name} ...')
        df = pd.DataFrame(self.worksheet.get_all_records())
        reports_df = df[['title','author','country','period','index']]
        print(tabulate(reports_df, headers=reports_df.columns, tablefmt="outline"))

    def display_one_report(self):
        print('\n Display a report')
        
    def modify_report_information(self):
        print('Update report')

    def delete_one_report(self):
        print('Delete report')