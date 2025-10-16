"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
from datetime import datetime
#i first used a code to help say the time now and then i store it in a variable
both = datetime.now()
#I then use the now part of the function to print out the current time
print(both)



"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
from datetime import datetime
 #first i use an variable for the current time
both = datetime.now()

convert = both.strftime("%m/%d/%Y") #i then use that variabel to make it simpler to then change the format of the to m/d/and y by using lowercase and uppercase letters
# lastly print out the result
print(convert)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
""" 
string1 = "10/4/2025"
string2 = "10/15/2025"
#i fist created two seperate springs and dates
string1again = datetime.strptime(string1, "%m/%d/%Y")
string2again = datetime.strptime(string2, "%m/%d/%Y")
#I then convert each of the strings into dates by striping them and putting them into the cstandard US date.
string3 = string2again - string1again
#After converting I then subtract the converted dates and store it into a new variable
print(string3)

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""
#I first ask the user to input their birthday in a specific sequence
birthdate = input("When is your birthday? m/d/y ")
#I then make sure to convert it into an actual date
birthday = datetime.strptime(birthdate, "%m/%d/%Y")
#next i also make sure to add the current time and time subtract the current time and the birthday to get how old you are.
today = datetime.now()
age = today.year - birthday.year
print(age , "years old")

