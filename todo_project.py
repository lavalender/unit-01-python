list2 = []
print("Your current todo list is: ")
#first you show your current list to the user
print(list2)
while True: # i then used a while loop to continue the to do list forever
    add = input("Would you like to add or remove a todo?")
    
    if add.lower() == "add":
        add_what = input("What would you like to add to your todo list?")
        list2.append(add_what)
        print("Your current todo list is: ")
        for x in list2:
            print(x)
    else:
        remove_what = int(input("which # todo would you like to remove"))
        print()
        del list2 [remove_what - 1]
        print("Your current todo list is: ")
        for x in list2:
            print(x)
        
                