def get_employee_input():
    '''
    :return: This returns a string displaying the users weekly pay which is calculated in a function called in this function
    '''
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
    # Call weekly_pay function with the parameters from above and store the return value, so it can be printed to main
    pay_statement = weekly_pay(hours_worked_as_int, hourly_pay_as_int)
    return pay_statement

def weekly_pay(hours, pay):
   '''
   :param hours: This is the users input of weekly hours worked
   :param pay: This is the users input of hourly wage
   :return: This returns a string that displays the users weekly pay
   '''
   total_pay = hours * pay
   return "Your weekly paycheck will be $" + str(total_pay)


# Driver code
if __name__ == "__main__":
    # Calls get_employee_input function which returns as are final string of info about weekly pay
    print(get_employee_input())
