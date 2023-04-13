import unittest


class Student:
    """Student class"""

    def __init__(self, lname, fname, major, gpa=0.0):
        if not isinstance(lname, str):
            raise TypeError("Last name should be a string")
        if not isinstance(fname, str):
            raise TypeError("First name should be a string")
        if not isinstance(major, str):
            raise TypeError("Major should be a string")
        if not isinstance(gpa, float):
            raise TypeError("GPA should be a float")
        if not 0.0 <= gpa <= 4.0:
            raise ValueError("GPA should be between 0.0 and 4.0")

        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.person = ('Doe', 'John')

    def tearDown(self):
        del self.person

    def test_object_created_required_attributes(self):
        student = Student("Doe", "John", "Computer Science")
        self.assertEqual(student.last_name, "Doe")
        self.assertEqual(student.first_name, "John")
        self.assertEqual(student.major, "Computer Science")
        self.assertEqual(student.gpa, 0.0)

    def test_object_created_all_attributes(self):
        student = Student("Doe", "John", "Computer Science", 3.5)
        self.assertEqual(student.last_name, "Doe")
        self.assertEqual(student.first_name, "John")
        self.assertEqual(student.major, "Computer Science")
        self.assertEqual(student.gpa, 3.5)

    def test_student_str(self):
        student = Student("Doe", "John", "Computer Science", 3.5)
        self.assertEqual(str(student), "Doe, John has major Computer Science with gpa: 3.5")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(TypeError):
            student = Student(123, "John", "Computer Science")

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(TypeError):
            student = Student("Doe", 123, "Computer Science")

    def test_object_not_created_error_major(self):
        with self.assertRaises(TypeError):
            student = Student("Doe", "John", 123)

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(TypeError):
            student = Student("Doe", "John", "Computer Science", "3.5")

        with self.assertRaises(ValueError):
            student = Student("Doe", "John", "Computer Science", -1.0)
            student = Student("Doe", "John", "Computer Science", 4.5)

def main():
    student1 = Student("Doe", "John", "Computer Science", 3.5)
    student2 = Student("Smith", "Jane", "Mathematics", 3.9)
    print(student1)
    print(student2)


    main()