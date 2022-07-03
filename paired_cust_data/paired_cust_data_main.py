#Creating a list of customer determinations contained in a set.

"""
    Create a method later that loads this information on startup.
"""
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
    user_choice = input("Please enter what you would like to do with the customer data:\nEnter \'d\' to display the current customer data.\nEnter \'a\' to add new customer data.\nEnter \'e\' to edit or delete current customer data.\n\nPlease input your choice here:\t\t")
    #Handling the case where the user enters d.
    if user_choice == "d":
        #Creating a for loop.
        for line in customer_determinations:
            #Printing out each line.
            print(line)
    #Handling the case where the user enters a.
    elif user_choice == "a":
        #Asking the user for the customer's name.
        add_cust_data = ("Please enter a customer's name:\t\t")
        #Asking the user for the customer's decision.
        add_cust_decision = ("Please enter a customer's decision:\t\t")
    #Handling the case where the user enters e.
    elif user_choice == 'e':
        #Instructing the user on how to make a selection.
        user_selection = input("Please input the value of the field you would like to edit (starting from 0):\t\t")
        #Setting a flag.
        not_selection = False
        #Handling the case where the user wants to modify a field.
        if user_selection.isdigit():
            #Accessing the customer data for the element entered.
            #Asking the user for the customer's name.
            customer_determinations[user_selection][user_selection] = ("Please enter a customer's name:\t\t")
            #Asking the user for the customer's decision.
            customer_determinations[user_selection][(user_selection)] = ("Please enter a customer's decision:\t\t")