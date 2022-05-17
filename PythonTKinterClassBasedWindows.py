from tkinter import *
from csv import DictReader

list_of_dict = {}


def main():
    root = Tk()
    WindowLogin(root, "Login")
    return None


def load_fish_data():
    global list_of_dict

    with open('Fish.csv', 'r') as csv_file_in_memory:
        dict_reader = DictReader(csv_file_in_memory)
        list_of_dict = list(dict_reader)
        print(list_of_dict)


# -------------------------------------------------------------------------------------------------------------------- #
class WindowLogin:
    # Class constructor
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        # username
        self.username_label = Label(self.root, text="Username")
        self.username_label.grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = Entry(self.root, width=30)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        # password
        self.password_label = Label(self.root, text="Password")
        self.password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = Entry(self.root, width=30, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)
        # show password toggle
        self.myCheckButton = Checkbutton(text="show password", command=self.show_password)
        self.myCheckButton.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        # login button
        self.myButton = Button(self.root, text="login", width=10, command=self.login)
        self.myButton.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        # GUI loop
        self.root.mainloop()

    def show_password(self):

        if self.password_entry.cget("show") == "*":
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def login(self):
        # username = admin
        # password = admin
        if self.username_entry.get() == "admin" and self.password_entry.get() == "admin":
            print("Login successful")
            # open new window
            self.root.destroy()
            root = Tk()
            WindowFishGame(root, "Fish Game", "400x400")
        else:
            print("Login failed")


# -------------------------------------------------------------------------------------------------------------------- #
class WindowFishGame:
    # Class constructor
    def __init__(self, root, title, geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)  # 400x400

        self.fish_name_label = Label(self.root, text="Fish Name")
        self.fish_name_label.pack(side=LEFT, padx=10, pady=5)

        self.root.mainloop()


if __name__ == '__main__':
    main()
