from tkinter import *


class LoginFrame:
    def __init__(self, master):
        self.fishing_frame = None
        self.master = master
        Frame(master)

        root.title("Bag Alert")
        root.resizable(False, False)

        self.username_label = Label(master, text="Username")
        self.username_label.grid(row=0, column=0, padx=10, pady=5)

        self.username_entry = Entry(master, width=30)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = Label(master, text="Password")
        self.password_label.grid(row=1, column=0, padx=10, pady=5)

        self.password_entry = Entry(master, width=30, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.myCheckButton = Checkbutton(text="show password", command=self.show_password)
        self.myCheckButton.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.myButton = Button(master, text="login", width=10, command="#")
        self.myButton.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def show_password(self):
        if self.password_entry.cget("show") == "*":
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    # I want to swap the frames LoginFrame and FishingFrame reset the layout of the frames


class FishingFrame:
    def __init__(self, container):
        self.container = container
        application_frame = Frame(container)
        application_frame.pack()
        root.title("page 2")

        self.myButton = Button(container, text="back", width=10, command="#")
        self.myButton.pack()


# scripts that will run
if __name__ == '__main__':
    root = Tk()
    login = LoginFrame(root)
    root.mainloop()
