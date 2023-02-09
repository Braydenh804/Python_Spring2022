def multiply_string(message, n):
    print( "hi")


# Driver code
if __name__ == "__main__":
    favorite_class = (input("Enter your favorite class: "))
    i = False
        while not i:
            try:
                times_multiplied = (input("Enter how many times you want to multiply the string between 2 and 7: "))
                times_multiplied_as_int = int(times_multiplied)
                if 2 <= times_multiplied_as_int <= 7:
                    i = True
                else:
                    raise ValueError
            except:
                print("Please input a valid number")
     multiply_string(favorite_class, times_multiplied_as_int)
