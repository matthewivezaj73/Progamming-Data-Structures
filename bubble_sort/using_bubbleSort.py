#Importing functions fom bubble_function.py
from functions.bubble_function import bubble_sort

#Creating a blank list.
user_list = []
#Setting a flag.
not_done = False
#Testing for user input.
while not not_done:
    #Printing out instructions to the user.
    print("Please enter \'a\' if you would like to add another item to the list.\nPlease enter \'s\' if you would like to sort and print the list.\nPlease enter \'q\' to quit the program.\n\nPlease enter your choice here:\t")
    #Asking the user if they would like to sort the list.
    user_choice = input()
    #Handling the case where the user chooses option a.
    if user_choice == "a":
        #Asking the user to input a number.
        print("Please input a number:")
        #Accepting input from the user.
        user_entry = input()
        #Checking if the input is a number.
        if (('.' in user_entry) and (user_entry.replace('.', '').isdigit())) or user_entry.isdigit():
            #Appending the item entered into a list.
            user_list.append(user_entry)
    #Handling the case where the user chooses option s.
    elif(user_choice == "s"):
        #Sorting the list.
        user_list.sort()
        #Printing the list.
        print(user_list)
    #Handling the case where the user chooses option q.
    elif(user_choice == "q"):
        not_done = True