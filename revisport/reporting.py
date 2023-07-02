from tabulate import tabulate

import revisport as rvp 
from revisport import SHEET

def reporting_menu(input_data):
    """
    Wraps all functions within the reporting menue
    """
    print("\nYou are going to create a simple report.")
    print("The report contains a table with the information about EU countries and climate indices.")
    print("The programm navigates you to generate the report.")
    print("Are you ready?")
    print("1: yes, continue creating the report")
    print("0: no; go back to MAIN MENU")
   
    while True:
        try:
            answer = int(input("Enter your choice: ").strip())
        except ValueError:
            print("You did not enter a number")
            continue

        if answer == 1:
            while True:
                report_input = reporting_questions(input_data)
                save_input = save_choices(report_input,input_data)
                print(save_input)
                if save_input:
                    return
        elif answer == 0:
            # back to main menu
            rvp.main_menu.main_menu(input_data)
            break
        else:
            print("Invalid choice, please enter a number 1 or 2!")
        
        # reporting_menu(input_data)

    
def reporting_questions(input_data):
    """
    Displays all question user has to answer in order to generate a report
    """

    #ask for countries 
    report_countries = select_country(input_data['countries'])

    # ask for time period
    report_years = select_time_period(input_data['years'])
    
    # ask for index
    report_index = select_index(input_data['indices'])

    # wrap and save the answer into dictionary
    report_input = dict()
    report_input['countries'] = report_countries
    report_input['years'] = report_years
    report_input['index'] = report_index
    
    return report_input
      
    
def select_country(countries):
    """
    Asks user to enter countries in the form of iso codes.
    The answer is validated and corresponding error message displayed in case of invalid input.
    """
    print("\nSelect countries for which you want to the report.")
    print("Enter iso code of selected countries, use comma as a separator (iso1,iso2):")
    print(tabulate(countries, headers=['iso','country'],tablefmt="outline"))

    while True:
        selected_countries = input('Enter your choice:')
        countries_ls = [country.upper().strip() for country in selected_countries.split(',')]

        try:
            correct_countries = all([item in countries.country for item in countries_ls])

            if correct_countries:
                return countries_ls

            elif countries_ls[-1] == '':
                raise ValueError(f"Missing country after , or no country specified at all")

            else:
                raise ValueError(
                    f"Only valid ISO codes or comma seperator are allowed, you wrote {selected_countries}"
                    )
        except (ValueError,IndexError) as e:
            print(f"Invalid input: {e}; please try again.\n") 


def select_time_period(years):
    """
    Asks user to enter time period. 
    The answer is validated and corresponding error message displayed in case of invalid input.
    """
    while True:
        try: 
            print("\nSelect a time period from years 2000 and 2020 (yyyy-yyyy).")
            selected_period_txt = input("Enter your choice:")
            selected_period_ls = [year.strip() for year in selected_period_txt.split('-')]
            correct_period = all([int(year) in years for year in selected_period_ls])

            if not correct_period:
                print('Year selection is not in range (2000-2020); please try again.')

            elif len(selected_period_ls)==1 or selected_period_ls[0]== selected_period_ls[1]:
                print('Missing year for a valid range; please try again.')
            
            elif correct_period and len(selected_period_ls)== 2 and selected_period_ls[0]< selected_period_ls[1]:
                return selected_period_ls

            elif correct_period and len(selected_period_ls)== 2 and selected_period_ls[0]> selected_period_ls[1]:
                print('Invalid format, a lower bound is larger than an upper bound; please try again.')

            else:
                print('Invalid input.')

        except ValueError:
                print(f"You did not enter number nor a valid range format; please try again.")  


def select_index(indices):
    print("\nPlease select an index from the list bellow:")
    print("1: GDP")
    print("2: Population")
    print("3: CO2 emmission (million tonnes)")
    print("4: Methane emmission (million tonnes of carbon dioxide-equivalents)")
    print("5: Energy consumption (terawatt-hours per year)")
    print("6: Greenhouse gas emissions (million tonnes of carbon dioxide-equivalents)")

    while True:
        try:
            answer = int(input("Enter your choice: ").strip())
        except ValueError:
            print("You did not enter a number")
            continue
        if answer in list(range(1,7)):
            return answer
        else:
            print("Invalid choice, please enter a number from 1 to 6!")


def save_choices(report_input,input_data):
    print(f'\nSave the choices: {report_input} ?')
    print("1: Yes, continue to display the report table.")
    print("2: No, make new changes.")
    print("0: Go back to the MAIN MENU")

    while True:
        try:
            answer = int(input("Enter your choice: ").strip())
            print(answer, answer == 1)
        except ValueError:
            print("You did not enter a number")
            continue

        if answer == 1:
            display_report(report_input)
            return True
        elif answer == 2:
            return False
        else:
            print("Invalid choice, please enter a number from 0 to 1!")





def display_report(report_input,input_data):
    """
    report_input = user_imput
    """
    print(report_input)
    indices = report_input.indices.iloc[report_input.index] + ['iso_code','country','year']
    report_data = input_data.data[[report_input.indices.iloc[report_input.index]]]
    return 