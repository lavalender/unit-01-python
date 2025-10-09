import random
"""
Task 1 (random module):
Write a program that simulates rolling a six-sided die 10 times.
Print each roll result.
"""
for i in range(11):
    dice = random.randint(1, 6)
    print(dice)



"""
Task 2 (random module):
Write a program that generates 5 random floating-point numbers between 0 and 1.
Then generate 5 random floating-point numbers between 10 and 20.
Print both sets of numbers.
"""



"""
Task 3 (random module):
Create a list of colors: ["red", "blue", "green", "yellow", "purple"].
Write a program that randomly selects and prints 3 colors from this list without replacement.
"""
for i in range(3):
    list1 = ["red", "blue", "green", "yellow", "purple"]
    print(random.choice(list1))

"""
Task 4 (random module):
Write a program that creates a list of numbers from 1 to 10, then shuffles the list
and prints the shuffled result.
"""
list2 = [""]
nums = random.randrange(1, 11)
    
print(list2)

