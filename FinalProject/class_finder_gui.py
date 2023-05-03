from tkinter import *
from PIL import Image, ImageTk
import csv


def create_login_window():
    # Create a Tkinter Log In Window
    login_window = Tk()
    login_window.title("Log In")
    login_window.geometry(f'{1035}x{1080}+{-10}+{0}')
    login_window.columnconfigure(0, weight=1)
    login_window.rowconfigure(1, weight=1)
    login_window.configure(bg='#333333')

    # Login in window functions

    def change_to_window():
        student_id = id_entry.get()
        if student_id.isnumeric() and len(str(student_id)) == 9:
            login_window.destroy()
            create_window()
        else:
            id_entry.delete(0, END)

    # Create Start Page GUI widgets
    start_page = Frame(login_window)
    start_page.config(bg="#333333")
    header_label = Label(start_page, text="DMACC Course Sign Up", bg='#333333', fg="#0c2b59", font=("Arial", 30))
    enterid_label = Label(start_page, text="Enter Student Id", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    id_entry = Entry(start_page, font=("Arial", 16))
    start_button = Button(start_page, text="Continue", bg="#0c2b59", fg="#FFFFFF", font=("Arial", 16),
                          command=change_to_window)
    info_label = Label(start_page, text="Please enter your 9 digit numeric id", bg='#333333', fg="#FFFFFF",
                       font=("Arial", 16,))

    # Placing widgets on the start_screen
    header_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=30)
    enterid_label.grid(row=1, column=0)
    id_entry.grid(row=1, column=1, pady=20)
    start_button.grid(row=3, column=0, columnspan=2, )
    info_label.grid(row=4, column=0, columnspan=2)
    start_page.pack()
    login_window.mainloop()


class Screen(Frame):

    def __init__(self, master, name):
        Frame.__init__(self, master)
        # Attributes
        self.master = master
        self.name = name
        # Initalise with master
        self.master.add_screen(self)

    def show(self):
        """
        Method will show screen
        """
        self.master.show_screen(self.name)


class ScreenController(Frame):
    """
    Screen Controller
    will manage screens
    in the program
    """

    def __init__(self, parent):
        Frame.__init__(self, parent)
        # Configure
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # Attributes
        self.allScreens = {}
        self.currentScreen = None

    def add_screen(self, screen_object):
        """
        Adds a Screen object to the screenController
        """
        # Place the screen
        screen_object.grid(row=0, column=0, sticky="nsew")
        # Add to dictionary
        self.allScreens[screen_object.name] = screen_object

    def show_screen(self, screen_name):
        if screen_name in self.allScreens:
            # Display
            self.allScreens[screen_name].tkraise()
            # Update variable
            self.currentScreen = screen_name


