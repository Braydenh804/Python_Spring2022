def switch_level(level):
    '''
    :param level: This is the letter passed through when called that points to a level
    :return: This returns the score associated with the level that was inputted.
    '''
    switcher = {
        "N": 50,
        "B": 150,
        "E": 300,
        "A": 500
    }
    return switcher.get(level, "Invalid level")  # Returns amount of points associated with the level or the invalid level message


if __name__ == "__main__":
    print(switch_level("N"))  # Call all levels and a non level to test code output
    print(switch_level("B"))
    print(switch_level("E"))
    print(switch_level("A"))
    print(switch_level("X"))