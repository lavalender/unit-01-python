"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print('You cannot divide by zero.')

# Example usage:
divide_numbers(10, 0)

"""
Example 2: Opening Files
"""

def read_file(filename):
    try: 
        file = open(filename, 'r')
        contents = file.read()
    except FileNotFoundError:
        print("This file does not exist")
    print("File contents:", contents)
    file.close()

# Example usage:
read_file("nonexistent.txt")