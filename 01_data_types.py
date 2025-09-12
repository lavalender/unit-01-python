
"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""

num = 23.36 #assigned by float a variable
newnum = int(num) #assigned my new converted float that is now an integer a variable 
print(newnum) #printed the new converted integer
print(num) #printed the original number



"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
num = -20 #i assigned by a variable to my number which would test to see if the code works
if num > 0: 
    print("positive") #if the number is greater than 0 than it is postive
elif num < 0: 
    print("negative") #if the number is less than 0 it is negative 
else:
    print("zero") #lastly if the number is neither and instead 0 then it is just zero. 
"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
num1 = float(input("give me a float: ")) #this prompts the user to give me a float and then checks to see if it is an float.
num2 = int(input("give me an integer: ")) #this prompts the user to give me a integer and then checks to see if it is an integer.
print(num1 + num2) #i put my two integer and float to add
print(num1 - num2) #put them to subtract
print(num1 * num2) #put them to multiply
print(num1/num2) #and lastly put them to divide all while printing out each of the results
"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
fruits = { #i first named the dictionary and assigned it a variable
    "dragon fruit" : 2,
    "banana" : 4,
    "strawberry" : 5
}#Then i assigned the quantities to the 3 fruits that i have 
print(fruits["strawberry"]) #I then printed out the value of the strawberry which is strored in my fruits dictionary 
"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
nums = "6,7,1,2,5" # i created a string variable 
my_nums = nums.split(",") # i then created a new variable for the string being turned into a tuple
print(nums) # i then printed the original string
print(my_nums) #and also my new tuple
"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""
list1 = ["Art", "Math", "Music"]
string = ",".join( list1 )
print(string)
dash_string = "-".join(list1)
print(dash_string)
