import random
"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
#I first created a for loop in at the range of 11 so that it can run 10.
for i in range(11):
    dice = random.randint(1, 6)
    print(dice)
    #i then use randint in order to the dice to roll arandom number from 1-6 and then print the reuslt 10 times.



"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""
#I first used random.uniform to generate 5 random floating point numbers that are between 0 and 1
random1 = [random.uniform(0.0, 1.0) for x in range (5)]
# I then use the same thing for thenunberz between 10 and 20
random2 = [random.uniform(10.0, 20.0) for x in range (5)]
print(random1)
print(random2)
#I then print each one randomly between each variable


"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
#I first used a for loop in order to run the list with the colors in it. I put the number 3 to just run the code 3 times.
for i in range(3):
    list1 = ["red", "blue", "green", "yellow", "purple"]
    #I then add the random choice to help pick 3 diffeent colors in thoes 3 times
    print(random.choice(list1))

"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
#I first created a list from 1-10 using range which would exclude the last number 11. 
lists = list(range(1, 11))
random.shuffle(lists)
print(lists)
# I then used a random shuffle to shuffle that list and print a number out from 1-10.

