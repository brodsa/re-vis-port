from tabulate import tabulate

import revisport as rvp 
from revisport import SHEET

def reporting_menu(input_data):
    """
    Wraps all functions within the reporting menue
    """
    print("\nYou are going to create a simple report.")
    print("The report contains a table with the information about EU countries and climate indices.")
    print("The programm navigates you to generate the report table.\n")

    while True:
        try:
            answer = input(
                "Are you ready (y - yes, continue / n - no, go back)? "
                )[0].lower().strip()

            if answer in ['y','n']:
                if answer=='n':
                    rvp.main_menu.welcome_menu()
                    rvp.main_menu.get_answer()
                else:
                    reporting_questions(input_data)
                break

            else:
                raise ValueError(f"Only y/n is allowed, you wrote {answer}")

        except (ValueError,IndexError) as e:
                print(f"Invalid input: {e}; please try again. \n")
        

    
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
    print(report_index)
      
    
def select_country(countries):
    """
    Aks user to enter countries in the form of iso codes.
    The answer is validated and corresponding error message displayed in case of invalid input.
    """
    print("\nSelect countries for which you want to the report.")
    print("\nEnter iso code of selected countries, use comma as a separator (iso1,iso2):")
    print(tabulate(countries, headers=['iso','country'],tablefmt="outline"))

    while True:
        selected_countries = input()
        countries_ls = [country.upper().strip() for country in selected_countries.split(',')]

        try:
            correct_countries = all([item in countries.country for item in countries_ls])

            if correct_countries:
                return countries_ls

            if countries_ls[-1] == '':
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
            selected_period_tx = input("Select a time period from years 2000 and 2020 (yyyy-yyyy):")
            selected_period_ls = [year.strip() for year in selected_period_tx.split('-')]
            correct_period = all([int(year) in years for year in selected_period_ls])

            if not correct_period:
                print('Year selection not in range (2000-2020); please try again.\n')

            elif len(selected_period_ls)==1 or selected_period_ls[0]== selected_period_ls[1]:
                print('Missing year for a valid range; please try again.\n')
            
            elif correct_period and len(selected_period_ls)== 2 and selected_period_ls[0]< selected_period_ls[1]:
                return selected_period_ls

            elif correct_period and len(selected_period_ls)== 2 and selected_period_ls[0]> selected_period_ls[1]:
                print('Invalid format, a lower bound is larger than an upper bound; please try again.\n')

            else:
                print('Invalid input.')

        except ValueError:
                print(f"You did not enter number or a valid range format; please try again. \n")  


def select_index(indices):
    print("\nPlease select an index from the list bellow:")
    print("1: GDP")
    print("2: Population")
    print("2: CO2 emmission (million tonnes)")
    print("3: Methane emmission (million tonnes of carbon dioxide-equivalents)")
    print("4: Energy consumption (terawatt-hours per year)")
    print("5: Greenhouse gas emissions (million tonnes of carbon dioxide-equivalents)")

    while True:
        try:
            answer = int(input("\nEnter your choice: ").strip())
        except ValueError:
            print("You did not enter a number")
            continue
        if answer in [1,2,3,4,5]:
            return answer
        else:
            print("Invalid choice, please enter a number from 1 to 5!")



