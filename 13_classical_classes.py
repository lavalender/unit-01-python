"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class Person:
   def __init__(self, name, age): #used init to define name and age attributes
       self.name = name
       self.age = age

   def hello(self): #function helps to print the attributes that you inputted with the sentence
       print(f"Hello my name is {self.name} and I am {self.age}")
introduction = Person("Valerie", 67) #the name and age to what you want to input into the hello 
introduction.hello() #the hello plus the attributes are then printed
"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
class Animal:
    def speak(self): #created a empty speak to be used in the different functions for the animals
        pass #pass it in order for it to move on to the next function
class Dog(Animal):
    def speak(self):
        print("Woof")
class Cat(Animal):
    def speak(self):
        print("Meow")

my_dog = Dog() #created objects to print the functions
my_cat = Cat()

my_dog.speak() 
my_cat.speak()
"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

class BankAccount:

    def __init__(self, balance, owner): #created the two attributes using init
        self.balance = balance
        self.owner = owner
     

    def deposit(self, amount): #amount attribute used to help store the amount you want to add
        if amount > 0: #if amount is more then 0 then it gets added to the current balance
           self.balance += amount 
           print(f"New balance {self.balance}")
        else: #if the amount is 0 or less this will print
           print("Insuffient amount, you cannot add $0")

    def withdraw(self, amount):#amount attribute used to help store the amount you want to subtract
        if amount > 0:#if amount is more then 0 then it gets subtracted to the current balance
            self.balance -= amount
            print(f"New balance {self.balance}")
        else: #if the amount is 0 or less this will print
            print("Insuffient amount, you cannot add $0")

account = BankAccount(100, "Dilisa") #created  an object to store the balance and owner

account.deposit(50) #adds 50
account.withdraw(50) #subtracts 50



