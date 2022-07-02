#Importing functions fom bubble_function.py
from functions.bubble_function import bubble_sort

#Creating a blank list.
user_list = []
#Setting a flag.
not_done = False
#Testing for user input.
while not not_done:
    #Asking the user if they would like to sort the list.
    user_choice = input("Please enter \'a\' if you would like to add another item to the list.\nPlease enter \'s\' if you would like to sort and print the list.\n\nPlease enter your choice here:\t")
    #Handling the case where the user chooses option a.
    if user_choice == "a":
        #Asking the user to input a number.
        print("Please input a number:")
        #Accepting input from the user.
        user_entry = input()
        #Checking if the input is a number.
        if (('.' in user_entry) and (user_entry.replace('.', '').isdigit()) and (len(user_entry.replace('.', '')) >= 2 and len(user_entry.replace('.', '')) <= 8)) or user_entry.isdigit():
            #Appending the item entered into a list.
            user_list.append(user_entry)