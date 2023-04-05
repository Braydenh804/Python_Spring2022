import gc
class Person:
    """Person class"""

    def __init__(self, lname, fname, addy=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        return self.last_name + ", " + self.first_name + " lives at " + self.address
class Student:
    """Student class"""

    def __init__(self, fname, major, sdate, gpa):
        self.first_name = fname
        self.major = major
        self.start_date = sdate
        self.gpa = gpa

    def change_major(self, new_major):
        self.major = new_major

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

    def display(self):
        return f"Name: {self.first_name}\nMajor: {self.major}\nStart Date: {self.start_date}\nGPA: {self.gpa}"




# Driver
if __name__ == '__main__':
    # Create a student object
    my_student = Student('Brayden','Computer Science','08/2022', 4.0)
    # Display Student
    print(my_student.display())
    # Change Major
    my_student.change_major('Being Awesome!')
    # Update the gpa
    my_student.update_gpa(3.0)
    # Display the student again
    print(my_student.display())
    # Perform garbage collection
    del my_student
    gc.collect()
