def multiply_string(message, n):
    '''
    :param message: holds the users input for there favorite class
    :param n: holds the number of times the user has selected to print the param message in the console bewteen 2 and 7
    '''
    i = 0 # loop that prints the users favorite class to the console the amount of times the user selected
    while i < n:
        print(message)
        i += 1


# Driver code
if __name__ == "__main__":
    # Asks user for there favorite class
    favorite_class = (input("Enter your favorite class: "))
    # Asks user how many times to print the favorite class in the console and makes sure it is a valid number and between 2 an 7
    i = False
    while not i:
        try:
            times_multiplied = (input("Enter a number between 2 and 7: "))
            times_multiplied_as_int = int(times_multiplied)
            if 2 <= times_multiplied_as_int <= 7:
                i = True
                multiply_string(favorite_class, times_multiplied_as_int)
            else:
                raise ValueError
        except:
            print('Please input a valid number') # If Input isn't valid it prints this and restarts

