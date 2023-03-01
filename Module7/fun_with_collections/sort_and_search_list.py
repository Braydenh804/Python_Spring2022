def make_list(num):
    """
    :param num: The num parameter is to choose how many numbers the user will input a number into a list
    :return: This function returns as the value of the list which is num_list
    """
    i = 0
    num_list = []
    while i < num:  # Loops until num is no longer more than i so the loop will run the same amount as the value num
        value = get_input()
        try:
            num_list.append(int(value) if value.isdigit() else float(value))
            i += 1  # Add one to i so the loop runs the proper amount of times

        except ValueError:  # If this is reached user didn't input a number
            print("Invalid input. Please enter a numeric value.")  # alerts user and doesn't affect the desired amount
            # of numbers going to the list
    return num_list


def get_input():
    """
    :return: Returns the users input which is hopefully a number
    """
    return input("Please Enter A Number: ")


def sort_list(unsorted_list):
    """
    :param unsorted_list: This parameter is the input of a number list that comes from the users inputs and it will
    get sorted by either smallest to largest or vice versa
    :return: This returns the sorted list to the main, so it
    can be used for the user to now search the position of a certain number in that list
    """
    i = False
    while not i:
        try:
            high_low = int(input("Please Enter 1 to sort the list from low to high or 2 to sort from high to low: "))
            if high_low == 1:
                unsorted_list.sort()
                i = True
                print("Sorted List: "+str(unsorted_list))
                return unsorted_list
            elif high_low == 2:
                unsorted_list.sort(reverse=True)
                i = True
                print("Sorted List: "+str(unsorted_list))
                return unsorted_list  # I used a return statement because I needed to save the sorted_list to use in
                # another function and I needed that value to be relayed to the main, so I could access it
            else:
                raise ValueError
        except ValueError:
            print("Invalid Enter 1 or 2")


def search_list(num_list):
    """
    :param num_list: This is the number listed that gets searched for the position of a value
    """
    i = False
    while not i:
        try:
            search_input = int(input("Enter a number to search for in the list: "))
            if type(search_input) == int:
                position = num_list.index(search_input)
                print("The number you searched for was found first in the #" + str(position + 1) + " spot in the list" )
                i = True

            else:
                raise ValueError
        except ValueError:
            print("Invalid Search")
# I didn't use a return statement here as I no longer needed the users created variables to continue with more
# features so i just instead printed the values to the console from inside the function


# Driver code
if __name__ == "__main__":
    sorted_list = sort_list(make_list(4))
    search_list(sorted_list)
