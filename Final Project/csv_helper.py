import csv
# Import writer class from csv module
from csv import writer
from tkinter import *


def formatinfo():
    info = entry.get()
    end = len(info) - 11
    prefix = info[0:3]
    class_num = info[4:7]
    class_name = info[10:end]
    credit_num = info[-1]
    List = [prefix, class_num, class_name, credit_num]
    print(List)
    int(credit_num)
    add_to_file(List)
    entry.delete(0, END)


def add_to_file(List):
    with open('DMACC Credit Classes.csv', 'a') as f_object:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)

        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(List)
        print("Added to csv file")

        # Close the file object
        f_object.close()

root = Tk()
entry = Entry(root, width=70)
entry.grid(row=0, column=0)
button1 = Button(root, height=10, width=50, text="Submit to CSV File", command=formatinfo).grid(row=1, column=0)
root.geometry("400x100")
root.mainloop()