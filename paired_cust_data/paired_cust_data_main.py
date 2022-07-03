#Creating a list of customer determinations contained in a set.
customer_determinations = [
    ("Doris Johnson", "Yes"),
    ("Karen Arnold", "No"),
    ("Skylar Thompson", "Yes")
]
#Setting a flag.
not_done = False
#Creating a while loop.
while not not_done:
    #Requesting user input on what the user would like to do.
    user_choice = input("Please enter what you would like to do with the customer data:\nEnter \'d\' to display the current customer data.\n")
    #Handling the case where the user enters d.
    if user_choice == "d":
        #Creating a for loop.
        for line in customer_determinations:
            #Printing out each line.
            print(line)
    #Handling the case where the user enters a.
    elif user_choice == "a":
        #Asking the user for their name.
        add_cust_data = ("Please enter a customer's name:\t\t")