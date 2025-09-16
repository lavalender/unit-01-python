"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""

ask = input("Enter the password: ") # first i asked for the user to input a password
if ask.lower() == "purpledolphin": # i put in the password that would work for my code and set it to automatically be lower after they put the password 
    print("You got it") 
else:
    print("WRONG") #if they didnt type in the right password it was wrong but as long as its the right password it shoudl be good

"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""
ask = input("Favorite Animal: ") # i did this to gain an inout 
if ask.strip() == "": #strip helps to remove the spaces and then the quotes check if the input is blank
    print("Wrong")
else:
    print("Right")

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""
animals= input("Which do you like most cat or dog: ") # To gain an input between the two i asked this question 
animal = animals.lower().replace("cat", "dog") # if they put cat despite if it is uppercase it will be set to lower and then set it to dog
print(animal)


"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""
name = input("What's your name? ") #ask for a name input
age = input("What's your age? ") #ask for an age input
print(name + " you're " + age + " years old. ") #print both responses into a sentence

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""
float1 = float(input("Put the first float: ")) #I asked for a float and if they didnt put a float in then it would automatically change it to one
float2 = float(input("Put the second float: ")) # i did it twice to get two floats
result = float2 / float1 #I divded the two floats
rounded_result = round(result, 1) #this rounds the result from the floats to the first tenth place
print(rounded_result) #lastly prints that new rounded result
