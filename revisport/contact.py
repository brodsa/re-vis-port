import os

import revisport as rvp
from revisport.helpers import question_to_save
from revisport.colors import WHITE, CYAN, PURPLE, YELLOW, GREEN
from revisport.Contacts import Contacts



def contact_menu(SHEET,input_data):
    """
    Wraps all functions within the contact menu.
    """
    os.system('clear')
    print(WHITE)
    print('-------')
    print('CONTACT')
    print('-------')
    print(
        "We are happy to hear from your.",
        "We appritate any feedback or suggestions for enhancement on ReVisPort")
    print(CYAN)
    print("Please select from the menu bellow?")
    print(" 1: Send a message.")
    print(" 0: Go back to HOME MENU.")

    while True:
        try:
            print(PURPLE +"Enter your choice: " + WHITE, end='')
            answer = int(input().strip())
        except ValueError:
            print(YELLOW + "You did not enter a number")
            continue

        if answer == 1:
            while True:
                contact_data = ask_contact_details()
                send = send_user_contact(SHEET, contact_data)
                if send:
                    input(CYAN + 'Press any key to continue to HOME MENU ...')
                    return
        elif answer == 0:
           rvp.home.main_menu(input_data)
           return
        else:
            print(YELLOW + "Invalid choice, please enter a number 0 or 1!\n")
    return


def ask_contact_details():
    """
    Aks user contact details and message to send

    Returns:
        contact_data(dict): All contact information.
    """
    print(CYAN)
    print("Please fill in the following to contact us.")
    # first name
    print(PURPLE + "Enter your first name: " + WHITE, end='')
    first_name = input()
    # last name
    print(PURPLE + "Enter your last name: " + WHITE, end='')
    last_name = input()
    # email
    while True:
        print(PURPLE + "Enter email*: " + WHITE, end='')
        email = input()
        condition_dot = '.' in email and email[-1]!='.'
        if '@' not in email:
            print(YELLOW + 'Invalid email: missing @, please try again.\n')
        elif not condition_dot:
            print(YELLOW + 'Invalid email: missing domain, please try again.\n')
        elif condition_dot:
            break
        else:
            print(YELLOW + 'Invalid email, please try again.\n')
    # message
    while True:
        print(PURPLE + "Write your message*: " + WHITE, end='')
        message = input()
        condition_empty = all([item == ' ' for item in message])
        if len(message)== 0 or condition_empty:
            print(YELLOW + 'Empty message, please try again.\n')
        else:
            break

    concat_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'message': message
    }

    return concat_data

def send_user_contact(SHEET, contact_data):
    """
    Asks user if the message should be save or if the information
    should be discarded.
    """
    print(CYAN)
    question_to_save(
        'keep the provided information',
        ' sending the message',
        'make changes')

    while True:
        try:
            print(PURPLE + "Enter your choice: " + WHITE, end='')
            answer = int(input().strip())
        except ValueError:
            print(YELLOW + "You did not enter a number.\n")
            continue
        
        if answer == 1:
            contact_worksheet = Contacts(SHEET)
            contact_worksheet.send_message(
                contact_data['first_name'],
                contact_data['last_name'],
                contact_data['email'],
                contact_data['message'])
            return True
        elif answer == 2:
            print(GREEN)
            print('Discarding entries ...\n')
            return False
        else:
            print(YELLOW + "Invalid choice, please enter a number 1 or 2!\n")
