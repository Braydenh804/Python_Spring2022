def make_list(num):
    '''
    :param num: The num parameter is to choose how many numbers the user will input a number into a list
    :return: This function returns as the value of the list which is num_list
    '''
    i = 0
    num_list = []
    while i < num:  # Loops until num is no longer more than i so the loop will run the same amount as the value num
        value = get_input()
        try:
            value = float(value)
            num_list.append('%g' % (value))  # This shaves off extra zero from the end of the float values and stores
            # them in a list
            i += 1  # Add one to i so the loop runs the proper amount of times

        except ValueError:  # If this is reached user didn't input a number
            print("Invalid input. Please enter a numeric value.")  # alerts user and doesn't affect the desired amount
            # of numbers going to the list
    return num_list


def get_input():
    '''
    :return: Returns the users input which is hopefully a number
    '''
    return input("Please Enter A Number:")


# Driver code
if __name__ == "__main__":
    print(make_list(10))  # Calls function and sets it to get 10 numbers from the user to be put in a list
