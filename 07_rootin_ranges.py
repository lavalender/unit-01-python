"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
#i used a for loop to find the range from 1-11 excluding 11 and then print out each of ther numbers.
for x in range(1, 11):
    print(x)

print("////Exercise 1////")

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
#i first did the same as before and used a range to print out 900-1001 excluding. Additonally, I add the 10 at the end to help the for loop count by 10. 
for x in range(900, 1001, 10):
    print(x)
print("////Exercise 2////")

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
#I first do the same as before again but instead i started from 1 in order to start the counting. I then put the 1-101 in order to go from the range 1-100. I then put 9 at the end in order to make it count by 9
for x in range(1, 101, 9):
    print(x)
print("////Exercise 3////")

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
#first i set a variable for the sum and set it at 0 in order to it to later be changed
sum = 0 
#I then set the range from 1-11 so that it included 10. 
for x in range(1, 11):
    #i then use the sum vairable to then substitute the new numbers from the range
    sum += x
    #lastly i print out the sum of all the numbers in the 1-10 range
print(sum)

print("////Exercise 4////")

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?
The output of this code is 5 rows of of asterisks that increasing by one for each row. 
- Explain the iterative process that this code executes to get that output
"""
#
rows = 5
for i in range(rows): #this variable makes it so that the code runs 5 times. We then use the variable to havce the code run that many times
    #the second for loop then makes it so that with each tiem the code runs again another asterike is added at the end of where there is a space.
    for j in range(i + 1):
        print('*', end=' ')
    print() 
print("////Exercise 5////")
