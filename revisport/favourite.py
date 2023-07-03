from revisport.helpers import empty_directory
from revisport.helpers import empty_report_sheet
from revisport import SHEET

def empty_favourite():
    empty_directory('./report/raw_tables')
    empty_directory('./report/summary_tables')
    empty_report_sheet(SHEET,sheetname='report')