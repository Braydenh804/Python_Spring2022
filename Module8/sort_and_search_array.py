import array as arr
def sort_array(arr):
    """
    Sorts the list that gets changed into an array in ascending order using the sort function
    """
    arr.sort()
    print(arr)
    return arr
def search_array(arr, obj):
    """
    Searches the input array for the given object and returns its index.
    Returns -1 if the object is not found in the array.
    """
    try:
        return arr.index(obj)
    except ValueError:
        return -1



if __name__ == "__main__":
    array_list = [45,24,21,99,54]
    num_array = arr.array('i', sort_array(array_list))
    search_value = search_array(num_array, 24)
    if search_value == -1 :
        print("Value was not found in the array below")
        print(num_array)
    else:
        print("Your value was stored in the array at position " + str(search_value))