def reporting_menu():
    print("\nYou are going to create a simple report.")
    print("The report contains a table with the information about countries and climate indices.")
    print("The programm navigates you to create such report.\n")

    while True:
        try:
            answer = input("Are you ready (y/n)?")[0].lower().strip()
            
            if answer=='y':
                print('you are about to create a report')
                break
            
            elif answer=='n':
                print('Oh, would')
                break

            else:
                raise ValueError(f"Only y/n is allowed, you wrote {answer}")




        except ValueError as e:
                print(f"Invalid data: {e}, please try again. \n")

    
        