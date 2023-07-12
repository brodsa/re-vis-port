import yaml
import os
import pandas as pd
from tabulate import tabulate


from revisport.helpers import empty_directory
from revisport.helpers import delete_report_from_sheet
from revisport.colors import *


class Contacts():
    """
    Contacts is an object describing all messages and related information
    filled in contact form by user.
    """
    def __init__(self, SHEET):
        """
        To initialize the object the Google sheet object must be 
        given as an input parameter. 
        """
        self.SHEET = SHEET
        self.worksheet_name = 'contact'
        self.worksheet = SHEET.worksheet('contact')

    def send_message(self, f_name, l_name, email,message):
        """
        Method to send the contact message. 
        The information are saved into Google Sheet
        """
        print(GREEN)
        print(f'Sending your message ...')

        contact_data = [
            f_name,
            l_name,
            email,
            message
        ]
        self.worksheet.append_row(contact_data)

        print(GREEN)
        print("Message sent successfully.\n")
        