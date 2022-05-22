from collections import Counter
from dataclasses import dataclass
from tkinter import *
from tkinter.messagebox import showinfo
from csv import DictReader
from random import randint


# -------------------------------------------------------------------------------------------------------------------- #
def main():
    root = Tk()
    WindowLogin(root, "Login")
    return None


# -------------------------------------------------------------------------------------------------------------------- #
class WindowLogin:
    # Class constructor
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        # key bindings
        self.root.bind("<Return>", self.login)
        self.root.bind("<Escape>", self.close)
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
        self.myButton = Button(self.root, text="login", width=10, command=lambda: self.login(self))
        self.myButton.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        # GUI loop
        self.root.mainloop()

    # show password toggle
    def show_password(self):

        if self.password_entry.cget("show") == "*":
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def login(self, event):
        # username = admin
        # password = admin
        if self.username_entry.get() == "admin" and self.password_entry.get() == "admin":
            showinfo("Login successful", "Welcome to Going Fishing!")
            # open new window
            # destroy current window
            self.root.destroy()
            # create new window from the WindowFishGame class
            root = Tk()
            WindowFishGame(root, "Fish Game")
        else:
            showinfo("Login", "Invalid username or password")

    def close(self, event):
        self.root.destroy()


# -------------------------------------------------------------------------------------------------------------------- #
class WindowFishGame:
    # Class constructor
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)
        self.root.config(bg="#dfe0e2")
        # ---------------------------------------------------------------------------------
        # load fish data
        self.fish_data = self.load_fish_data()
        # random number 1-6
        self.random_number = randint(1, 6)
        # vars used to store fish data
        self.players_fish_list = []
        self.players_kept_fish_list = []
        self.players_illegal_fish_list = []
        self.players_released_fish_list = []
        self.players_total_points = 0

        # fish template class
        @dataclass()
        class FishTemplate:
            def __init__(self, name, keeper, fish, points_kept, points_released):
                self.name = name
                self.keeper = keeper
                self.fish = fish
                self.points_kept = points_kept
                self.points_released = points_released

        # Fish objects
        self.king_george_whiting = FishTemplate(self.fish_data[0]["Name"],
                                                self.fish_data[0]["Keeper"],
                                                self.fish_data[0]["Fish"],
                                                self.fish_data[0]["Points if kept"],
                                                self.fish_data[0]["Points if released"])

        self.lost_bait = FishTemplate(self.fish_data[1]["Name"],
                                      self.fish_data[1]["Keeper"],
                                      self.fish_data[1]["Fish"],
                                      self.fish_data[1]["Points if kept"],
                                      self.fish_data[1]["Points if released"])

        self.small_mulloway = FishTemplate(self.fish_data[2]["Name"],
                                           self.fish_data[2]["Keeper"],
                                           self.fish_data[2]["Fish"],
                                           self.fish_data[2]["Points if kept"],
                                           self.fish_data[2]["Points if released"])

        self.snapper = FishTemplate(self.fish_data[3]["Name"],
                                    self.fish_data[3]["Keeper"],
                                    self.fish_data[3]["Fish"],
                                    self.fish_data[3]["Points if kept"],
                                    self.fish_data[3]["Points if released"])

        self.large_mullet = FishTemplate(self.fish_data[4]["Name"],
                                         self.fish_data[4]["Keeper"],
                                         self.fish_data[4]["Fish"],
                                         self.fish_data[4]["Points if kept"],
                                         self.fish_data[4]["Points if released"])

        self.seaweed_monster = FishTemplate(self.fish_data[5]["Name"],
                                            self.fish_data[5]["Keeper"],
                                            self.fish_data[5]["Fish"],
                                            self.fish_data[5]["Points if kept"],
                                            self.fish_data[5]["Points if released"])

        # fish GUI ------------------------------------------------------------------------
        self.fish_name_label = Label(self.root, text="Fish Name: ", width=20)
        self.fish_name_label.grid(row=0, column=0, padx=10, pady=5)

        self.fish_name_label_two = Label(self.root, width=45, text="")
        self.fish_name_label_two.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

        self.player_points_label = Label(self.root, text="Player Points: ", width=20)
        self.player_points_label.grid(row=2, column=0, padx=10, pady=5)

        self.player_points_label_two = Label(self.root, text="", width=45)
        self.player_points_label_two.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

        # buttons
        self.go_fishing_button = Button(self.root, text="Go Fishing", width=20, height=3, command=self.go_fishing)
        self.go_fishing_button.grid(row=3, column=0, padx=10, pady=5)

        self.keep_fish_button = Button(self.root, text="Keep Fish", width=20, height=3, command=self.keep_fish)
        self.keep_fish_button.grid(row=3, column=1, padx=10, pady=5)
        self.keep_fish_button.config(state=DISABLED)

        self.release_fish_button = Button(self.root, text="Release Fish", width=20, height=3, command=self.release_fish)
        self.release_fish_button.grid(row=3, column=2, padx=10, pady=5)
        self.release_fish_button.config(state=DISABLED)

        self.finish_fishing_button = Button(self.root, text="Finish Fishing", width=70,
                                            command=lambda: self.finish_fishing(self.players_total_points,
                                                                                self.players_kept_fish_list,
                                                                                self.players_released_fish_list,
                                                                                self.players_illegal_fish_list))
        self.finish_fishing_button.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

        self.root.mainloop()
        # GUI loop ------------------------------------------------------------------------

    def go_fishing(self):
        # random number 1-6
        self.random_number = randint(1, 6)
        self.fish_name_label_two.config(fg='black')

        if self.random_number == 1:
            self.fish_name_label_two.config(text=self.king_george_whiting.name)
            self.players_fish_list.append(self.king_george_whiting)
            self.go_fishing_button.config(state=DISABLED)
            self.keep_fish_button.config(state=NORMAL)
            self.release_fish_button.config(state=NORMAL)

        elif self.random_number == 2:
            self.fish_name_label_two.config(text=self.lost_bait.name)
            self.players_fish_list.append(self.lost_bait)
            self.go_fishing_button.config(state=DISABLED)
            self.keep_fish_button.config(state=NORMAL)
            self.release_fish_button.config(state=NORMAL)

        elif self.random_number == 3:
            self.fish_name_label_two.config(text=self.small_mulloway.name)
            self.players_fish_list.append(self.small_mulloway)
            self.go_fishing_button.config(state=DISABLED)
            self.keep_fish_button.config(state=NORMAL)
            self.release_fish_button.config(state=NORMAL)

        elif self.random_number == 4:
            self.fish_name_label_two.config(text=self.snapper.name)
            self.players_fish_list.append(self.snapper)
            self.go_fishing_button.config(state=DISABLED)
            self.keep_fish_button.config(state=NORMAL)
            self.release_fish_button.config(state=NORMAL)

        elif self.random_number == 5:
            self.fish_name_label_two.config(text=self.large_mullet.name)
            self.players_fish_list.append(self.large_mullet)
            self.go_fishing_button.config(state=DISABLED)
            self.keep_fish_button.config(state=NORMAL)
            self.release_fish_button.config(state=NORMAL)

        elif self.random_number == 6:
            self.fish_name_label_two.config(text=self.seaweed_monster.name)
            self.players_fish_list.append(self.seaweed_monster)
            self.go_fishing_button.config(state=DISABLED)
            self.keep_fish_button.config(state=NORMAL)
            self.release_fish_button.config(state=NORMAL)

    def keep_fish(self):
        current_fish_value = self.fish_name_label_two.cget("text")
        current_fish = next(z for z in self.fish_data if z["Name"] == current_fish_value)

        if current_fish["Keeper"] == "Y":
            self.players_kept_fish_list.append(current_fish)
            self.players_total_points += int(current_fish["Points if kept"])
            self.player_points_label_two.config(text=self.players_total_points)
            self.go_fishing_button.config(state=NORMAL)
            self.keep_fish_button.config(state=DISABLED)
            self.release_fish_button.config(state=DISABLED)

        else:
            self.players_illegal_fish_list.append(current_fish)
            self.players_total_points += int(current_fish["Points if kept"])
            self.player_points_label_two.config(text=self.players_total_points)
            self.fish_name_label_two.config(fg='red', text="This fish is not a keeper")
            self.go_fishing_button.config(state=NORMAL)
            self.keep_fish_button.config(state=DISABLED)
            self.release_fish_button.config(state=DISABLED)

    def release_fish(self):
        current_fish_value = self.fish_name_label_two.cget("text")
        current_fish = next(z for z in self.fish_data if z["Name"] == current_fish_value)
        self.players_released_fish_list.append(current_fish)

        self.players_total_points += int(current_fish["Points if released"])
        self.player_points_label_two.config(text=self.players_total_points)
        self.go_fishing_button.config(state=NORMAL)
        self.keep_fish_button.config(state=DISABLED)
        self.release_fish_button.config(state=DISABLED)

    @classmethod
    def finish_fishing(cls,
                       players_points, players_kept_fish_list, players_released_fish_list, players_illegal_fish_list):
        root = Tk()
        root.title("Fishing Results")

        # display how many times a player as a type of fish in kept fish
        kept_fish_count = Counter(fish["Name"] for fish in players_kept_fish_list)
        kept_fish_count_list = list(kept_fish_count.items())
        row_index = 0
        for fish in enumerate(kept_fish_count_list):
            Label(root, width=70, height=2, anchor="w", bg="#53917e", text=f"Fish you kept: {fish}").grid(row=row_index,
                                                                                                          column=0)
            row_index += 1

        # display how many times a player as a type of fish in illegal fish
        illegal_fish_count = Counter(fish["Name"] for fish in players_illegal_fish_list)
        illegal_fish_count_list = list(illegal_fish_count.items())
        row_index = 50
        for fish in enumerate(illegal_fish_count_list):
            Label(root, width=70, height=2, anchor="w", bg="#db5461", text=f"Illegal Fish you kept: {fish}").grid(
                row=row_index, column=0)
            row_index += 1

        # display how many times a player as a type of fish in released fish
        released_fish_count = Counter(fish["Name"] for fish in players_released_fish_list)
        released_fish_count_list = list(released_fish_count.items())
        row_index = 100
        for fish in enumerate(released_fish_count_list):
            Label(root, width=70, height=2, anchor="w", bg="#fcd0a1", text=f"Fish you released: {fish}").grid(
                row=row_index, column=0)
            row_index += 1

        # display players total points after fishing
        Label(root, text=f"Total points: {players_points}").grid(row=150, column=0)

    @classmethod
    def load_fish_data(cls):
        with open('Fish.csv', 'r') as csv_file_in_memory:
            dict_reader = DictReader(csv_file_in_memory)
            list_of_dict = list(dict_reader)
            return list_of_dict


# -------------------------------------------------------------------------------------------------------------------- #
if __name__ == '__main__':
    main()
