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
number = int(input("give me a number: ")) #
result = 1

while number > 0:
    result = number * result
    number -= 1
print(result)


"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
password = "PurpleDolphin"
asks = input("Enter a password: ")

while asks != password:
    print("Try Again!")
    asks = input("Enter a password: ")
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

i = 0 
i2 = 1

while 1 > 0:
    sum = i + i2
    i2 == sum
    sum = i2 + sum


print(sum)