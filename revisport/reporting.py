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
                "Are you ready (y - yes, continue / n - no, go back)? "
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

    report_countries = select_country(countries)

    print(report_countries)
   




    
    
def select_country(countries):
    print("\nSelect countries for which you want to the report.")
    print("\nType iso code of selected countries and use comma as a separator, i.e. LVA,AUT")
    print(tabulate(countries, headers=['iso','country'],tablefmt="outline"))

    while True:
        selected_countries = input()
        countries_ls = [country.upper().strip() for country in selected_countries.split(',')]

        try:
            correct_countries = all([item in countries.country for item in countries_ls])

            if correct_countries:
                return countries_ls

            if countries_ls[-1] == '':
                raise ValueError(f"Missing country after ,")

            else:
                raise ValueError(
                    f"Only valid ISO codes or comma seperator are allowed, you wrote {selected_countries}"
                    )
        except (ValueError,IndexError) as e:
            print(f"Invalid input: {e}; please try again. \n") 
