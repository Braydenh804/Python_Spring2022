class Employee:
    def __init__(self, lname, fname, addy, pnum, salaried, sdate, sal):
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = pnum
        self.salaried = salaried
        self.start_date = sdate
        self.salary = sal


    def display(self):
        emp_type = "Salaried" if self.salaried else "Hourly"
        if self.salaried:
            emp_salary = f"${self.salary:.2f}/year"
        else:
            emp_salary = f"${self.salary:.2f}/hour"
        return f"{self.first_name} {self.last_name}\n{self.address}\n{emp_type} employee: {emp_salary}\nStart date: {self.start_date}"


emp = Employee("Wilson", "Joe", "645 Oak Street\nDes Moines, Iowa", "123-123-9876", False, "4-22-2021", 18)
print(emp.display())
