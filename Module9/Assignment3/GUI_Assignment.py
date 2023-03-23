import tkinter as tk

class FavoriteMealGUI:
    def __init__(self, master):
        self.master = master
        master.title("Favorite Meal")

        # Checkbuttons
        self.breakfast_var = tk.BooleanVar()
        self.breakfast_cb = tk.Checkbutton(master, text="Breakfast", variable=self.breakfast_var,
                                           command=self.cb_checked)
        self.breakfast_cb.grid(row=1, column=0, sticky="W")

        self.second_breakfast_var = tk.BooleanVar()
        self.second_breakfast_cb = tk.Checkbutton(master, text="Second Breakfast", variable=self.second_breakfast_var,
                                                  command=self.cb_checked)
        self.second_breakfast_cb.grid(row=2, column=0, sticky="W")

        self.lunch_var = tk.BooleanVar()
        self.lunch_cb = tk.Checkbutton(master, text="Lunch", variable=self.lunch_var,
                                       command=self.cb_checked)
        self.lunch_cb.grid(row=3, column=0, sticky="W")

        self.dinner_var = tk.BooleanVar()
        self.dinner_cb = tk.Checkbutton(master, text="Dinner", variable=self.dinner_var,
                                        command=self.cb_checked)
        self.dinner_cb.grid(row=4, column=0, sticky="W")

        # Waiting label
        self.waiting_label = tk.Label(master, text="Waiting")
        self.waiting_label.grid(row=5, column=0)

        # Exit button
        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.grid(row=6, column=0)

    def cb_checked(self):
        if self.breakfast_var.get():
            print("Breakfast checked!")
        if self.second_breakfast_var.get():
            print("Second Breakfast checked!")
        if self.lunch_var.get():
            print("Lunch checked!")
        if self.dinner_var.get():
            print("Dinner checked!")


if __name__ == '__main__':
    m = tk.Tk()
    gui = FavoriteMealGUI(m)
    m.mainloop()