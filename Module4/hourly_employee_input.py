def get_employee_input():
    # Docstring -- Prompts the user for name, amount of hours worked and hourly pay and prints the info in the console

    first_name = input("Enter your first name : ")  # Get users first name
    # Get amount of hours worked loop until valid answer
    i = False
    while not i:
        try:
            hours_worked = int(input("Enter your weekly hours worked: "))
            hours_worked_as_int = int(hours_worked)
            if 0 <= hours_worked_as_int <= 115:
                i = True
            else:
                raise ValueError('Bad Input')
        except:
            print("Please input a valid amount of weekly hours")
    # Get the users hourly pay rate loop until valid answer
    i = False
    while not i:
        try:
            hourly_pay = float(input("Enter your hourly pay: "))
            hourly_pay_as_int = float(hourly_pay)
            if 0 <= hourly_pay_as_int:
                i = True
            else:
                raise ValueError('Bad Input')
        except:
            print("Please input a valid hourly pay")
# Print the info in a string
    print("{}, Weekly hours:{}, Hourly wage:${}".format( first_name, hours_worked_as_int, hourly_pay_as_int))

# Driver code
if __name__ == "__main__":
    get_employee_input()
