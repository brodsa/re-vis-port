# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


from revisport import helpers
from revisport import SHEET

# data preparation
# data = helpers.prepare_data(SHEET,'owid-co2-data','filter')
# print(data.head())


def main_menu():
    # welcome message
    print("Welcome to ReVisPort!\n")
    print("Your command line reporting tool is ready for you to use.\n")
    print("Please reade carefully and follow the instructions.\n")
    print("\n")

    # welcome qustion
    print("Select the item from the menu:")
    print("1: Reporting")
    print("2: Favourite")
    print("3: References")

    
    answer = input()

    print(f"You have selected {answer}")





main_menu()