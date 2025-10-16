"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""
def greeting(name): 
    print("Hello " + name)

greeting("Coco and Oreo")

"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def numsqu(a, b): 
    return a ** b

print(numsqu(2, 4))

"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
def oddoeven(number): 
    return number % 2 == 0
print(oddoeven(2))


"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
def rectangle(len, wid):
    return len * wid 
    
print(rectangle(3, 5))
"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def temperature(C):
    return (C * 1.8) + 32

print(temperature(38))
"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
def mean (num):
    return sum(num) // len(num)

print(mean([1, 2, 3, 10]))
"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.

Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""
def store (price, quantity, discounts = 0.0):
    subtotal = price * quantity
    return subtotal - (subtotal * discounts)
print(store(3, 4))