# Step 1: First Import all the libraries used in this program

import sys
from datetime import date 

# Problem 1: Write a Python program that reads two command-line inputs, month (between 1 and 12) 
# and year (between 1 and 9999), and produces the calendar for the specified month in the 
# specified year. 

num_of_arguements = len(sys.argv) 

if num_of_arguements == 3:

     # Step 2: Use a try and error block to prevent any potential errors from crashing the program

   try:

        # Step 3: Let's assign command line argument indexes to month and year

        month = int(sys.argv[1])
        year = int(sys.argv[2])

        # Step 4: Let's check if the year and month input are within an acceptable range

        if not (1 <= month <= 12):
            print("Month must be in between 1 and 12")
        elif not (1 <= year <= 9999):
            print("Year must be in between 1 and 9999")
        else:
            # Step 5: If the month and year are within an acceptable range, then proceed with the program

            month_name = ""
            num_days = 0

            # Step 6: Let's determine if a year is a leap year for printing the correct number of days for February

            if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
                is_leap = True
            else:
                is_leap = False

            # Step 7: Let's determine the number of days in each month

            if month == 1:
                month_name = "January"
                num_days = 31
            elif month == 2:
                month_name = "February"
                if is_leap:
                    num_days = 29
                else:
                    num_days = 28
            elif month == 3:
                month_name = "March"
                num_days = 31
            elif month == 4:
                month_name = "April"
                num_days = 30
            elif month == 5:
                month_name = "May"
                num_days = 31
            elif month == 6:
                month_name = "June"
                num_days = 30
            elif month == 7:
                month_name = "July"
                num_days = 31
            elif month == 8:
                month_name = "August"
                num_days = 31
            elif month == 9:
                month_name = "September"
                num_days = 30
            elif month == 10:
                month_name = "October"
                num_days = 31
            elif month == 11:
                month_name = "November"
                num_days = 30
            elif month == 12:
                month_name = "December"
                num_days = 31

            # Step 8: Let's determine the day of the week for the first of the month

            d = date(year, month, 1)
            start_day_of_week = (d.weekday() + 1) % 7 

            # STEP 9: Print a blank line to separate months
            print() 

            # Step 10: Center the header (Month Year)
            # The total width of the calendar is 20 characters

            header = f"{month_name} {year}"
            padding = (20 - len(header)) // 2
            print(" " * padding + header)

            # Step 11: Print the days of the week header
            print("Su Mo Tu We Th Fr Sa")

            # Step 12: Print the leading spaces for the first week
            print("   " * start_day_of_week, end="")

            # Step 13: Loop through all the days in the month and print them
            for day in range(1, num_days + 1):
                print(f"{day: >2} ", end="")

                # Step 14: After printing a day, check if it was a Saturday to print a new line to start the next week
                if (start_day_of_week + day) % 7 == 0:
                    print()

    # Step 15: Enter the except block so that the program can deal with errors

   except IndexError:
        print("Please provide a year as a command line argument.")
   except ValueError:
        print(f"Invalid literal for int(): '{sys.argv[1]}'")
   except Exception as e:
        print(str(e))
    
# Problem 2: Modify your program also to accept just the year as a command-line parameter and print the calendar for the entire year.

elif num_of_arguements == 2:
    
    # Step 2: Use a try and error block to prevent any potential errors from crashing the program

    try:
        # Step 3: Let's assign command line argument indexes to year

        year = int(sys.argv[1])

        # Step 4: Let's check if the year input is within an acceptable range

        if not (1 <= year <= 9999):
            print(f"year {year} is out of range")
        else:
            # Step 5: Run the loop for each month

            for month in range(1, 13):
                month_name = ""
                num_days = 0

                # Step 6: Let's determine if a year is a leap year for printing the correct number of days for February

                if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
                    is_leap = True
                else:
                    is_leap = False

                # Step 7: Let's determine the number of days in each month

                if month == 1:
                    month_name = "January"
                    num_days = 31
                elif month == 2:
                    month_name = "February"
                    if is_leap:
                        num_days = 29
                    else:
                        num_days = 28
                elif month == 3:
                    month_name = "March"
                    num_days = 31
                elif month == 4:
                    month_name = "April"
                    num_days = 30
                elif month == 5:
                    month_name = "May"
                    num_days = 31
                elif month == 6:
                    month_name = "June"
                    num_days = 30
                elif month == 7:
                    month_name = "July"
                    num_days = 31
                elif month == 8:
                    month_name = "August"
                    num_days = 31
                elif month == 9:
                    month_name = "September"
                    num_days = 30
                elif month == 10:
                    month_name = "October"
                    num_days = 31
                elif month == 11:
                    month_name = "November"
                    num_days = 30
                elif month == 12:
                    month_name = "December"
                    num_days = 31

                # Step 8: Let's determine the day of the week for the first of the month

                d = date(year, month, 1)
                start_day_of_week = (d.weekday() + 1) % 7 

                # STEP 9: Print a blank line to separate months
                print() 

                # Step 10: Center the header (Month Year)
                # The total width of the calendar is 20 characters

                header = f"{month_name} {year}"
                padding = (20 - len(header)) // 2
                print(" " * padding + header)

                # Step 11: Print the days of the week header
                print("Su Mo Tu We Th Fr Sa")

                # Step 12: Print the leading spaces for the first week
                print("   " * start_day_of_week, end="")

                # Step 13: Loop through all the days in the month and print them
                for day in range(1, num_days + 1):
                    print(f"{day: >2} ", end="")

                    # Step 14: After printing a day, check if it was a Saturday to print a new line to start the next week
                    if (start_day_of_week + day) % 7 == 0:
                        print()
            
                # Step 15: After the loop, print one final newline if the last day was not a Saturday to make sure the next month's header starts on a clean new line.
                if (start_day_of_week + num_days) % 7 != 0:
                    print()

    # Step 16: Enter the except block so that the program can deal with errors

    except IndexError:
        print("Please provide a year as a command line argument.")
    except ValueError:
        print(f"Invalid literal for int(): '{sys.argv[1]}'")
    except Exception as e:
        print(str(e))
