def measurements(a_list):
    '''
    :param a_list: Hold a list of either one or two values that make up the lengths on either a square or rectangle
    :return: Returns a string of the area and perimeter of the square or rectangle
    '''

    def area(a_list):
        '''
        :return: Returns with the value of the area of the square or rectangle
        '''
        if len(a_list) == 1:  # If one value is in the list it's a square
            return a_list[0] ** 2  # This means the sides are the same, so we can just multiply the value by itself
        elif len(a_list) == 2:  # If two values are in the list it's a rectangle
            return a_list[0] * a_list[1] # This means we multiply both of the values together the get the area

    def perimeter(a_list):
        '''
        :return: Returns with the value of the perimeter of the square or rectangle
        '''
        if len(a_list) == 1:  # If one value is in the list it's a square
            return a_list[0] * 4  # Since it's a square there will be 4 sides at that length ,so we multiply by 4 to
            # get the perimeter
        elif len(a_list) == 2:  # If two values are in the list it's a rectangle
            return (a_list[0] + a_list[1]) * 2 # Since it's a rectangle there will be 2 sets of sides that have the
            # same length ,so we add the two values together and multiply it by 2 to get
            #  by 2 to get the perimeter

    area_val = area(a_list)
    perimeter_val = perimeter(a_list)

    return "Perimeter = " + str(perimeter_val) + " Area = " + str(area_val)


if __name__ == '__main__':
    rectangle = [2.1, 3.4]
    print(measurements(rectangle))  # expected output: Perimeter = 11 Area = 7.14

    square = [3.5]
    print(measurements(square))  # expected output: Perimeter = 14 Area = 12.25
