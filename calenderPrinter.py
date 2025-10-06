
days_in_month = int(input("How many days are in the month? "))
first_day = int(input("What day of the week does the month start on? (Sun=1, Monday=2, ... Sat= 7) "))

counter = 0 #counts the number of variables 
#def calender_printer(days_in_month, first_day):

calender_title = ["S", "M" , "T", "W", "T", "F", "S"]

print(calender_title)

for i in range(first_day-1):
    print("_", end = " ") #ensure it prints on same line

for i in range(1, days_in_month+1):
    print(i, end= " ")



#print_gaps based on the day user selected
