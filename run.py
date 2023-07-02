# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from revisport.main_menu import welcome_message
from revisport.main_menu import welcome_load_data 
from revisport.main_menu import main_menu 
# from revisport.main_menu import select_from_main_menu

def main():
    # display only at the begining
    # print the welcome message
    welcome_message()

    # load data
    input_data = welcome_load_data()

    # display in case of maine 
    # print the menu choices
    main_menu(input_data)

 


main()
