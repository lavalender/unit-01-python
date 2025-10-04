import math
print("Welcome to the Calculator-inator 9000!")
numone = float(input("Enter the first number: "))
numtwo = float(input("Enter the second number: "))
#I  created two different variables in order to store the values that the person inputs. This way i can just put the variable in for the calculator despite the multiple different inputs. 
print("Select Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponential")
print("7. Remainder")
# i then show the person the different operations that can be doen in the calculator

operation = int(input("Enter choice: "))
#I then made sure that the value that they pick is an integer. If not they will then be sent to the else statement at the bottom of the if statement where it will tell them to properly imput a number 1-7
if operation == 1:
    results = numone + numtwo
    print(results)
elif operation == 2:
    results = numone - numtwo
    print(results)

elif operation == 3:
    results = numone * numtwo
    print(results)

# for both 4 and 5 i then create two seperate if else statments inside the elif for when the second number which is the denomonster 0. I did this because anything divided by 0 is still just 0.
elif operation == 4: 
    if numtwo == 0:
        print("You cannot calculate with that number")
    else: 
        results = numone / numtwo
        print(results)

elif operation == 5:
    if numtwo == 0:
        print("You cannot calculate with that number")
    else: 
        results = numone // numtwo
        print(results)
elif operation == 6:
    results = numone ** numtwo
    print(results)

elif operation == 7:
    results = numone % numtwo
    print(results)
#This is then where the code will end if you input a value that is not an integer and not between 1-7
else:
    print("Invaild. Select an Operation 1-7")
