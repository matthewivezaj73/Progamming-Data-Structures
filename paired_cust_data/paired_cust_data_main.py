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