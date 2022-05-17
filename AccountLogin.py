import tkinter as tk
from tkinter import ttk


class AccountLoginApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(WindowOne)
        # self.geometry('500x300')

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


# login window
class WindowOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Username").grid(row=0, column=0)
        tk.Label(self, text="Password").grid(row=1, column=0)
        tk.Entry(self, width=20).grid(row=0, column=1)
        tk.Entry(self, width=20, show="*").grid(row=1, column=1)
        # mirror = tk.Entry.cget()
        # tk.Entry(self, width=20, mirror)
        tk.Checkbutton(self, text="show password",
                       command=self.show_password).grid(row=3, column=0)
        tk.Button(self, text="Login",
                  command=lambda: master.switch_frame(WindowTwo)).grid(row=3, column=0, columnspan=2)

    def show_password(self):
        print("sdsds")






# application window
class WindowTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is the page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Open Window One", command=lambda: master.switch_frame(WindowOne)).pack()


# scripts that will run
if __name__ == '__main__':
    app = AccountLoginApp()
    app.mainloop()
