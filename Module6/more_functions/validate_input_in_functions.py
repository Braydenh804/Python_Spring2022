def score_input(test_name, test_score=-1, invalid_message='Invalid test score!'):
    '''
    :param test_name: User inputs the name of their test
    :param test_score: User inputs the score they got on said test
    :param invalid_message: User can create a custom error message for an incorrect numeric value
    :return: function returns the name of the test and the score whether it is valid, invalid or if it was bad input
    '''
    try:
        test_score = int(test_score)  # If user types a number in quotations it will convert it to a numeric value
        is_num = type(test_score)  # Checks to make sure input is a number to be used if it is not in the required range
        if 0 <= test_score <= 100:  # If test_score parameter is between 0 and 100 return test name and score to be
            # printed in main
            return test_name + ': ' + str(test_score)
        elif is_num == int or float:  # If test-score parameter is not in the range but is a float or int return the
            # test name and the invalid message parameter to be printed in main
            return test_name + ': ' + invalid_message
        else:
            raise ValueError  # Raise value error as the parameter passed was not a number and return the test name
            # and the value error to be printed in main
    except ValueError:
        return test_name + ': ValueError encountered'


if __name__ == '__main__':  # Testing different parameters being passed to the score_input function
    display_string = score_input('Test 1', 86)
    print(display_string)
    display_string2 = score_input('Test 2', -31)
    print(display_string2)
    display_string3 = score_input('Test 3', 121)
    print(display_string3)
    display_string4 = score_input('Test 4', "i did bad")
    print(display_string4)
    display_string5 = score_input('Final Exam', "130", "Shhh dont let the professor know")
    print(display_string5)