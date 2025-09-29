survey_name = input("Enter survey name: ") # so first the person who is inputting the survey results puts in the name
num_responses = int(input("Enter number of responses: ")) #then this is the amount of responses that gets unputted and run

total_rating = 0 #the total rating is calculated through the amount of rating each person puts
new_customers = 0 #this helps to count the total amount of new customers

for x in range(num_responses): # this for loop runs the amount of num of reponses fthat were inputed at the start
    customer_type = input("Are they a new customer? (y/n): ") # this is then used to ask someone if it is a new or returning cutomer
    rating = int(input("What is the rating?(1-5): ")) #this is then used to ask the user what is the rating
    total_rating += rating #the total rating is then calculated by adding the rating of each person and what they inputted
    if total_rating < 1 and total_rating > 5: #this if statement makes sure that the user stays inside the range of 1-5 for the rating
        print("Invaild") #if they go outside the range it then prints is invaild
    
    if customer_type == "y": #if the user types that they are a new customer it the adds to the variable new customers. 
        new_customers +=1
    else: #if they are not it then remains the same
        new_customers +=0

avg_rating =total_rating/num_responses #in order to find the average rating, we divide the added rating that was inputted and added before by the number of responses at the start
print(avg_rating) # then we finally print out the average
print(new_customers) #along with the total amount of new customers that we calculated and added before. 
    