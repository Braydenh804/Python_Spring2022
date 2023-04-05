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


class Student(Person):
    """Student class"""

    def __init__(self, id_num, lname, fname, major="Computer Science", gpa="0.0"):
        super().__init__(lname, fname, addy='')
        self.id_number = id_num
        self.major = major
        self.gpa = gpa

    def change_major(self, new_major):
        self.major = new_major

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

    def display(self):
        return f"{self.last_name}, {self.first_name}:({self.id_number})\nMajor: {self.major}\nGPA: {self.gpa}"


# Driver
if __name__ == '__main__':
    # Driver
    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())
    del my_student
    gc.collect()
