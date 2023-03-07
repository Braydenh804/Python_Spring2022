def in_set(sets, value):
    if str(value) in sets:
        print("The value "+ str(value)+ " is in the set " + str(sets))
        return True
    else:
        print("The value " + str(value) + " is not in the set " + str(sets))
        return False


if __name__ == '__main__':
    test_set = set('123567')
    test_value = 5
    in_set(test_set, test_value)
