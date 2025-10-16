book = {}
#First i put the whole code except the dictionary in the while statment in order to it to run over and over 
while True: 
    print("Contact Book Menu: ")
    #I then added the options for each setting in the contact book

    print("1. Add contact")
    print("2. Delete contact")
    print("3. Lists contacts")
    print("4. Exit")
    contact = input("Enter your choice: ")
    #I then ask the user what choice they want to have. 
    #for each choice i added it into an individual if elif else statement for each of the 4 choics
    if contact == "1":
        name = input("Enter the contact name: ")
        phone = (input("Enter their number: "))
        #In order to complete the first and third extra credit i then used is digit to keep the phon enumber as numbers and not letter. I then also use if len is greater than 10 in order to stop the code. 
        #I use an or statement to make sure that if 1 or both statements are met then it would print that output.
        if not phone.isdigit() or len(phone) > 10:
            print("The number you entered has to be less than 10 digits")
        else:
            book[name] = phone
            print("Contact added successfully!")
    #For the second part this is for if they input 2 and for when they want to delete a contact
    elif contact == "2"
        remove = input("What would you like to delete?")
        #I then use an if else statment for if what they want to remove exists already in the dictonary then prints that it does not exist if it doesn't.
        if remove in book:
            del book[name]
        else:
            print("That does not exist!")
    #This is then used in order to print out the dictionary is a proper and demure way. I use a for loop in order to print out each of the contacts that is being added in a specific way.
    elif contact == "3":
        print("Contacts: ")
        for x in book:
            print(x, ":", book[x] )
    #The 4th choice is then used to exit the contact book so I use a break to end it completely.
    elif contact == "4":
        break
    #Lastly if they input a number that does nto exist then it would display thyat it does not exist. 
    else:
        print("That choice does not exist")