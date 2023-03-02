# This program makes a note file with peoples names and test scores and reads to contexts of the read and prints it
# into the console
def get_student_info(student_name):
    """
    :param student_name: This name is what the user will input scores under to be stored in a tuple
    """
    students_scores = []  # List variable declared
    i = False  # Loop Condition
    while not i:  # Loop that does not end until I = true
        try:
            print("Entering scores for " + str(student_name))
            list_input = int(input("Enter your score between 1 and 100 (-1 to exit): "))  # User inputs a value
            if 1 <= list_input <= 100:  # Checks if the value is going to be stored in the list
                students_scores.append(list_input)  # Adds the valid number to the end of students_scores list
                print(list_input, " has been added to the list")  # Confirms there input is going to be in the list
            elif list_input == -1:  # If value is valid above but is equal to -1 end loop
                print("Thank you for entering scores for " + str(student_name))
                break  # Changed to break instead of having if change I to True
            else:
                raise ValueError('Bad Input')  # If value doesn't fit the criterion raise error to restart code
        except ValueError:
            print("Please input a valid number")  # Before code restarts inform user the input was invalid
    a_tuple = (student_name, students_scores)
    write_to_file(a_tuple)


def write_to_file(a_tuple):
    """
    :param a_tuple: is the name and a list of numbers from the previous function that is getting put in a text file
    """
    f = open('student_info.txt', 'a')
    f.write(str(a_tuple) + "\n")
    f.close()


def read_from_file():
    """
    This function reads each line of the student_info.txt file
    """
    f = open('student_info.txt', 'r')
    file_lines = f.readlines()
    # printing the list using loop
    for x in range(len(file_lines)):
        print(file_lines[x])
    f.close()


if __name__ == '__main__':
    open("student_info.txt", "w").close()
    get_student_info("Brayden")
    get_student_info("Rob")
    get_student_info("Jose")
    get_student_info("Caden")
    read_from_file()