def create_window():
    # Home screen functions

    # Create a Tkinter Window
    window = Tk()
    window.title("Class Finder")
    window.geometry(f'{1035}x{1080}+{-10}+{0}')
    window.columnconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.configure(bg='#333333')
    # Create a Controller for the screens
    screen_master = ScreenController(window)
    screen_master.grid(row=1, column=0, sticky="NSEW")

    home_page = Screen(screen_master, "Home Page")
    home_page.config(bg="#333333")

    # Create a navigation bar
    nav_bar = Frame(window)
    nav_bar.grid(row=0, column=0, sticky="EW")
    nav_bar.config(bg="#333333")
    home_page_button = Button(nav_bar, text='Current Schedule', bg="#0c2b59", fg='#FFFFFF', font=("Arial", 16),
                              command=lambda: home_page.show())
    add_classes_page_button = Button(nav_bar, text='Add New Classes', bg="#0c2b59", fg='#FFFFFF', font=("Arial", 16),
                                     command=lambda: add_new_classes.show())
    remove_classes_page_button = Button(nav_bar, text='Remove Classes', bg="#0c2b59", fg='#FFFFFF', font=("Arial", 16),
                                        command=lambda: remove_classes.show())
    tuition_total_page_button = Button(nav_bar, text='Check Tuition Total', bg="#0c2b59", fg='#FFFFFF',
                                       font=("Arial", 16), command=lambda: [tuition_total.show(), calculate_tuition()])
    sign_out_button = Button(nav_bar, text='Log Out', bg="#0c2b59", fg='#FFFFFF', font=("Arial", 16), command=quit)
    image = Image.open('settings-icon.png').convert('RGBA')
    image = image.resize((30, 30), Image.ANTIALIAS)
    settings_img = ImageTk.PhotoImage(image)
    admin_page_button = Button(nav_bar, text=' Admin Settings ', bg="#0c2b59", fg='#FFFFFF', font=("Arial", 16),
                               image=settings_img, compound=RIGHT, width=200, anchor='w',
                               command=lambda: admin_page.show())
    current_schedule_label = Label(home_page, text=' Schedule', font=("Arial", 50), bg='#333333', fg='#FFFFFF')

    # Placing toolbar widgets
    home_page_button.grid(row=0, column=0)
    add_classes_page_button.grid(row=0, column=1)
    remove_classes_page_button.grid(row=0, column=2)
    tuition_total_page_button.grid(row=0, column=3)
    admin_page_button.grid(row=0, column=4)
    sign_out_button.grid(row=0, column=5)
    current_schedule_label.grid(row=1, columnspan=6)

    # home_page main content GUI widgets
    # Semester 1 content

    s1_c1_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=48)
    s1_c2_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=48)
    s1_c3_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=48)
    s1_c4_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=48)
    s1_c5_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=48)
    s1_credits_display_label = Label(home_page, text='               0/16', font=("Arial", 14), bg='#333333',
                                     fg='#FFFFFF', anchor='w', width=48)
    semester1_label = Label(home_page, text='Semester 1:', font=("Arial", 20), bg='#333333', fg='#FFFFFF')
    s1_c1_label = Label(home_page, text='Class 1:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s1_c2_label = Label(home_page, text='Class 2:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s1_c3_label = Label(home_page, text='Class 3:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s1_c4_label = Label(home_page, text='Class 4:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s1_c5_label = Label(home_page, text='Class 5:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s1_total_credit_label = Label(home_page, text='Credits :', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                  anchor='w', width=6)

    # Semester 1 widgets placement

    semester1_label.grid(row=2, columnspan=2, pady=10)
    s1_c1_display_label.grid(row=3, column=0, columnspan=3)
    s1_c2_display_label.grid(row=4, column=0, columnspan=3)
    s1_c3_display_label.grid(row=5, column=0, columnspan=3)
    s1_c4_display_label.grid(row=6, column=0, columnspan=3)
    s1_c5_display_label.grid(row=7, column=0, columnspan=3)
    s1_credits_display_label.grid(row=8, column=0, columnspan=3)
    s1_c1_label.grid(row=3, column=0, sticky=W)
    s1_c2_label.grid(row=4, column=0, sticky=W)
    s1_c3_label.grid(row=5, column=0, sticky=W)
    s1_c4_label.grid(row=6, column=0, sticky=W)
    s1_c5_label.grid(row=7, column=0, sticky=W)
    s1_total_credit_label.grid(row=8, column=0, sticky=W)

    # Semester 3 content

    s3_c1_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=48)
    s3_c2_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=48)
    s3_c3_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=48)
    s3_c4_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=48)
    s3_c5_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=48)
    s3_credits_display_label = Label(home_page, text='               0/16', font=("Arial", 14), bg='#333333',
                                     fg='#FFFFFF', anchor='w', width=48)
    semester3_label = Label(home_page, text='Semester 3:', font=("Arial", 20), bg='#333333', fg='#FFFFFF')
    s3_c1_label = Label(home_page, text='Class 1:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s3_c2_label = Label(home_page, text='Class 2:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s3_c3_label = Label(home_page, text='Class 3:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s3_c4_label = Label(home_page, text='Class 4:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s3_c5_label = Label(home_page, text='Class 5:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s3_total_credit_label = Label(home_page, text='Credits :', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                  anchor='w', width=6)

    # Semester 3 widgets placement

    semester3_label.grid(row=9, columnspan=2, pady=10)
    s3_c1_display_label.grid(row=10, column=0, columnspan=3)
    s3_c2_display_label.grid(row=11, column=0, columnspan=3)
    s3_c3_display_label.grid(row=12, column=0, columnspan=3)
    s3_c4_display_label.grid(row=13, column=0, columnspan=3)
    s3_c5_display_label.grid(row=14, column=0, columnspan=3)
    s3_credits_display_label.grid(row=15, column=0, columnspan=3)
    s3_c1_label.grid(row=10, column=0, sticky=W)
    s3_c2_label.grid(row=11, column=0, sticky=W)
    s3_c3_label.grid(row=12, column=0, sticky=W)
    s3_c4_label.grid(row=13, column=0, sticky=W)
    s3_c5_label.grid(row=14, column=0, sticky=W)
    s3_total_credit_label.grid(row=15, column=0, sticky=W)

    # Semester 5 content

    s5_c1_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=48)
    s5_c2_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=48)
    s5_c3_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=48)
    s5_c4_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=48)
    s5_c5_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=48)
    s5_credits_display_label = Label(home_page, text='               0/16', font=("Arial", 14), bg='#333333',
                                     fg='#FFFFFF', anchor='w', width=48)
    semester5_label = Label(home_page, text='Semester 5:', font=("Arial", 20), bg='#333333', fg='#FFFFFF')
    s5_c1_label = Label(home_page, text='Class 1:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s5_c2_label = Label(home_page, text='Class 2:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s5_c3_label = Label(home_page, text='Class 3:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s5_c4_label = Label(home_page, text='Class 4:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s5_c5_label = Label(home_page, text='Class 5:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s5_total_credit_label = Label(home_page, text='Credits :', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                  anchor='w', width=6)

    # Semester 5 widgets placement
    semester5_label.grid(row=16, columnspan=2, pady=10)
    s5_c1_display_label.grid(row=17, column=0, columnspan=3)
    s5_c2_display_label.grid(row=18, column=0, columnspan=3)
    s5_c3_display_label.grid(row=19, column=0, columnspan=3)
    s5_c4_display_label.grid(row=20, column=0, columnspan=3)
    s5_c5_display_label.grid(row=21, column=0, columnspan=3)
    s5_credits_display_label.grid(row=22, column=0, columnspan=3)
    s5_c1_label.grid(row=17, column=0, sticky=W)
    s5_c2_label.grid(row=18, column=0, sticky=W)
    s5_c3_label.grid(row=19, column=0, sticky=W)
    s5_c4_label.grid(row=20, column=0, sticky=W)
    s5_c5_label.grid(row=21, column=0, sticky=W)
    s5_total_credit_label.grid(row=22, column=0, sticky=W)

    # Semester 2 content

    s2_c1_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=42)
    s2_c2_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=42)
    s2_c3_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=42)
    s2_c4_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=42)
    s2_c5_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=42)
    s2_credits_display_label = Label(home_page, text='               0/16', font=("Arial", 14), bg='#333333',
                                     fg='#FFFFFF', anchor='w', width=42)
    semester2_label = Label(home_page, text='Semester 2:', font=("Arial", 20), bg='#333333', fg='#FFFFFF')
    s2_c1_label = Label(home_page, text='Class 1:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s2_c2_label = Label(home_page, text='Class 2:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s2_c3_label = Label(home_page, text='Class 3:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s2_c4_label = Label(home_page, text='Class 4:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s2_c5_label = Label(home_page, text='Class 5:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s2_total_credit_label = Label(home_page, text='Credits :', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                  anchor='w', width=6)

    # Semester 2 widgets placement

    semester2_label.grid(row=2, column=3, columnspan=2, pady=10)
    s2_c1_display_label.grid(row=3, column=3, columnspan=3)
    s2_c2_display_label.grid(row=4, column=3, columnspan=3)
    s2_c3_display_label.grid(row=5, column=3, columnspan=3)
    s2_c4_display_label.grid(row=6, column=3, columnspan=3)
    s2_c5_display_label.grid(row=7, column=3, columnspan=3)
    s2_credits_display_label.grid(row=8, column=3, columnspan=3)
    s2_c1_label.grid(row=3, column=3, sticky=W)
    s2_c2_label.grid(row=4, column=3, sticky=W)
    s2_c3_label.grid(row=5, column=3, sticky=W)
    s2_c4_label.grid(row=6, column=3, sticky=W)
    s2_c5_label.grid(row=7, column=3, sticky=W)
    s2_total_credit_label.grid(row=8, column=3, sticky=W)

    # Semester 4 content

    s4_c1_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=42)
    s4_c2_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=42)
    s4_c3_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=42)
    s4_c4_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=42)
    s4_c5_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=42)
    s4_credits_display_label = Label(home_page, text='               0/16', font=("Arial", 14), bg='#333333',
                                     fg='#FFFFFF', anchor='w', width=42)
    semester4_label = Label(home_page, text='Semester 4:', font=("Arial", 20), bg='#333333', fg='#FFFFFF')
    s4_c1_label = Label(home_page, text='Class 1:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s4_c2_label = Label(home_page, text='Class 2:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s4_c3_label = Label(home_page, text='Class 3:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s4_c4_label = Label(home_page, text='Class 4:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s4_c5_label = Label(home_page, text='Class 5:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s4_total_credit_label = Label(home_page, text='Credits :', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                  anchor='w', width=6)

    # Semester 4 widgets placement

    semester4_label.grid(row=9, column=3, columnspan=2, pady=10)
    s4_c1_display_label.grid(row=10, column=3, columnspan=3)
    s4_c2_display_label.grid(row=11, column=3, columnspan=3)
    s4_c3_display_label.grid(row=12, column=3, columnspan=3)
    s4_c4_display_label.grid(row=13, column=3, columnspan=3)
    s4_c5_display_label.grid(row=14, column=3, columnspan=3)
    s4_credits_display_label.grid(row=15, column=3, columnspan=3)
    s4_c1_label.grid(row=10, column=3, sticky=W)
    s4_c2_label.grid(row=11, column=3, sticky=W)
    s4_c3_label.grid(row=12, column=3, sticky=W)
    s4_c4_label.grid(row=13, column=3, sticky=W)
    s4_c5_label.grid(row=14, column=3, sticky=W)
    s4_total_credit_label.grid(row=15, column=3, sticky=W)

    # Semester 6 content

    s6_c1_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=42)
    s6_c2_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=42)
    s6_c3_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=42)
    s6_c4_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=42)
    s6_c5_display_label = Label(home_page, text='              Empty', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                anchor='w', width=42)
    s6_credits_display_label = Label(home_page, text='               0/16', font=("Arial", 14), bg='#333333',
                                     fg='#FFFFFF', anchor='w', width=42)
    semester6_label = Label(home_page, text='Semester 6:', font=("Arial", 20), bg='#333333', fg='#FFFFFF')
    s6_c1_label = Label(home_page, text='Class 1:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s6_c2_label = Label(home_page, text='Class 2:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s6_c3_label = Label(home_page, text='Class 3:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s6_c4_label = Label(home_page, text='Class 4:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s6_c5_label = Label(home_page, text='Class 5:', font=("Arial", 14), bg='#333333', fg='#FFFFFF', anchor='w', width=6)
    s6_total_credit_label = Label(home_page, text='Credits :', font=("Arial", 14), bg='#333333', fg='#FFFFFF',
                                  anchor='w', width=6)

    # Semester 6 widgets placemen

    semester6_label.grid(row=16, column=3, columnspan=2, pady=10)
    s6_c1_display_label.grid(row=17, column=3, columnspan=3)
    s6_c2_display_label.grid(row=18, column=3, columnspan=3)
    s6_c3_display_label.grid(row=19, column=3, columnspan=3)
    s6_c4_display_label.grid(row=20, column=3, columnspan=3)
    s6_c5_display_label.grid(row=21, column=3, columnspan=3)
    s6_credits_display_label.grid(row=22, column=3, columnspan=3)
    s6_c1_label.grid(row=17, column=3, sticky=W)
    s6_c2_label.grid(row=18, column=3, sticky=W)
    s6_c3_label.grid(row=19, column=3, sticky=W)
    s6_c4_label.grid(row=20, column=3, sticky=W)
    s6_c5_label.grid(row=21, column=3, sticky=W)
    s6_total_credit_label.grid(row=22, column=3, sticky=W)

    # Add new class functions
    class ClassInfo:
        def __init__(self, prefix, class_num, class_name, credits):
            self.prefix = prefix
            self.class_num = class_num
            self.class_name = class_name
            self.credits = credits

    with open('DMACC Credit Classes.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        add_class = {}
        for row in csv_reader:
            # skip the first line in the file because it is the header
            if line_count == 0:
                line_count += 1
                continue
            # create an item in dictionary county with a key of the county name and a value of the object
            add_class[str(row[0] + row[1])] = ClassInfo(row[0], row[1], row[2], row[3])

    def search_prefixs():
        try:
            invalid_search = 0
            for key in add_class:
                if add_class[key].prefix == search_entry_pre.get().upper():
                    print(add_class[key].prefix + " " + add_class[key].class_num + ": " + add_class[
                        key].class_name + " - Credits: " + add_class[key].credits)
                    invalid_search = invalid_search + 1
            if invalid_search == 0:
                raise ValueError
        except ValueError:
            print("That Prefix Does Not Exist Please Try Again")
        search_entry_pre.delete(0, END)

    def search_nums():
        try:
            invalid_search = 0
            for key in add_class:
                if int(add_class[key].class_num) == int(search_entry_num.get()):
                    print(add_class[key].prefix + " " + add_class[key].class_num + ": " + add_class[
                        key].class_name + " - Credits: " + add_class[key].credits)
                    invalid_search = invalid_search + 1
            if invalid_search == 0:
                raise ValueError
        except ValueError:
            print("Invalid Search Results Please Try Again")
        search_entry_num.delete(0, END)

    def define_totals():
        global TotalClassesS1
        global TotalClassesS2
        global TotalClassesS3
        global TotalClassesS4
        global TotalClassesS5
        global TotalClassesS6
        global TotalCreditS1
        global TotalCreditS2
        global TotalCreditS3
        global TotalCreditS4
        global TotalCreditS5
        global TotalCreditS6
        TotalClassesS1 = 0
        TotalClassesS2 = 0
        TotalClassesS3 = 0
        TotalClassesS4 = 0
        TotalClassesS5 = 0
        TotalClassesS6 = 0
        TotalCreditS1 = 0
        TotalCreditS2 = 0
        TotalCreditS3 = 0
        TotalCreditS4 = 0
        TotalCreditS5 = 0
        TotalCreditS6 = 0
        global current_class_list_s1
        global current_class_list_s2
        global current_class_list_s3
        global current_class_list_s4
        global current_class_list_s5
        global current_class_list_s6
        current_class_list_s1 = []
        current_class_list_s2 = []
        current_class_list_s3 = []
        current_class_list_s4 = []
        current_class_list_s5 = []
        current_class_list_s6 = []
        entry_button_3_del.destroy()

    def add_classes():
        global TotalClassesS1
        global TotalClassesS2
        global TotalClassesS3
        global TotalClassesS4
        global TotalClassesS5
        global TotalClassesS6
        global TotalCreditS1
        global TotalCreditS2
        global TotalCreditS3
        global TotalCreditS4
        global TotalCreditS5
        global TotalCreditS6
        ErrorTotal = 0
        try:
            if int(var.get()) == 1:
                if TotalClassesS1 == 5:
                    raise ValueError
            if int(var.get()) == 2:
                if TotalClassesS2 == 5:
                    raise ValueError
            if int(var.get()) == 3:
                if TotalClassesS3 == 5:
                    raise ValueError
            if int(var.get()) == 4:
                if TotalClassesS4 == 5:
                    raise ValueError
            if int(var.get()) == 5:
                if TotalClassesS5 == 5:
                    raise ValueError
            if int(var.get()) == 0:
                if TotalClassesS6 == 5:
                    raise ValueError
        except ValueError:
            ErrorTotal += 1
            print('You Have Already Signed Up For 5 Classes Semester Please Try To Fill Another Semester')
        try:
            if int(var.get()) == 0:
                raise ValueError
        except ValueError:
            ErrorTotal += 1
            print('Please Select A Semester Before Pressing Enter')

        try:
            invalid_search = 0
            for key in add_class:
                if str(add_class[key].prefix + add_class[key].class_num) == str(
                        search_entry_add.get().upper().replace(" ", "")):
                    invalid_search = invalid_search + 1
                    global ValidSearchKey
                    ValidSearchKey = key
            if invalid_search == 0:
                raise ValueError
        except ValueError:
            ErrorTotal += 1
            print("Invalid Search Results Please Try Again")
        try:
            global current_class_list_s1
            global current_class_list_s2
            global current_class_list_s3
            global current_class_list_s4
            global current_class_list_s5
            global current_class_list_s6

            if int(var.get()) == 1:
                if TotalCreditS1 + int(add_class[ValidSearchKey].credits) <= 16:
                    current_class_list_s1.insert(TotalClassesS1,
                                                 add_class[ValidSearchKey].prefix + add_class[ValidSearchKey].class_num)
                else:
                    raise ValueError
            if int(var.get()) == 2:
                if TotalCreditS2 + int(add_class[ValidSearchKey].credits) <= 16:
                    current_class_list_s2.insert(TotalClassesS2,
                                                 add_class[ValidSearchKey].prefix + add_class[ValidSearchKey].class_num)
                else:
                    raise ValueError
            if int(var.get()) == 3:
                if TotalCreditS3 + int(add_class[ValidSearchKey].credits) <= 16:
                    current_class_list_s3.insert(TotalClassesS3,
                                                 add_class[ValidSearchKey].prefix + add_class[ValidSearchKey].class_num)
                else:
                    raise ValueError
            if int(var.get()) == 4:
                if TotalCreditS4 + int(add_class[ValidSearchKey].credits) <= 16:
                    current_class_list_s4.insert(TotalClassesS4,
                                                 add_class[ValidSearchKey].prefix + add_class[ValidSearchKey].class_num)
                else:
                    raise ValueError
            if int(var.get()) == 5:
                if TotalCreditS5 + int(add_class[ValidSearchKey].credits) <= 16:
                    current_class_list_s5.insert(TotalClassesS5,
                                                 add_class[ValidSearchKey].prefix + add_class[ValidSearchKey].class_num)
                else:
                    raise ValueError
            if int(var.get()) == 6:
                if TotalCreditS6 + int(add_class[ValidSearchKey].credits) <= 16:
                    current_class_list_s6.insert(TotalClassesS6,
                                                 add_class[ValidSearchKey].prefix + add_class[ValidSearchKey].class_num)
                else:
                    raise ValueError
        except ValueError:
            ErrorTotal += 1
            print('Semester ' + str(var.get()) + ' Has A 16 Credit Limit In Which Adding This Class Exceeds That Limit')

        # When Adding A Class To Semester 1 Check If It Has Already Been Signed Up For
        if int(var.get()) == 1:
            # Checks If New Class Is Already Signed Up For In Semester 1
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s1)):
                    if current_class_list_s1[TotalClassesS1] == current_class_list_s1[x]:
                        num_of_matches += 1
                if num_of_matches >= 2:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 1')
            # Checks If New Class Is Already Signed Up For In Semester 2
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s2)):
                    if current_class_list_s1[TotalClassesS1] == current_class_list_s2[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 2')
            # Checks If New Class Is Already Signed Up For In Semester 3
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s3)):
                    if current_class_list_s1[TotalClassesS1] == current_class_list_s3[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 3')
            # Checks If New Class Is Already Signed Up For In Semester 4
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s4)):
                    if current_class_list_s1[TotalClassesS1] == current_class_list_s4[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 4')
            # Checks If New Class Is Already Signed Up For In Semester 5
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s5)):
                    if current_class_list_s1[TotalClassesS1] == current_class_list_s5[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 5')
            # Checks If New Class Is Already Signed Up For In Semester 6
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s6)):
                    if current_class_list_s1[TotalClassesS1] == current_class_list_s6[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 6')

        # When Adding A Class To Semester 2 Check If It Has Already Been Signed Up For
        if int(var.get()) == 2:
            # Checks If New Class Is Already Signed Up For In Semester 1
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s1)):
                    if current_class_list_s2[TotalClassesS2] == current_class_list_s1[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 1')
            # Checks If New Class Is Already Signed Up For In Semester 2
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s2)):
                    if current_class_list_s2[TotalClassesS2] == current_class_list_s2[x]:
                        num_of_matches += 1
                if num_of_matches >= 2:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 2')
            # Checks If New Class Is Already Signed Up For In Semester 3
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s3)):
                    if current_class_list_s2[TotalClassesS2] == current_class_list_s3[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 3')
            # Checks If New Class Is Already Signed Up For In Semester 4
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s4)):
                    if current_class_list_s2[TotalClassesS2] == current_class_list_s4[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 4')
            # Checks If New Class Is Already Signed Up For In Semester 5
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s5)):
                    if current_class_list_s2[TotalClassesS2] == current_class_list_s5[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 5')
            # Checks If New Class Is Already Signed Up For In Semester 6
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s6)):
                    if current_class_list_s2[TotalClassesS2] == current_class_list_s6[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 6')

        # When Adding A Class To Semester 3 Check If It Has Already Been Signed Up For
        if int(var.get()) == 3:
            # Checks If New Class Is Already Signed Up For In Semester 1
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s1)):
                    if current_class_list_s3[TotalClassesS3] == current_class_list_s1[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 1')
            # Checks If New Class Is Already Signed Up For In Semester 2
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s2)):
                    if current_class_list_s3[TotalClassesS3] == current_class_list_s2[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 2')
            # Checks If New Class Is Already Signed Up For In Semester 3
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s3)):
                    if current_class_list_s3[TotalClassesS3] == current_class_list_s3[x]:
                        num_of_matches += 1
                if num_of_matches >= 2:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 3')
            # Checks If New Class Is Already Signed Up For In Semester 4
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s4)):
                    if current_class_list_s3[TotalClassesS3] == current_class_list_s4[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 4')
            # Checks If New Class Is Already Signed Up For In Semester 5
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s5)):
                    if current_class_list_s3[TotalClassesS3] == current_class_list_s5[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 5')
            # Checks If New Class Is Already Signed Up For In Semester 6
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s6)):
                    if current_class_list_s3[TotalClassesS3] == current_class_list_s6[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 6')

        # When Adding A Class To Semester 4 Check If It Has Already Been Signed Up For
        if int(var.get()) == 4:
            # Checks If New Class Is Already Signed Up For In Semester 1
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s1)):
                    if current_class_list_s4[TotalClassesS4] == current_class_list_s1[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 1')
            # Checks If New Class Is Already Signed Up For In Semester 2
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s2)):
                    if current_class_list_s4[TotalClassesS4] == current_class_list_s2[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 2')
            # Checks If New Class Is Already Signed Up For In Semester 3
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s3)):
                    if current_class_list_s4[TotalClassesS4] == current_class_list_s3[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 3')
            # Checks If New Class Is Already Signed Up For In Semester 4
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s4)):
                    if current_class_list_s4[TotalClassesS4] == current_class_list_s4[x]:
                        num_of_matches += 1
                if num_of_matches >= 2:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 4')
            # Checks If New Class Is Already Signed Up For In Semester 5
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s5)):
                    if current_class_list_s4[TotalClassesS4] == current_class_list_s5[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 5')
            # Checks If New Class Is Already Signed Up For In Semester 6
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s6)):
                    if current_class_list_s4[TotalClassesS4] == current_class_list_s6[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 6')

        # When Adding A Class To Semester 5 Check If It Has Already Been Signed Up For
        if int(var.get()) == 5:
            # Checks If New Class Is Already Signed Up For In Semester 1
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s1)):
                    if current_class_list_s5[TotalClassesS5] == current_class_list_s1[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 1')
            # Checks If New Class Is Already Signed Up For In Semester 2
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s2)):
                    if current_class_list_s5[TotalClassesS5] == current_class_list_s2[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 2')
            # Checks If New Class Is Already Signed Up For In Semester 3
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s3)):
                    if current_class_list_s5[TotalClassesS5] == current_class_list_s3[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 3')
            # Checks If New Class Is Already Signed Up For In Semester 4
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s4)):
                    if current_class_list_s5[TotalClassesS5] == current_class_list_s4[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 4')
            # Checks If New Class Is Already Signed Up For In Semester 5
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s5)):
                    if current_class_list_s5[TotalClassesS5] == current_class_list_s5[x]:
                        num_of_matches += 1
                if num_of_matches >= 2:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 5')
            # Checks If New Class Is Already Signed Up For In Semester 6
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s6)):
                    if current_class_list_s5[TotalClassesS5] == current_class_list_s6[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 6')

        # When Adding A Class To Semester 6 Check If It Has Already Been Signed Up For
        if int(var.get()) == 6:
            # Checks If New Class Is Already Signed Up For In Semester 1
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s1)):
                    if current_class_list_s6[TotalClassesS6] == current_class_list_s1[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 1')
            # Checks If New Class Is Already Signed Up For In Semester 2
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s2)):
                    if current_class_list_s6[TotalClassesS6] == current_class_list_s2[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 2')
            # Checks If New Class Is Already Signed Up For In Semester 3
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s3)):
                    if current_class_list_s6[TotalClassesS6] == current_class_list_s3[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 3')
            # Checks If New Class Is Already Signed Up For In Semester 4
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s4)):
                    if current_class_list_s6[TotalClassesS6] == current_class_list_s4[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 4')
            # Checks If New Class Is Already Signed Up For In Semester 5
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s5)):
                    if current_class_list_s6[TotalClassesS6] == current_class_list_s5[x]:
                        num_of_matches += 1
                if num_of_matches >= 1:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 5')
            # Checks If New Class Is Already Signed Up For In Semester 6
            try:
                num_of_matches = 0
                for x in range(len(current_class_list_s6)):
                    if current_class_list_s6[TotalClassesS6] == current_class_list_s6[x]:
                        num_of_matches += 1
                if num_of_matches >= 2:
                    raise ValueError
            except ValueError:
                ErrorTotal += 1
                print('You Have Already Signed Up For That Class In Semester 6')
        if ErrorTotal == 0:
            print('The Class Listed Below Will Be Add To Semester ' + str(var.get()))
            print(add_class[ValidSearchKey].prefix + " " + add_class[ValidSearchKey].class_num + ": " + add_class[
                ValidSearchKey].class_name + " - Credits: " + add_class[ValidSearchKey].credits)

            if int(var.get()) == 1:
                TotalClassesS1 += 1
                TotalCreditS1 += int(add_class[ValidSearchKey].credits)
            elif int(var.get()) == 2:
                TotalClassesS2 += 1
                TotalCreditS2 += int(add_class[ValidSearchKey].credits)
            elif int(var.get()) == 3:
                TotalClassesS3 += 1
                TotalCreditS3 += int(add_class[ValidSearchKey].credits)
            elif int(var.get()) == 4:
                TotalClassesS4 += 1
                TotalCreditS4 += int(add_class[ValidSearchKey].credits)
            elif int(var.get()) == 5:
                TotalClassesS5 += 1
                TotalCreditS5 += int(add_class[ValidSearchKey].credits)
            elif int(var.get()) == 6:
                TotalClassesS6 += 1
                TotalCreditS6 += int(add_class[ValidSearchKey].credits)

            # Change Labels On Current Schedule Page
            if int(var.get()) == 1:
                if TotalClassesS1 == 1:
                    s1_c1_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS1 == 2:
                    s1_c2_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS1 == 3:
                    s1_c3_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS1 == 4:
                    s1_c4_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS1 == 5:
                    s1_c5_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
            elif int(var.get()) == 2:
                if TotalClassesS2 == 1:
                    s2_c1_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS2 == 2:
                    s2_c2_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS2 == 3:
                    s2_c3_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS2 == 4:
                    s2_c4_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS2 == 5:
                    s2_c5_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
            elif int(var.get()) == 3:
                if TotalClassesS3 == 1:
                    s3_c1_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS3 == 2:
                    s3_c2_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS3 == 3:
                    s3_c3_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS3 == 4:
                    s3_c4_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS3 == 5:
                    s3_c5_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
            elif int(var.get()) == 4:
                if TotalClassesS4 == 1:
                    s4_c1_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS4 == 2:
                    s4_c2_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS4 == 3:
                    s4_c3_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS4 == 4:
                    s4_c4_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS4 == 5:
                    s4_c5_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
            elif int(var.get()) == 5:
                if TotalClassesS5 == 1:
                    s5_c1_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS5 == 2:
                    s5_c2_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS5 == 3:
                    s5_c3_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS5 == 4:
                    s5_c4_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS5 == 5:
                    s5_c5_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
            elif int(var.get()) == 6:
                if TotalClassesS6 == 1:
                    s6_c1_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS6 == 2:
                    s6_c2_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS6 == 3:
                    s6_c3_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS6 == 4:
                    s6_c4_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
                if TotalClassesS6 == 5:
                    s6_c5_display_label.config(text='              ' + add_class[ValidSearchKey].class_name)
            s1_credits_display_label.config(text='               ' + str(TotalCreditS1) + '/16')
            s2_credits_display_label.config(text='               ' + str(TotalCreditS2) + '/16')
            s3_credits_display_label.config(text='               ' + str(TotalCreditS3) + '/16')
            s4_credits_display_label.config(text='               ' + str(TotalCreditS4) + '/16')
            s5_credits_display_label.config(text='               ' + str(TotalCreditS5) + '/16')
            s6_credits_display_label.config(text='               ' + str(TotalCreditS6) + '/16')
            search_entry_add.delete(0, END)

        else:
            if int(var.get()) == 1:
                current_class_list_s1.pop()
            if int(var.get()) == 2:
                current_class_list_s2.pop()
            if int(var.get()) == 3:
                current_class_list_s3.pop()
            if int(var.get()) == 4:
                current_class_list_s4.pop()
            if int(var.get()) == 5:
                current_class_list_s5.pop()
            if int(var.get()) == 6:
                current_class_list_s6.pop()

    # Add New Classes Window and Widgets

    add_new_classes = Screen(screen_master, "Add Classes")
    add_new_classes.config(bg="#333333")

    search_label_pre = Label(add_new_classes, text='Enter 3 Letter Prefix To\nSearch For Classes', font=("Arial", 20),
                             fg='#FFFFFF', bg='#333333', pady=10)
    search_label_pre.grid(row=0, column=0, columnspan=2, padx=10)
    global search_entry_pre
    search_entry_pre = Entry(add_new_classes, font=('Arial', 16), width=4)
    search_entry_pre.grid(row=1, column=0, sticky='wens')
    entry_button_1 = Button(add_new_classes, text='Enter', fg="#FFFFFF", bg='#0c2b59', command=search_prefixs)
    entry_button_1.grid(row=1, column=1, sticky='wens')
    search_key_label_1 = Label(add_new_classes, font=("Arial", 11), justify='left', fg='#FFFFFF', bg='#333333',
                               text='ACC - Accounting\nADM - Administrative Assistant\nASM - Aging Services Management\nAGA - Agriculture-Agronomy\nAGB - Agriculture-Farm Management\nAGC - Agriculture-Comprehensive\nAGH - Agriculture-Horticulture\nAGM - Agriculture-Mechanics\nAGP - Agriculture-Precision Ag\nAGS - Agriculture-Animal Science\nAGT - Agriculture-Technology\nAGV - Agriculture-Veterinary Technology\nANI - Animation\nANT - Anthropology\nAPP - Apparel Merchandising\nMLW - Architectural Millwork\nARC - Architectural Technologies\nART - Art\nADN - Associate Degree Nursing\nATC - Auto Tech CAP (Chrysler)\nATF - Ford ASSET\nATG - Auto Tech ASEP (GM)\nAUT - Automotive Technology\nAVI - Aviation\nAVM - Aviation Maintenance\nBIO - Biology\nBPT - Bioprocess Technology\nBMA - Building Maintenance\nBCA - Business Computer Application\nBUS - Business\nCET - Civil Engineering Technology\nCHM - Chemistry\nPEC - Coaching Officiating\nCPR - Collision Repair/Refinishing\nCAD - Computer Aided Drafting\nCIS - Computer Programming\nCOM - Communication\nNET - Computer Networking\nCSC - Computer Science\nCON - Construction\nCRJ - Criminal Justice\nDAT - Data Analytics\nDEA - Dental Assistant\nDHY - Dental Hygiene\nDSL - Diesel\nDRA - Drama-Film and Theatre\nECE - Early Childhood Education\nECN - Economics\nEDU - Education')
    search_key_label_1.grid(row=7, column=0, columnspan=2)

    search_label_num = Label(add_new_classes, text='Enter 3 Digit Course Number\nTo Search For Classes',
                             font=("Arial", 20), fg='#FFFFFF', bg='#333333', pady=10)
    search_label_num.grid(row=0, column=2, columnspan=2, padx=10)
    global search_entry_num
    search_entry_num = Entry(add_new_classes, font=("Arial", 16), width=4)
    search_entry_num.grid(row=1, column=2, sticky='wens')
    entry_button_2 = Button(add_new_classes, command=search_nums, text='Enter', fg="#FFFFFF", bg='#0c2b59')
    entry_button_2.grid(row=1, column=3, sticky='wens')
    search_key_label_2 = Label(add_new_classes, font=("Arial", 11), justify='left', fg='#FFFFFF', bg='#333333',
                               text='ELT - Electronics\nELE - Electrical Technology\nEMS - Emergency Medical Service\nEGR - Engineering\nEGT - Engineering Technology\nENG - English\nELL - English Language Learner\nENV - Environmental Science\nFIN - Finance\nFIR - Fire Science\nFLA - Arabic-Foreign Language\nFLC - Chinese-Foreign Language\nFLF - French-Foreign Language\nFLG - German-Foreign Language\nFLI - Italian-Foreign Language\nFLJ - Japanese-Foreign Language\nFLS - Spanish-Foreign Language\nGEO - Geography\nGLS - Global Studies\nGRD - Graphic Design\nGRT - Graphic Technologies\nHIT - Health Information Technology\nHSC - Health Science\nHCR - Heating and Air Conditioning\nHIS - History\nHON - Honors\nHCM - Hospitality, Culinary & Management\nHSV - Human Services\nHUM - Humanities\nIND - Industrial Technology\nINF - Informatics\nPEV - Intercollegiate Physical Education\nINT - Interior Design\nITR - Interpretation and Translation\nJOU - Journalism\nSRV - Land Surveying\nLIT - Literature\nMGT - Management\nMFG - Manufacturing\nMKT - Marketing\nMMS - Mass Media Studies\nMAT - Mathematics\nMAP - Medical Assistant\nMLT - Medical Lab Technology\nMOR - Mortuary Science\nMUA - Music-applied\nMUS - Music-general\nOPT - Optometric/Ophthalmic Assistant\nPRL - Paralegal')
    search_key_label_2.grid(row=7, column=2, columnspan=2)

    search_label_add = Label(add_new_classes, text='Enter 3 Digit Prefix & Num\n To Add Classes', font=("Arial", 20),
                             fg='#FFFFFF', bg='#333333', pady=10)
    search_label_add.grid(row=0, column=4, columnspan=2, padx=10)
    search_entry_add = Entry(add_new_classes, font=("Arial", 16), width=4)
    search_entry_add.grid(row=1, column=4, sticky='wens')
    entry_button_3 = Button(add_new_classes, text='Enter', fg="#FFFFFF", bg='#0c2b59', command=add_classes)
    entry_button_3.grid(row=1, column=5, sticky='wens')
    entry_button_3_del = Button(add_new_classes, text='Enter', fg="#FFFFFF", bg='#0c2b59',
                                command=lambda: [define_totals(), add_classes()])
    entry_button_3_del.grid(row=1, column=5, sticky='wens')
    search_key_label_3 = Label(add_new_classes, font=("Arial", 11), justify='left', fg='#FFFFFF', bg='#333333',
                               text='PHR - Pharmacy Technology\nPHI - Philosophy\nPHB - Phlebotomy\nPEA - Physical Education Activities\nPEH - Physical Education & Health-General\nPET - Physical Education Training\nPHS - Physical Science\nPHY - Physics\nPOL - Political Science\nPNN - Practical Nursing\nPSY - Psychology\nRRO - Railroad Operations\nRDG - Reading\nCRC - Real Time Reporting\nREL - Religion\nRCP - Respiratory Therapy\nSOC - Sociology\nSPC - Speech\nSDV - Student Development\nSUR - Surgical Technology\nTEL - Telecommunications Technology\nWAT - Water Environmental Technology\nWDV - Web Development\nWEL - Welding\nWTT - Wind Energy & Turbine Technology\nWBL - Work-Based Learning\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    search_key_label_3.grid(row=7, column=4, columnspan=2)

    prefix_grouping_label = Label(add_new_classes,
                                  text='These Below Are The Subject Names\nAnd There Correlated Prefixes',
                                  font=("Arial", 20), fg='#FFFFFF', bg='#333333', pady=5)
    prefix_grouping_label.grid(row=3, column=0, rowspan=2, columnspan=4)

    checkbox_label = Label(add_new_classes, text='Select The Semester Before You Press Enter', font=("Arial", 13),
                           fg='#FFFFFF', bg='#333333', pady=5)
    checkbox_label.grid(row=3, column=4, columnspan=2)

    def sel():
        selection = "You selected Semester " + str(var.get())
        print(selection)

    var = IntVar()
    c1 = Radiobutton(add_new_classes, text='S1', variable=var, width=5, value=1, command=sel)
    c1.grid(row=4, column=4, sticky='w')
    c2 = Radiobutton(add_new_classes, text='S2', variable=var, width=5, value=2, command=sel)
    c2.grid(row=4, column=4)
    c3 = Radiobutton(add_new_classes, text='S3', variable=var, width=5, value=3, command=sel)
    c3.grid(row=4, column=4, sticky='e')
    c4 = Radiobutton(add_new_classes, text='S4', variable=var, width=5, value=4, command=sel)
    c4.grid(row=4, column=5, sticky='w')
    c5 = Radiobutton(add_new_classes, text='S5', variable=var, width=5, value=5, command=sel)
    c5.grid(row=4, column=5)
    c6 = Radiobutton(add_new_classes, text='S6', variable=var, width=5, value=6, command=sel)
    c6.grid(row=4, column=5, sticky='e')

    # Remove Classes Functions

    def remove_class():
        global current_class_list_s1
        global current_class_list_s2
        global current_class_list_s3
        global current_class_list_s4
        global current_class_list_s5
        global current_class_list_s6
        global TotalClassesS1
        global TotalClassesS2
        global TotalClassesS3
        global TotalClassesS4
        global TotalClassesS5
        global TotalClassesS6
        global TotalCreditS1
        global TotalCreditS2
        global TotalCreditS3
        global TotalCreditS4
        global TotalCreditS5
        global TotalCreditS6
        # Remove class if in Semester 1
        for x in range(len(current_class_list_s1)):
            try:
                if str(current_class_list_s1[x]) == str(r_class_entry.get().upper().replace(" ", "")):
                    key = (add_class[current_class_list_s1[x]].prefix+str(add_class[current_class_list_s1[x]].class_num))
                    print(str(current_class_list_s1[x]) + ' Has Been Removed From Semester 1')
                    TotalClassesS1 -= 1
                    TotalCreditS1 -= int(add_class[key].credits)
                    current_class_list_s1.remove(key)
                    s1_c1_display_label.config(text='              Empty')
                    s1_c2_display_label.config(text='              Empty')
                    s1_c3_display_label.config(text='              Empty')
                    s1_c4_display_label.config(text='              Empty')
                    s1_c5_display_label.config(text='              Empty')
                    for x in range(len(current_class_list_s1)):
                        key = (add_class[current_class_list_s1[x]].prefix + str(add_class[current_class_list_s1[x]].class_num))
                        if x == 0:
                            s1_c1_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 1:
                            s1_c2_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 2:
                            s1_c3_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 3:
                            s1_c4_display_label.config(text='              ' + add_class[key].class_name)
                    s1_credits_display_label.config(text='               ' + str(TotalCreditS1) + '/16')
                    r_class_entry.delete(0, END)
            except IndexError:
                pass
        # Remove class if in Semester 2
        for x in range(len(current_class_list_s2)):
            try:
                if str(current_class_list_s2[x]) == str(r_class_entry.get().upper().replace(" ", "")):
                    key = (add_class[current_class_list_s2[x]].prefix+str(add_class[current_class_list_s2[x]].class_num))
                    print(str(current_class_list_s2[x]) + ' Has Been Removed From Semester 2')
                    TotalClassesS2 -= 1
                    TotalCreditS2 -= int(add_class[key].credits)
                    current_class_list_s2.remove(key)
                    s2_c1_display_label.config(text='              Empty')
                    s2_c2_display_label.config(text='              Empty')
                    s2_c3_display_label.config(text='              Empty')
                    s2_c4_display_label.config(text='              Empty')
                    s2_c5_display_label.config(text='              Empty')
                    for x in range(len(current_class_list_s2)):
                        key = (add_class[current_class_list_s2[x]].prefix + str(add_class[current_class_list_s2[x]].class_num))
                        if x == 0:
                            s2_c1_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 1:
                            s2_c2_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 2:
                            s2_c3_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 3:
                            s2_c4_display_label.config(text='              ' + add_class[key].class_name)
                    s2_credits_display_label.config(text='               ' + str(TotalCreditS2) + '/16')
            except IndexError:
                pass
        # Remove class if in Semester 3
        for x in range(len(current_class_list_s3)):
            try:
                if str(current_class_list_s3[x]) == str(r_class_entry.get().upper().replace(" ", "")):
                    key = (add_class[current_class_list_s3[x]].prefix+str(add_class[current_class_list_s3[x]].class_num))
                    print(str(current_class_list_s3[x]) + ' Has Been Removed From Semester 3')
                    TotalClassesS3 -= 1
                    TotalCreditS3 -= int(add_class[key].credits)
                    current_class_list_s3.remove(key)
                    s3_c1_display_label.config(text='              Empty')
                    s3_c2_display_label.config(text='              Empty')
                    s3_c3_display_label.config(text='              Empty')
                    s3_c4_display_label.config(text='              Empty')
                    s3_c5_display_label.config(text='              Empty')
                    for x in range(len(current_class_list_s3)):
                        key = (add_class[current_class_list_s3[x]].prefix + str(add_class[current_class_list_s3[x]].class_num))
                        if x == 0:
                            s3_c1_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 1:
                            s3_c2_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 2:
                            s3_c3_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 3:
                            s3_c4_display_label.config(text='              ' + add_class[key].class_name)
                    s3_credits_display_label.config(text='               ' + str(TotalCreditS3) + '/16')
                    r_class_entry.delete(0, END)
            except IndexError:
                pass
        # Remove class if in Semester 4
        for x in range(len(current_class_list_s4)):
            try:
                if str(current_class_list_s4[x]) == str(r_class_entry.get().upper().replace(" ", "")):
                    key = (add_class[current_class_list_s4[x]].prefix+str(add_class[current_class_list_s4[x]].class_num))
                    print(str(current_class_list_s4[x]) + ' Has Been Removed From Semester 4')
                    TotalClassesS4 -= 1
                    TotalCreditS4 -= int(add_class[key].credits)
                    current_class_list_s4.remove(key)
                    s4_c1_display_label.config(text='              Empty')
                    s4_c2_display_label.config(text='              Empty')
                    s4_c3_display_label.config(text='              Empty')
                    s4_c4_display_label.config(text='              Empty')
                    s4_c5_display_label.config(text='              Empty')
                    for x in range(len(current_class_list_s4)):
                        key = (add_class[current_class_list_s4[x]].prefix + str(add_class[current_class_list_s4[x]].class_num))
                        if x == 0:
                            s4_c1_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 1:
                            s4_c2_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 2:
                            s4_c3_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 3:
                            s4_c4_display_label.config(text='              ' + add_class[key].class_name)
                    s4_credits_display_label.config(text='               ' + str(TotalCreditS4) + '/16')
                    r_class_entry.delete(0, END)
            except IndexError:
                pass
        # Remove class if in Semester 5
        for x in range(len(current_class_list_s5)):
            try:
                if str(current_class_list_s5[x]) == str(r_class_entry.get().upper().replace(" ", "")):
                    key = (add_class[current_class_list_s5[x]].prefix+str(add_class[current_class_list_s5[x]].class_num))
                    print(str(current_class_list_s5[x]) + ' Has Been Removed From Semester 5')
                    TotalClassesS5 -= 1
                    TotalCreditS5 -= int(add_class[key].credits)
                    current_class_list_s5.remove(key)
                    s5_c1_display_label.config(text='              Empty')
                    s5_c2_display_label.config(text='              Empty')
                    s5_c3_display_label.config(text='              Empty')
                    s5_c4_display_label.config(text='              Empty')
                    s5_c5_display_label.config(text='              Empty')
                    for x in range(len(current_class_list_s5)):
                        key = (add_class[current_class_list_s5[x]].prefix + str(add_class[current_class_list_s5[x]].class_num))
                        if x == 0:
                            s5_c1_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 1:
                            s5_c2_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 2:
                            s5_c3_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 3:
                            s5_c4_display_label.config(text='              ' + add_class[key].class_name)
                    s5_credits_display_label.config(text='               ' + str(TotalCreditS5) + '/16')
                    r_class_entry.delete(0, END)
            except IndexError:
                pass
        # Remove class if in Semester 6
        for x in range(len(current_class_list_s6)):
            try:
                if str(current_class_list_s6[x]) == str(r_class_entry.get().upper().replace(" ", "")):
                    key = (add_class[current_class_list_s6[x]].prefix+str(add_class[current_class_list_s6[x]].class_num))
                    print(str(current_class_list_s6[x]) + ' Has Been Removed From Semester 6')
                    TotalClassesS6 -= 1
                    TotalCreditS6 -= int(add_class[key].credits)
                    current_class_list_s6.remove(key)
                    s6_c1_display_label.config(text='              Empty')
                    s6_c2_display_label.config(text='              Empty')
                    s6_c3_display_label.config(text='              Empty')
                    s6_c4_display_label.config(text='              Empty')
                    s6_c5_display_label.config(text='              Empty')
                    for x in range(len(current_class_list_s6)):
                        key = (add_class[current_class_list_s6[x]].prefix + str(add_class[current_class_list_s6[x]].class_num))
                        if x == 0:
                            s6_c1_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 1:
                            s6_c2_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 2:
                            s6_c3_display_label.config(text='              ' + add_class[key].class_name)
                        if x == 3:
                            s6_c4_display_label.config(text='              ' + add_class[key].class_name)
                    s6_credits_display_label.config(text='               ' + str(TotalCreditS6) + '/16')
                    r_class_entry.delete(0, END)
            except IndexError:
                pass

    remove_classes = Screen(screen_master, 'Remove Classes')
    remove_classes.config(bg='#333333')
    r_class_label = Label(remove_classes, text='Enter The Class You Wish\nTo Remove And Press Enter',
                          font=("Arial", 14), bg='#333333', fg='#FFFFFF', width=37, pady=20)
    r_class_label.grid(row=0, column=0)
    r_class_entry = Entry(remove_classes, font=("Arial", 16))
    r_class_entry.grid(row=1, column=0)
    r_class_button = Button(remove_classes, text='Enter', fg="#FFFFFF", bg='#0c2b59', width=7, height=3, command=remove_class)
    r_class_button.grid(row=2, column=0)


    # Tuition Page Functions
    def calculate_tuition():
        global TotalCreditS1
        global TotalCreditS2
        global TotalCreditS3
        global TotalCreditS4
        global TotalCreditS5
        global TotalCreditS6
        all_credits = TotalCreditS1 + TotalCreditS2 + TotalCreditS3 + TotalCreditS4 + TotalCreditS5 + TotalCreditS6
        in_state = all_credits * 178
        out_state = all_credits * 356
        instate_label.config(text='Total In-State Tuition For All Of Your Semesters Is: $'+ str(in_state))
        outstate_label.config(text="Total Out of State Tuition For All Of Your Semesters Is: $"+ str(out_state))
    # Tuition Total Page
    tuition_total = Screen(screen_master, 'Tuition Total')
    tuition_total.config(bg='#333333')

    instate_label = Label(tuition_total, text='Total In-State Tuition For All Of Your Semesters Is: $0', font=("Arial", 20), bg='#333333', fg='#FFFFFF', width=50, pady=20)
    instate_label.grid(row=0, column=0, sticky='wens')
    outstate_label = Label(tuition_total, text='Total Out of State Tuition For All Of Your Semesters Is: $0', font=("Arial", 20), bg='#333333', fg='#FFFFFF', width=50, pady=20)
    outstate_label.grid(row=1, column=0, sticky='wens')








    admin_page = Screen(screen_master, 'Admin Settings')
    admin_page.config(bg='#333333')
    does_not_exist = Label(admin_page, text='404 This Page Does Not Exist', font=("Arial", 36), bg='#333333',fg='#FFFFFF', width=37, pady=20)
    does_not_exist.grid(row=0, columnspan=2)
    home_page.show()
    window.mainloop()


if __name__ == '__main__':
    create_login_window()
    create_window()
