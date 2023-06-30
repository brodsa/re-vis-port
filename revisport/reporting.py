from tabulate import tabulate

import revisport as rvp 
from revisport import SHEET

def reporting_menu(data,countries):
    print("\nYou are going to create a simple report.")
    print("The report contains a table with the information about EU countries and climate indices.")
    print("The programm navigates you to generate the report table.\n")

    while True:
        try:
            answer = input(
                "Are you ready (y - yes, continue / n - no, go back)?"
                )[0].lower().strip()

            if answer in ['y','n']:
                if answer=='n':
                    rvp.main_menu.welcome_menu()
                    rvp.main_menu.get_answer()
                else:
                    reporting_questions(data,countries)
                break

            else:
                raise ValueError(f"Only y/n is allowed, you wrote {answer}")


        except (ValueError,IndexError) as e:
                print(f"Invalid input: {e}; please try again. \n")
        

    
def reporting_questions(data,countries):
    print("Select ISO code of an EU country for which you wish to create a report!")
    print(tabulate(countries, headers=['iso','country'],tablefmt="outline"))
    
        