# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from revisport.main_menu import welcome_message
from revisport.main_menu import welcome_load_data 
from revisport.main_menu import main_menu 
from revisport.favourite import empty_favourite

# from revisport.main_menu import select_from_main_menu

def main():
    # empty saved reports
    empty_favourite()

    # display the introduction text only at the begining
    welcome_message()

    # load data only once when starting the program
    input_data = welcome_load_data()

    # starts the actuall programm
    while True:
        main_menu(input_data)

 


main()
