# ---------------------------------------------------------------------
# Defined variables and prompts at the beginning of the program
#  -> make the code flexible if prompts or values changed changed
# ---------------------------------------------------------------------

# Values
day_in_week = 7
min_number_month_days = 28
max_number_month_days = 31
min_number_week_days = 1
max_number_week_days = 7

# Prompts
prompts_days_in_month= "How many days are in the month? "
prompt_first_day = "What day of the week does the month start on? (Sun=1, Mon=2, ..., Sat= 7) "

prompt_error_handling_month = f"Enter a value between {min_number_month_days} to {max_number_month_days}"
prompt_error_handling_week = f"Enter a value between {min_number_week_days} to {max_number_week_days}"

# ---------------------------------------------------------------------
# FUNCTION: Get number of days in month
# ---------------------------------------------------------------------

def get_days_in_month():

    """

    Get the number of days in a month from a user

    Returns
    -------
    integer between 28 to 31 -> preforms extensive error testing to ensure
                                users input a value in this range 
    
    """

    while True:
        try:
            days_in_month = int(input(prompts_days_in_month))        
        except ValueError: # Users can't input non-integers
            raise ValueError(f"{prompt_error_handling_month}")

         # Users can't input values that dont fall betwwen min_number and max number
        if days_in_month < min_number_month_days or days_in_month > max_number_month_days:
            raise ValueError(f"{prompt_error_handling_month}")
        
        # Returned to be passed into calender_printer()
        return days_in_month

# ---------------------------------------------------------------------
# FUNCTION: Get number of days in week
# ---------------------------------------------------------------------

def get_days_in_week():
    
    """

    Get the day the week starts, from user

    Returns
    -------
    integer between 1 to 7 -> preforms extensive error testing to ensure
                                users input a value in this range 
    
    """

    while True:
        try:
            first_day  = int(input(prompt_first_day))
        except ValueError: # Users can't input non-integers
            raise ValueError(f"{prompt_error_handling_week}")

        # Users can't input values that dont fall betwwen min_number and max number  
        if first_day < min_number_week_days or first_day > max_number_week_days:      
            raise ValueError(f"{prompt_error_handling_week}") 
        
        # Returned to be passed into calender_printer()  
        return first_day

# ---------------------------------------------------------------------
# FUNCTION: Calender printer
# ---------------------------------------------------------------------

def calender_printer(days_in_month, first_day):

    """

    Prints the calendar using paramters user has passed in

    Paramaters
    ----------
    days_in_month : integer, Number of days in the month (28-31)
    first_day     : integer, Day of the week the month starts on (1-7)

    Returns
    -------
    list -> list of weekday names
    
    """

    calender_title = [" S", "M" , "T", "W", "T", "F", "S"]
    print("  ".join(calender_title)) 

   # Makes spaces/gaps based on first day of month
    for i in range(first_day-1):
        print("   ", end="") # Ensures it prints on same line

    # Takes number of days in the month
    for i in range(1, days_in_month+1): 
        print(f"{i:2}", end=" ") 

        # New line after every 7th day (including spaces)
        if (i + first_day - 1) % day_in_week == 0:
            print()  # Newline

    return calender_title

if __name__ == "__main__":

    days_in_month = get_days_in_month()
    first_day = get_days_in_week()
    calender_printer(days_in_month, first_day)
        