#variables
day_in_week = 7 


min_number_month_days = 28
max_number_month_days = 31

min_number_week_days = 1
max_number_week_days = 7

#prompts
prompts_days_in_month= "How many days are in the month? "
prompt_first_day = "What day of the week does the month start on? (Sun=1, Mon=2, ..., Sat= 7) "
prompt_error_handling = "Enter a value between "



def get_days_in_month():
    """function which gets the number of days in a month from users and preforms error handling """   
    while True:
        try:
            days_in_month = int(input( prompts_days_in_month))
            #user can only input a number within a specific range
            if min_number_month_days <= days_in_month <= max_number_month_days:
                #passed into calender_printer()
                return days_in_month
            else:
                print(f"{prompt_error_handling} {min_number_month_days} to {max_number_month_days}")
        #users can't input non-integers        
        except ValueError:
            print(f"{prompt_error_handling} {min_number_month_days} to {max_number_month_days}")
        

def get_days_in_week():
    """function which gets the day of the week the month starts on and preforms error handling """               
    while True:
        try:
            first_day  = int(input(prompt_first_day))
            if min_number_week_days <= first_day  <= max_number_week_days :
                return first_day
            else:
                print(f"{prompt_error_handling} {min_number_week_days} to {max_number_week_days}")
        except ValueError:
            print(f"{prompt_error_handling} {min_number_week_days} to {max_number_week_days}")

        


def calender_printer(days_in_month, first_day):
    """function which prints a calender""" 
    calender_title = [" S", "M" , "T", "W", "T", "F", "S"]
    print("  ".join(calender_title)) 

         #makes spaces/gaps based on first day of month
    for i in range(first_day-1):
        print("   ", end="") # end = "" ensure it prints on same line

        #takes number of days in the month
    for i in range(1, days_in_month+1): 
        print(f"{i:2}", end=" ") 

             #new line after every 7th day (including spaces)
        if (i + first_day - 1) % day_in_week == 0:
            print()  # newline

    return calender_title

#calls function
days_in_month = get_days_in_month()
first_day = get_days_in_week()
calender_printer(days_in_month, first_day)