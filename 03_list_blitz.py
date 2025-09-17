"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
animals = ["dog", "cat", "snake", "tiger"] # I created a list for animals
print(animals) # and then printed it
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
num = [1 , 2 , 3, 4] #i created a list for numbers
num.append( 67 ) #next used append to add the number 67
print(num) #lastly printed the new list 
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
num = [1 , 2 , 3, 4] #I created a list 
num.remove(2) #I then removed the number at the second index
print(num) #lastly printed the new list

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
num_list = [2 , 4 , 6 , 8] # i created a random list
num_list[2] = 12 #i chose the index 2 to replace with the new number 12
print(num_list) # i then printed out the updated list
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
animals = ["dog", "cat", "snake", "tiger"] # i first created a random list
animals.append("pig") #I appended the first animal name
animals.append("lizard") #then appended another which would be at the end of the list
print(animals) # I then printed out the updated list
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
animals = ["dog", "cat", "snake", "tiger"] # i created a random list
del animals[2] #then specifically chose to delete index 2 
print(animals) # lastly printed the updated list

"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
animals_list = ["dog", "cat"] # I used the list from the last task and created a new list 
print(animals_list) #I then printed the new list
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
list1 = [26, 27 ,30] #i created my first list
list2 = [39, 67, 41] #I created my second list
list3 = list1 + list2 # then used a variable to store my new combined lists 
print(list3) #then printed out that new list