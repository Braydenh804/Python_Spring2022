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


class Employee(Person):
    def __init__(self, lname, fname, addy, sdate, salary):
        super().__init__(lname, fname, addy)
        self.start_date = sdate
        self.salary = salary

    def display(self):
        return f"{self.first_name} {self.last_name}\n{self.address}\nStart Date: {self.start_date}\nYearly Salary: {self.salary}\n"


class Manager(Employee, Person):
    def __init__(self, lname, fname, addy, sdate, salary, dept, direct_reports):
        super().__init__(lname, fname, addy, sdate, salary)
        self.department = dept
        self.direct_reports = direct_reports


    def get_raise(self, new_salary):
        self.salary = new_salary


    def display(self):
        return f"{self.department} Manager: {self.first_name} {self.last_name}\nAddress: {self.address}\nYearly Salary: {self.salary}\nStart Date: {self.start_date}\nDirect Reports:\n\n{employee1.display()}\n{employee2.display()}\n{employee3.display()}"


if __name__ == '__main__':
    employee1 = Employee("Jacob", "Ethan", "8423 Willow Dr\nDes Moines, Iowa", "04-26-22", "$30,000")
    employee2 = Employee("Wood", "Hayley", "436 Park Street\nDes Moines, Iowa", "03-21-23", "$31,000")
    employee3 = Employee("Stone", "Ben", "3521 Cypress Dr\nDes Moines, Iowa", "08-11-22", "$29,000")
    the_boss = Manager("Hayworth", "Brayden", "645 Oak Street\nDes Moines, Iowa", "05-17-21", "$40,000", "Perishables", [employee1, employee2, employee3])
    print(the_boss.display())
    the_boss.get_raise("$42,000")
    print(the_boss.display())