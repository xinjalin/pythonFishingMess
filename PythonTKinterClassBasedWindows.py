from tkinter import *


def main():
    root = Tk()
    window_login = WindowLogin(root, "Login")
    # window_fish_game = WindowFishGame(root, "Fish Game", "400x400")  # docent work
    return None


class WindowLogin:

    def __init__(self, root, title):
        self.root = root
        self.root.title(title)

        self.username_label = Label(self.root, text="Username")
        self.username_label.grid(row=0, column=0, padx=10, pady=5)

        self.username_entry = Entry(self.root, width=30)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = Label(self.root, text="Password")
        self.password_label.grid(row=1, column=0, padx=10, pady=5)

        self.password_entry = Entry(self.root, width=30, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.myCheckButton = Checkbutton(text="show password", command=self.show_password)
        self.myCheckButton.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.myButton = Button(self.root, text="login", width=10, command=self.login)
        self.myButton.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.root.mainloop()
        pass

    def show_password(self):

        if self.password_entry.cget("show") == "*":
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
        pass

    def login(self):

        if self.username_entry.get() == "admin" and self.password_entry.get() == "admin":
            print("Login successful")
            # open new window
            self.root.destroy()
            root = Tk()
            window_fish_game = WindowFishGame(root, "Fish Game", "400x400")
            pass
        else:
            print("Login failed")
        pass

    pass


class WindowFishGame:

    def __init__(self, root, title, geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)  # formatted as "width x height"

        self.fish_name_label = Label(self.root, text="fish name")
        self.fish_name_label.pack(side=LEFT, padx=10, pady=5)

        self.root.mainloop()
        pass

    pass


if __name__ == '__main__':
    main()
