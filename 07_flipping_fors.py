"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
#first i set a variable for the word that I want to print out each chracter for
animal = "Penguin"
#i then created a loop for each chracter in the variable animal and to print out that character
for char in animal:
    print(char)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
#I first made a list with two numbers in it to calculate
print("----------------Excersise 2----------------")
nums = [5, 10]
result = 0
#Using result as an empty vairable to hold the reuslt i then use it in a for loop to run and add the result to the x. This runs twice because there are two numbers in the list so it runs and sets the first number as result then adds the second number.
for x in nums:
    result += x
    print(result)
"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
#i first made a sentence to use for the code
sen = ("I love cats and dogs.") 
#I then used the split function, to help split the words after the spaces, 
lists= sen.split(" ")
#I then use a for loop in order to count the different lengths of each word after the split. 
for x in lists:
    print(len(x))

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
#I expected the code to possibly print out the length of the words because in the for loop I used x in animals. 
#Instead in the code, it prints out the number that I assigned to the word. 

#First i created an animal list with 4 different animals and assigned a number or "value" for each
animals = {
    "cats" : 67, 
    "dogs": 21,
    "lions":11,
    "wolves":10
}

#I then use a for loop to print out the key and also the number that I assigned which is placed as x in animals
for x in animals:
    print("Key:")
    print(x)
    print("Value:")
    print(animals[x])
