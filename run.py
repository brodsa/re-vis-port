# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from revisport import helpers
from revisport import SHEET
from revisport.main_menu import welcome_message 
from revisport.main_menu import welcome_menu 
from revisport.main_menu import get_answer

# data preparation
# data = helpers.prepare_data(SHEET,'owid-co2-data','filter')
# print(data.head())


def main_menu():
    # print the welcome message
    welcome_message()

    # print the menu choices
    welcome_menu()

    # select from the menu
    get_answer()
 


main_menu()