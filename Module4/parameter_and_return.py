def multiply_string(message, n):
    i = 0
    while i < n:
        print(message)
        i += 1


# Driver code
if __name__ == "__main__":
    favorite_class = (input("Enter your favorite class: "))
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
            print('Please input a valid number')

