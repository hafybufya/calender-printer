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
    """function which gets the number of days in a month from users and preforms error handling """   
    while True:
        try:
            days_in_month = int(input(prompts_days_in_month))
            
        except ValueError: #users can't input non-integers
            raise ValueError(f"{prompt_error_handling_month}")

        if days_in_month < min_number_month_days or days_in_month > max_number_month_days:
            raise ValueError(f"{prompt_error_handling_month}")
        
        return days_in_month

# ---------------------------------------------------------------------
# FUNCTION: Get number of days in week
# ---------------------------------------------------------------------

def get_days_in_week():
    """function which gets the day of the week the month starts on and preforms error handling """               
    while True:
        try:
            first_day  = int(input(prompt_first_day))
        except ValueError:
            raise ValueError(f"{prompt_error_handling_week}")
              
        if first_day < min_number_week_days or first_day > max_number_week_days:
            raise ValueError(f"{prompt_error_handling_week}")   
        return first_day

# ---------------------------------------------------------------------
# FUNCTION: Calender printer
# ---------------------------------------------------------------------

def calender_printer(days_in_month, first_day):
    """function which prints a calender""" 
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
            print()  # newline
    return calender_title

if __name__ == "__main__":

    days_in_month = get_days_in_month()
    first_day = get_days_in_week()
    calender_printer(days_in_month, first_day)
        