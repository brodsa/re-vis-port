# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('re-vis-port')

# owid_sheet = SHEET.worksheet('owid-co2-data')
# owid = owid_sheet.get_all_values()
# owid_header = owid.pop(0)
# owid_df = pd.DataFrame(data = owid, columns = owid_header)
# print(owid_df.head())


def get_data(sheetname):
    """
    Get data from the given worksheet
    """
    worksheet = SHEET.worksheet(sheetname)
    df = pd.DataFrame(worksheet.get_all_records())
    return df




owid_df = get_data('owid-co2-data')
filter_df = get_data('filter')
data_tmp = owid_df[owid_df.country.isin(filter_df.country)]
indices = [ind for ind in filter_df.ind if ind !='']
data = data_tmp[indices]
print(owid_df.year.between(filter_df.year[0],filter_df.year[1]))
