import yaml
import os
import pandas as pd
from tabulate import tabulate


from revisport.helpers import empty_directory
from revisport.helpers import delete_report_from_sheet
from revisport.colors import *


class Contacts():
    def __init__(self, SHEET):
        self.SHEET = SHEET
        self.worksheet_name = 'contact'
        self.worksheet = SHEET.worksheet('contact')

    def send_message(
        self, first_name, last_name, email,	message):

        print(GREEN)
        print(f'Sending your message ...')

        contact_data = [
            first_name,
            last_name,
            email,
            message
        ]
        self.worksheet.append_row(contact_data)

        print(GREEN)
        print("Message sent successfully.\n")