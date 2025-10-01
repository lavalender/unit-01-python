list2 = []
print("Your current todo list is: ")
#first you show your current list to the user
print(list2)
print("-------------------------------")
while True: # i then used a while loop to continue the to do list forever
    add = input("Would you like to add or remove a todo? ")

    if add.lower() == "add":
        add_what = input("What would you like to add to your todo list? ")
        list2.append(add_what)
        # i then append in order to add whatever the input they stated for in the add_what input. So anything they choose to add to the list then gets added.
        print("Your current todo list is: ")
        for x in list2:
            print(x)
            #next I display the updated list2 with the new appended items. Additonally, the add function then runs again to ask if they still want to add or remove something the next time
            print("-------------------------------")

    else:
        remove_what = int(input("which # todo would you like to remove"))
        print()
        del list2 [remove_what - 1]
        #i then ask what number specifically they would like to remove which the updated index which starts at 1 now. The -1 is used to help order the things in the list without
        # indexes. For example what would normally be 0, 1, 2 would now be 1, 2. 

        print("Your current todo list is: ")
        for x in list2:
            print(x)
            #lastly i then show the updated list with what they have removed from the list. 
        
                