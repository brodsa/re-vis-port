import os

import revisport as rvp
from revisport.helpers import question_to_save
from revisport.colors import WHITE, CYAN, PURPLE, YELLOW, GREEN


def contact_menu(SHEET,input_data):
    """
    Wraps all functions within the contact menu.
    
    Args:
        SHEET(obj): Google sheet object
        input_data(data frame): A data frame with climate input data
        as a input parameter for main_menu()

    """
    os.system('clear')
    print(WHITE)
    print('-------')
    print('CONTACT')
    print('-------')
    print(
        "We are happy to hear from your.",
        "We appreciate any feedback or suggestions for",
        "\nenhancement on ReVisPort")
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
                    input(CYAN + 'Press any key to return HOME  ...')
                    os.system('clear')
                    return
        elif answer == 0:
            os.system('clear')
            rvp.home.main_menu(SHEET,input_data)
            return
        else:
            print(YELLOW + "Invalid choice, please enter a number 0 or 1!\n")
    return


def ask_contact_details():
    """
    Asks a user for contact details 
    and message to send.

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

    # email address
    email = ask_contact_email()

    # message
    message = ask_write_message()

    concat_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'message': message
    }

    return concat_data

def ask_contact_email():
    """
    Asks for a contact email and validates 
    the user input.

    Returns:
        email(str): A valid email address.
    """

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

    return email


def ask_write_message():
    """
    Asks to write a message and validates the input.

    Returns:
        message(str): a message which is a non empty string.
    """
    while True:
        print(PURPLE + "Write your message*: " + WHITE, end='')
        message = input()
        condition_empty = all([item == ' ' for item in message])
        if len(message)== 0 or condition_empty:
            print(YELLOW + 'Empty message, please try again.\n')
        else:
            break

    return message


def send_user_contact(SHEET, contact_data):
    """
    Asks user if the message should be saved or if the information
    should be discarded.

    Args:
        SHEET(obj): Google sheet object.
        contact_data(data frame): Data frame with all contact form data,
        filled by a user.
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


class Contacts():
    """
    Contacts is an object describing all messages and related information
    filled in the contact form by user.
    """
    def __init__(self, SHEET):
        """
        Initializes the object Contacts.
        Vars:
            SHEET(obj): Google sheet object.
        """
        self.SHEET = SHEET
        self.worksheet_name = 'contact'
        self.worksheet = SHEET.worksheet('contact')

    def send_message(self, f_name, l_name, email,message):
        """
        Sends the contact message in a way of saving 
        the provided information into Google worksheet.
        """
        print(GREEN)
        print("Sending your message ...")

        contact_data = [
            f_name,
            l_name,
            email,
            message
        ]
        self.worksheet.append_row(contact_data)

        print(GREEN)
        print("Message sent successfully.\n")