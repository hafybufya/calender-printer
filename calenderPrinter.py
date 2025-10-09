# add a thing that means it can only take months that equal = 28, 29, 30, 31
#if they say 29 ask if its a leap year and if they say yes THEn continie and only then

#make sure no numbers hardcoded

day_in_week = 7 

prompts_days_in_month= "How many days are in the month? "

prompt_first_day = "What day of the week does the month start on? (Sun=1, Monday=2, ... Sat= 7) "

min_number_month_days = 28
max_number_month_days = 31
    #take user input: number of days in month

#days_in_month = int(input( prompts_days_in_month))
#days_in_month = 30

    #take user input: day the month starts on
first_day = int(input(prompt_first_day))
#user cant input value > 7


try:
    days_in_month = int(input( prompts_days_in_month))
except ValueError:
    print(" Months cannot have partial days! Please enter a whole number between 28 - 31") #unhardcode numbers
    days_in_month = int(input( prompts_days_in_month))
except NameError:
    #this part not working i thoguht it would work for string
    print("Must be an integer! Please enter a whole number between 28 - 31 ") #is there a way for this to be repeated everytime instead?
    first_day = int(input(prompt_first_day))
else:
        #takes number of days in the month
    for i in range(1, days_in_month+1): 
        print(f"{i:2}", end=" ") 




 # function to print calendar


#make sure this only prints if eveyrthing functional !!

# calender_title = ["S", "M" , "T", "W", "T", "F", "S"]
# print("  ".join(calender_title)) 

        #makes spaces based on first day of month
for i in range(first_day-1):
    print("   ", end="") # end = "" ensure it prints on same line

#     #takes number of days in the month
# for i in range(1, days_in_month+1): 
#     print(f"{i:2}", end=" ") 

            #new line after every 7th day (including spaces)
    if (i + first_day - 1) % day_in_week == 0:
        print()  # newline


#calls function
