import pandas as pd
import os, shutil

def get_data_from_worksheet(SHEET,sheetname):
    """
    Get data from the given worksheet
    """
    worksheet = SHEET.worksheet(sheetname)
    df = pd.DataFrame(worksheet.get_all_records())
    return df


def prepare_data(SHEET,*sheetnames):
    """
    Prepare data for reporting
    """
    # get data from worksheets
    sheets = [argv for argv in sheetnames]
    owid_df = get_data_from_worksheet(SHEET,sheets[0])  # 'owid-co2-data'
    filter_df = get_data_from_worksheet(SHEET,sheets[1])  # 'filter'

    # filter out all data
    data_tmp = owid_df[owid_df.country.isin(filter_df.country) & owid_df.year.between(filter_df.year[0],filter_df.year[1])]
    filter_columns = [ind for ind in filter_df.ind if ind !='']  # get rid off o missing valaus, represented as empty string
    
    # prepare output data
    data = data_tmp[filter_columns]
    countries = data[['iso_code','country']].drop_duplicates()
    countries = countries.set_index('iso_code')
    years = list(range(filter_df.year[0],filter_df.year[1]+1))
    indices = pd.DataFrame(filter_columns[3:],columns=['ind'])

    input_data = dict()
    input_data["data"] = data
    input_data["countries"] = countries
    input_data["years"] = years
    input_data["indices"] = indices

    return input_data

def question_to_save(
    txt_question = None,
    txt_1='',
    txt_2='make changes'):
    if txt_question is None:
        txt_question = 'save your choices'
    print(f'Would you like to {txt_question}?')
    print(f" 1: Yes, continue{txt_1}.")
    print(f" 2: No, {txt_2}.")
    
def update_worksheet(SHEET, sheetname, row_data):

    worksheet_report = SHEET.worksheet('report')
    worksheet_report.append_row(row_data)

def empty_directory(folder,filename=None):
    """
    Empties directory based on the directory path.
    Taken from https://stackoverflow.com/
    questions/185936/how-to-delete-the-contents
    -of-a-folder

    Vars:
        folder(str): Folder path of report tables.
        filnames(str): List of file to be deleted
    
    """
    # for entire folder
    if filename is None:
        filenames = os.listdir(folder)
    else:
        filenames = [filename]

    for file_name in filenames:
        file_path = os.path.join(folder, file_name)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: f{e}')


def delete_report_from_sheet(SHEET, report_id = None):
    """
    Deletes report information from the sheet.

    Vars:
        SHEET(obj): Google sheet object
        report_id(int): Report ID, in case no
        specification the entire sheet is cleared.
    """
    
    worksheet = SHEET.worksheet('report')
    if report_id is None:
        row_n = worksheet.row_count
        if row_n > 1:
            i_start = 2
            i_end = row_n
    else:
        i_start= report_id + 2
        i_end = None

    worksheet.delete_rows(i_start,i_end)







