"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
animals = ["dog", "cat", "snake", "tiger"]
print(animals)
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
num = [1 , 2 , 3, 4]
num.append( 67 )
print(num)
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
num = [1 , 2 , 3, 4]
num.remove(2)
print(num)

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
animals = ["dog", "cat", "snake", "tiger"]
animals.append("pig")
animals.append("lizard")
print(animals)
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
animals = ["dog", "cat", "snake", "tiger"]
del animals[2]
print(animals)

"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
list1 = [26, 27 ,30]
list2 = [39, 67, 41]
list3 = list1 + list2
print(list3)