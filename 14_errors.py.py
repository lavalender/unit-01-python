"""
Identify the potential errors in the following code snippets and modify 
them to include appropriate try/except blocks to handle exceptions gracefully.
"""


"""
Example 1: Division
"""

def divide_numbers(num1, num2):
    try: #i put try around this code because this would result in the error if a 0 is substituted
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError: #if the 0 was then used in the code and the error came up it would print this
        print('You cannot divide by zero.')

# Example usage:
divide_numbers(10, 0)

"""
Example 2: Opening Files
"""
def read_file(filename):
    try: #if the file is not found then the error would occur so i used a try if that happens
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError: #because the file does not exist this error pops up so i created the print
        print("This file does not exist")

"""
Example 3: List Items
"""

def get_item(lst, index):
    try: #in case that the index does not exist and the code cant run, i used try 
        item = lst[index]
    except IndexError: #when the error does occur then i print that it does not exist
        print("This index does not exist within the list")
        return
    print("Item:", item)
# Example usage:
my_list = [1, 2, 3]
get_item(my_list, 5)

"""
Example 4: Dictionaries
"""

def get_value(dictionary, key):
    try: #in case the dictionary key does not exist i used a try 
        value = dictionary[key]
        print("Value:", value)
    except KeyError: #when it does not exist i then print out that the key does not exist
        print("That key does not exist")
        return

# Example usage:
my_dict = {"a": 1, "b": 2}
get_value(my_dict, "c")

"""
Example 5: Else/Finally
Modify the following code to include an else block to execute code if no exceptions occur 
and a finally block to ensure that a certain action is always performed, regardless of whether an exception is raised.
"""
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:", contents)
    except FileNotFoundError:
        print("Error: File not found.")
    else: #else statement was made in the case that the error did not occur and the file was found
        print("File contents:", contents)
        print("File has been found")
    finally: #added a finally which prints even if it did or did not work
        print("File extraction attempted")

# Example usage:
process_file("example.txt")

