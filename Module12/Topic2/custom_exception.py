class InvalidCustomerIdException(Exception):
    pass


class InvalidNameException(Exception):
    pass


class InvalidPhoneNumberFormat(Exception):
    pass


class Customer:
    """Customer class"""

    def __init__(self, cid, lname, fname, pnumber):  # Constructor sets all to no value
        if int(cid) < 1000 or int(cid) > 9999:
            raise InvalidCustomerIdException("Invalid customer ID")
        if not all(c.isalpha() or c.isspace() for c in lname):
            raise InvalidNameException("Invalid last name")
        if not all(c.isalpha() or c.isspace() for c in fname):
            raise InvalidNameException("Invalid first name")
        if len(pnumber) != 12 or pnumber[3] != '-' or pnumber[7] != '-':
            raise InvalidPhoneNumberFormat(f"Invalid phone number format")
        for i in range(12):
            if i == 3 or i == 7:
                continue
            if not pnumber[i].isdigit():
                raise InvalidPhoneNumberFormat(f"Invalid phone number format")
        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnumber

    def __str__(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number

    def __repr__(self):
        return 'Customer({},{},{},{},{})'.format(self.customer_id, self.last_name, self.first_name, self.phone_number)

    def change_last_name(self, name):
        self.last_name = name

    def change_first_name(self, name):
        self.first_name = name

    def change_phone_number(self, number):
        self.phone_number = number

    def change_address(self, addy):
        self.address = addy

    def display(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number + " Address: " + self.address


# Driver code
# Valid customer
customer_one = Customer('1000', 'Duck', 'Donald', '555-555-5555')  # all required
print(str(customer_one))

# Invalid phone
# Wait! try/except needed!
# constructor with invalid customer_id
try:
    c = Customer(999, "Doe", "John", "123-456-7890")
except InvalidCustomerIdException as e:
    print("Caught exception:", e)

# constructor with invalid last_name
try:
    c = Customer(1234, "Doe1", "John", "123-456-7890")
except InvalidNameException as e:
    print("Caught exception:", e)

# constructor with invalid first_name
try:
    c = Customer(1234, "Doe", "John1", "123-456-7890")
except InvalidNameException as e:
    print("Caught exception:", e)

# constructor with invalid phone_number
try:
    c = Customer(1234, "Doe", "John", "1234-567-890")
except InvalidPhoneNumberFormat as e:
    print("Caught exception:", e)

try:
    c = Customer(1234, "Doe", "John", "1234-567-890")
except InvalidPhoneNumberFormat as e:
    print("Caught exception:", e)
