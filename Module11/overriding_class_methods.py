class Employee:
    def __init__(self, lname, fname, addy, pnum):
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = pnum


    def display(self):
        return f"{self.first_name} {self.last_name}\n{self.address}Phone #: {self.phone_number}"


class SalariedEmployee(Employee):
    def __init__(self, sdate, salary, lname, fname, addy, pnum):
        super().__init__(lname, fname, addy, pnum)
        self.start_date = sdate
        self.salary = salary


    def give_raise(self, new_salary):
        self.salary = new_salary


    def display(self):
        return f"{self.first_name} {self.last_name}\n{self.address}\nPhone #: {self.phone_number}\nStart Date: {self.start_date}\nYearly Salary: {self.salary}\n"


class HourlyEmployee(Employee):

    def __init__(self, sdate, hourly_pay, lname, fname, addy, pnum):
        super().__init__(lname, fname, addy, pnum)
        self.start_date = sdate
        self.hourly_pay = hourly_pay


    def give_raise(self, new_hourly_pay):
        self.hourly_pay = new_hourly_pay


    def display(self):
        return f"{self.first_name} {self.last_name}\n{self.address}\nPhone #: {self.phone_number}\nStart Date: {self.start_date}\nHourly Pay: {self.hourly_pay}\n"




if __name__ == '__main__':
    employee1 = SalariedEmployee("08-11-2018", "$40,000", "Doe", "John", "342 Clearview Dr\nDes Moines, Iowa", "515-123-4567")
    print(employee1.display())
    employee1.give_raise("$45,000")
    print(employee1.display())
    employee2 = HourlyEmployee("04-15-2019", "$10", "Doe", "Jane", "243 Blankview Dr\nDes Moines, Iowa", "515-765-4321")
    print(employee2.display())
    employee2.give_raise("$12")
    print(employee2.display())