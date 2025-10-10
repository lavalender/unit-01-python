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

random1 = [random.uniform(0.0, 1.0) for x in range (5)]
random2 = [random.uniform(10.0, 20.0) for x in range (5)]
print(random1)
print(random2)


"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
#I first used a for loop in order to run the 
for i in range(3):
    list1 = ["red", "blue", "green", "yellow", "purple"]
    print(random.choice(list1))

"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
lists = list(range(1, 11))
random.shuffle(lists)
print(lists)

