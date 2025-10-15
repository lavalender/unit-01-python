book = {}
while True: 
    print("Contact Book Menu: ")

    print("1. Add contact")
    print("2. Delete contact")
    print("3. Lists contacts")
    print("4. Exit")
    contact = input("Enter your choice: ")
    if contact == "1":
        name = input("Enter the contact name: ")
        phone = (input("Enter their number: "))
        book[name] = phone
        print("Contact added successfully!")
    elif contact == "2":
        remove = input("What would you like to delete?")
        if remove in book:
            del book[name]
        else:
            print("That does not exist!")
    elif contact == "3":
        print("Contacts: ")
        for x in book:
            print(x, ":", book[x] )
    elif contact == "4":
        break
    else:
        print("That choice does not exist")