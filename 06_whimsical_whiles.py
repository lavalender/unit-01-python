"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
i = 1 # first you set a variable to 1

while i < 11: #while the i is less then 11
    print(i) # you print the current i you have if it is less than 11
    i += 1 #and then you add 1 and reeat until it is greater or equal to 11

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
print("Task 2")
i = 11 #first I set the i equal to 11 

while i > 1: #this means that from 11 it will continue if it is greater than one
    i -= 1 # then you subract from the new i value for example it starts with 11 so 11 - 1
    print(i) # and then you print that new i value

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
number = int(input("give me a number: ")) #first we ask the user for an input
result = 1

while number > 0: #the while function will continue until the new number is greater than 0 because you cant multiple 0 by a number without just getting 0
    result = number * result #first you mutliple 1 by the number you input in order to get the number as the new result
    number -= 1 #then that number then gets subtracted by 1 and continues through the while statement. The new subrtacted number will then get multipled the new result from before and will continue.
print(result)


"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
password = "PurpleDolphin" # I have a specific password the user has to get 
asks = input("Enter a password: ") # I then ask the user to enter the password

while asks != password: #the condition is if the input is not equal to the password
    print("Try Again!")
    asks = input("Enter a password: ") #and if it is not equal you have to input it until it is right
else:
    print("You got it!")
            

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

i = 0 #this is the first number in the Fibonacci sequence
i2 = 1 #this is the second number in the Fibonacci sequence
count = 0 #the counter starts at 0 and increaeses in the while function
n = int(input("Enter how many Fibonacci numbers to print: ")) #I ask the user how many of the numbers they want shown

while n > count: # then as the number is set the counter increases and the while function keeps going until the counter is greater than or equal to the input number 
    print(i)
    sum = i + i2 # so first the two number i and i2 are added to get a sum. 
    i = i2 . # then in the sequence the second number then gets added by the sum. So the i2 from before turns into the new i
    i2 = sum #Now the sum from before turns into the new i2 to get added. 
    count += 1 #the counter increase for the amount of times that while function is ran