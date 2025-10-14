"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
from datetime import datetime
#i first used a code to help say the time now and then i store it in a variable
both = datetime.now()
#I then 
print(both)



"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
from datetime import datetime
 
both = datetime.now()

convert = both.strftime("%m/%d/%Y")

print(convert)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
""" 
string1 = "10/4/2025"
string2 = "10/15/2025"

string1again = datetime.strptime(string1, "%m/%d/%Y")
string2again = datetime.strptime(string2, "%m/%d/%Y")
string3 = string2again - string1again
print(string3)

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

birthdate = input("When is your birthday? m/d/y ")

birthday = datetime.strptime(birthdate, "%m/%d/%Y")
today = datetime.now()
age = today.year - birthday.year
print(age , "years old")

