def in_set(sets, value):
    '''
    :param sets: the set created in the main is passed to the function
    :param value: the value that is to be looked for in the set is passed from the main
    :return: returns whether the value passed through was in the set being true if it was included and false if not
    '''
    if str(value) in sets: # If value is found in set return true and print below statement
        print("The value "+ str(value)+ " is in the set " + str(sets))
        return True
    else: # If value isn't found in set return false and print below statement
        print("The value " + str(value) + " is not in the set " + str(sets))
        return False


if __name__ == '__main__':
    # create test set and value to put in the in_set function
    test_set = set('123567')
    test_value = 5
    in_set(test_set, test_value)
