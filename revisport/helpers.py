import pandas as pd

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
    indices = [ind for ind in filter_df.ind if ind !='']  # get rid off o missing valaus, represented as empty string
    
    data = data_tmp[indices]
    countries = data[['iso_code','country']].drop_duplicates()
    countries = countries.set_index(range(0,len(filter_df.country)))

    return False, countries