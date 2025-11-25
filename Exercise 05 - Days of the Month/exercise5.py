print('welcome to the days in a month program')
def monthdays():
    #dictionary which holds months numbers as keys and number of days as values
    number_days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:21,11:30,12:31}
    #Ask user for month
    month=int(input("Enter the month number(1-12):"))
    #Check if the month number is valid
    if month<1 or month>12:
        print("Invalid month number.Please enter a value between 1 and 12")
    else:
     #Check leap year
     if month==2:
         leapyear=input("Is it a leap year? (yes/no):")
         if leapyear=="yes":
            print("February has 29 days")
         else:
            print("February has 28 days")
     else:
         print("Month",month,"has",number_days[month],"days.")
monthdays()