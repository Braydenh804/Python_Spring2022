from Module13.Assignment3 import create_db
from Module13.Assignment3 import write_db
from Module13.Assignment3 import read_db
from tkinter import *

'''
Define functions/methods below here
'''


def create_student_and_person_table():
    create_db.create_tables('gui-db.db')


def add_person():
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    conn = write_db.create_connection("gui-db.db")
    with conn:
        person = (firstname, lastname)
        write_db.create_person(conn, person)


def add_student():
    firstname = firstname_entry.get()
    lastname = lastname_entry.get()
    major = major_entry.get()
    begin_date = startdate_entry.get()
    conn = write_db.create_connection("gui-db.db")
    with conn:
        student = (firstname, lastname, major, begin_date)
        write_db.create_student(conn, student)


# View person table
def view_person_table():
    conn = read_db.create_connection("gui-db.db")
    with conn:
        rows = read_db.select_all_persons(conn)
        for row in rows:
            print(row)


# View student table
def view_student_table():
    conn = read_db.create_connection("gui-db.db")
    with conn:
        rows = read_db.select_all_students(conn)
        for row in rows:
            print(row)


# GUI
root = Tk()

# Labels
Label(root, text="First Name").grid(row=0)
Label(root, text="Last Name").grid(row=1)
Label(root, text="Major").grid(row=2)
Label(root, text="Start Date").grid(row=3)

# Entries
firstname_entry = Entry(root)
lastname_entry = Entry(root)
major_entry = Entry(root)
startdate_entry = Entry(root)

firstname_entry.grid(row=0, column=1)
lastname_entry.grid(row=1, column=1)
major_entry.grid(row=2, column=1)
startdate_entry.grid(row=3, column=1)

# Buttons
button1 = Button(root, text="Create Database & Table", command=create_student_and_person_table).grid(row=4, column=0)
button2 = Button(root, text="Add Person", command=add_person).grid(row=4, column=1)
button3 = Button(root, text="Add Student", command=add_student).grid(row=4, column=2)
button4 = Button(root, text="View Person Table", command=view_person_table).grid(row=5, column=1)
button5 = Button(root, text="View Student Table", command=view_student_table).grid(row=6, column=1)
button6 = Button(root, text="Exit", command=root.quit).grid(row=7, column=1)

root.mainloop()