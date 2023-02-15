"""Allows a user to enter as many numbers between 1 and 100 that will be added to a list that will print when the
user enters -1 to exit"""
users_num_list = []  # List variable declared
i = False  # Loop Condition
while not i:  # Loop that does not end until I = true
    try:
        list_input = int(input("Enter a number between 1 and 100 (-1 to exit):"))  # User inputs a value
        if 1 <= list_input <= 100:  # Checks if the value is going to be stored in the list
            users_num_list.append(list_input)  # Adds the valid number to the end of users_num_list
            print(list_input, " has been added to the list")  # Confirms there input is going to be in the list
        elif list_input == -1:  # If value is valid above but is equal to -1 end loop
            i = True
        else:
            raise ValueError('Bad Input')  # If value doesn't fit the criterion raise error to restart code
    except ValueError:
        print("Please input a valid number")  # Before code restarts inform user the input was invalid

print("Numbers in your list:")  # When code is exited by the user typing -1 print every value stored in users_num_list
for n in users_num_list:
    print(int(n))
