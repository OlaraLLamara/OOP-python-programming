# Your task is to write and test a function which takes one argument (a year) and returns True if the year is a leap year, or False otherwise.
def is_year_leap(year): #function decleration
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:

    # if((year % 400 == 0) or  (year % 100 != 0) and  (year % 4 == 0)): 
        print(True,  ":", year, "is a leap year")
    else:
        print(False, ":", year, "is not a leap year")

year = int(input("Please Enter a year to check if its a leap year or not: "))
is_year_leap(year) #function call 
