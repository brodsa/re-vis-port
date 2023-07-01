# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from revisport.main_menu import welcome_message
from revisport.main_menu import welcome_load_data 
from revisport.main_menu import welcome_menu 
from revisport.main_menu import get_answer

def main_menu():
    # print the welcome message
    welcome_message()

    # load data
    input_data = welcome_load_data()

    # print the menu choices
    welcome_menu()


    # select from the menu
    get_answer(input_data)

 


main_menu()
