'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
x = int(input("Pick a number: "))
if x > 10:
    print("True")
else:
    print("False")
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
age = int(input("How old are you? "))
student_status = input("Whats your status ")
if age < 18 or student_status == "student":
    print("Price is $10")
else: 
    print("Price is $20")


'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
fruits_list = ["apple", "banana", "dragon fruit", "peach"]
fruit = input("What is your favorite fruit: ")
if fruit in fruits_list :
    print("Yes, that fruit is in the list.")
else: 
    print("No, that fruit is not in the list.")

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
...
'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
weight = int(input("What is the order weight? "))
zones = input("What zone are you in? Zone A or Zone B ")
if zones == "Zone A" or zones == "A":
    price1 = 


    
'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
