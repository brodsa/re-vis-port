import os
import shutil

import pandas as pd


def get_data_from_worksheet(SHEET, sheetname):
    """
    Gets data from the given worksheet

    Args:
        SHEET(obj): Google sheet object
        sheetname(str): Name of worksheet to get data from.

    Returns:
        df(dataframe): dataframe with data stored in worksheet

    """
    worksheet = SHEET.worksheet(sheetname)
    df = pd.DataFrame(worksheet.get_all_records())
    return df


def prepare_data(SHEET, *sheetnames):
    """
    Prepares data for reporting. Data are stored
    in two worksheets.

    Args:
        SHEET(obj): Google sheet object
        sheetnames(args*): Name of worksheets to get data from.

    Returns:
        input_data(dataframe): Dataframe of data which are basis for
        creating report.
    """
    # get data from worksheets
    sheets = [argv for argv in sheetnames]
    owid_df = get_data_from_worksheet(SHEET, sheets[0])  # 'owid-co2-data'
    filter_df = get_data_from_worksheet(SHEET, sheets[1])  # 'filter'

    # filter out all data
    filter_country = owid_df.country.isin(filter_df.country)
    filter_year = owid_df.year.between(filter_df.year[0], filter_df.year[1])
    data_tmp = owid_df[filter_country & filter_year]
    # get rid off o missing valaus, represented as empty string
    filter_columns = [ind for ind in filter_df.ind if ind != '']

    # prepare output data
    data = data_tmp[filter_columns]
    countries = data[['iso_code', 'country']].drop_duplicates()
    countries = countries.set_index('iso_code')
    years = list(range(filter_df.year[0], filter_df.year[1]+1))
    indices = pd.DataFrame(filter_columns[3:], columns=['ind'])

    input_data = dict()
    input_data["data"] = data
    input_data["countries"] = countries
    input_data["years"] = years
    input_data["indices"] = indices

    return input_data


def question_to_save(txt_question=None, txt_1='', txt_2='make changes'):
    """
    Prints questions to answer with two possible choices,
    yes and no. The text for the choices can be adjusted.

    Args:
        txt_question(str): Question text.
        txt_1(str): Text to the yes answer.
        txt_2(str): Text to the no answer.
    """

    if txt_question is None:
        txt_question = 'save your choices'
    print(f'Would you like to {txt_question}?')
    print(f" 1: Yes, continue{txt_1}.")
    print(f" 2: No, {txt_2}.")


def update_worksheet(SHEET, sheetname, row_data):
    """
    Inserts a new line of data in the given worksheet.

    Args:
        SHEET(obj): Google sheet object.
        sheetname(str): Name of the worsheet to insert data.
        row_data(ls): New data to be inserted.
    """
    worksheet_report = SHEET.worksheet('report')
    worksheet_report.append_row(row_data)


def empty_directory(folder, filename=None):
    """
    Empties directory based on the directory path.
    Taken from https://stackoverflow.com/
    questions/185936/how-to-delete-the-contents
    -of-a-folder

    Args:
        folder(str): Folder path of report tables.
        filnames(str): List of file to be deleted.
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


def delete_report_from_sheet(SHEET, report_id=None):
    """
    Deletes report information from the sheet.

    Args:
        SHEET(obj): Google sheet object.
        report_id(int): Report ID, in case no
        specification the entire sheet is cleared.
    """
    worksheet = SHEET.worksheet('report')
    # no id specified means delete all data
    if report_id is None:
        row_n = worksheet.row_count
        if row_n > 1:
            i_start = 2
            i_end = row_n
    # delete a row with a specified ID
    else:
        i_start = report_id + 2
        i_end = None

    worksheet.delete_rows(i_start, i_end)
