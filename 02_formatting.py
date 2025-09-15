"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""

ask = input("Enter the password: ")
if ask.lower() == "purpledolphin":
    print("You got it") 
else:
    print("WRONG")

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
ask = input("Favorite Animal: ")
if ask.strip() == "":
    print("Wrong")
else:
    print("Right")

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
animals= input("Which do you like most cat or dog: ")
animal = animals.lower().replace("cat", "dog")
print(animal)


"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
name = input("What's your name? ")
age = input("What's your age?")
print(name + " you're " + age + " years old. ")

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
float1 = input("Put the first float: ")
float2 = input("Put the second float: ")
result = float2 / float1 
print(result)