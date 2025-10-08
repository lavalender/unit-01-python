import os
import sys
"""
Task 1 (os module):
Write a Python program that prints the current folder (working directory) using the os module.
"""
current = os.getcwd()
print(current)
#I first used a variable to hold the value of the current directory and then printed it out
"""
Task 2 (os module):
Create a new directory called "test_folder" in the current directory.
Then print a list of all files and directories in the current directory.
"""
#first i created a file/ directory called test_folder. 
files = os.listdir()
#Next i then create a variable to save the list of the directories, and print it out after.
print(files)

"""
Task 3 (os module):
Write a program that checks if a directory called "data" exists in the current 
working directory. If it doesn't exist, create it. If it does exist, print 
"Directory already exists."
"""

#First i used the os path exists in order to find whether or not the directory data esixts
if os.path.exists("data"):
    print("Directiory already exists")
#if the path did exist then a message would pop up stating that it already exists and does not need to be made
else:
    os.mkdir("data")
#if the file does not already exist then the if else statment makes it. 


"""
Task 4 (os.path module):
Write a program that checks if a file called "config.txt" exists in the current directory.
If it exists, print its path. If it doesn't exist, print "File not found."
"""
#I first used an if else statment in order to determine whether or not the file existed
if os.path.isfile("config.txt"):
    print(os.path.abspath("config.txt"))
#for the if statment it looks for the file and after will print out its directory using the abspath
else:
    print("File not found")
#in the else statement if the if statment does not qualify then it goes to the else where it states that the file is not foumd. 
"""
Task 5 (sys module):
Write a program that prints the Python version you are currently using.
"""
print("Python Version")
print(sys.version)
#In order to print out the version i used the sys version and also printed out a statement stating its the Python Version

"""
Task 6 (sys module):
Write a program that prints the platform your Python interpreter is running on
(e.g., 'linux', 'win32', 'darwin'). The output should be user friendly names
"Linux", "Windows", "MacOS"
"""
platform = sys.platform
#first i saved the code to find the platform as a variabel to help make it easier to use in the if else functions

if platform == ("linux"):
    print("Linux")
elif platform == ("win32"):
    print("Windows")
elif platform == ("darwin"):
    print("MacOS")
else:
    print("Any other platform")
#next i then go through each platform using its offical name in the system and then additonally priting out its common name to make it more understanding for people who dont know their interpreter name