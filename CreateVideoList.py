import tkinter as tk
import video_library as lib
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
import time
from tkinter import messagebox

maxOfRangeLibrary = 6
class CreateVideoList:
    def __init__(self,root):
        self.root = root
        self.root.title("Create Video List")

        self.checkbox_vars = []
        self.entries = []
        self.detail_label = ttk.Label(self.root, text="", wraplength=300)
        self.detail_label.pack()
    
        self.last_checked_name = ""  # Store the last checked video name
        self.last_unchecked_name = ""  # Store the last unchecked video name


        self.create_checkboxes()
        self.create_button()

    def create_checkboxes(self):
            # names_directors = [
            #     "Tom and Jerry - Fred Quimby",
            #     "Breakfast at Tiffany's - Blake Edwards",
            #     "Casablanca - Michael Curtiz",
            #     "The Sound of Music - Robert Wise",
            #     "Gone with the Wind - Victor Fleming"
            # ]
        if len(lib.library) <= maxOfRangeLibrary:
            for idx in range(len(lib.library)):
                frame = ttk.Frame(self.root)
                frame.pack(fill=tk.X)  # Adjust the packing method

                strKey = str(idx + 1).zfill(2)
                name = lib.get_name(strKey)
                director = lib.get_director(strKey)
                rating = lib.get_rating(strKey)

                video_info_with_rating = f"{name} - {director} (Rating: {rating})"

                var = ttk.IntVar()
                checkbox = tk.Checkbutton(frame, text=video_info_with_rating, variable=var)
                checkbox.grid(row=0, column=0, sticky="w")  # Adjust grid layout

                entry = tk.Entry(frame, width=5)  # Adjust entry width as needed
                entry.grid(row=0, column=1, padx=10)  # Adjust grid layout
                self.entries.append(entry)

                self.checkbox_vars.append(var)

                checkbox.config(command=lambda idx=idx: self.checkbox_checked(idx))
        else:
            messagebox.showerror("NOT VALID", "Check Again Please !!!!")


    def checkbox_checked(self, idx):
        entry_value = self.entries[idx].get()
        checkbox_status = self.checkbox_vars[idx].get()

        if checkbox_status == 1:
            print(f"Checkbox at position {idx} is checked. Entry value: {entry_value}")
            self.last_checked_name = lib.get_name(str(idx + 1))  # Store the last checked video name
            # self.last_unchecked_name = ""  # Reset the unchecked name
            self.show_detail()
        else:
            print(f"Checkbox at position {idx} is unchecked.")
            self.last_unchecked_name = lib.get_name(str(idx + 1))  # Store the last unchecked video name
            self.show_detail()

    def show_detail(self):
        if self.last_checked_name:
            self.detail_label.config(text=f"Selected: {self.last_checked_name}")
        elif self.last_unchecked_name:
            self.detail_label.config(text=f"Unchecked: {self.last_unchecked_name}")

    def create_button(self):
        button = tk.Button(self.root, text="Play", command=self.play, width=50, height=1)
        button.pack()
        reset_button = tk.Button(self.root, text="Reset", command=self.reset, width=50, height=1)  # Add a Reset button
        reset_button.pack()

    def print_last_details(self):
        if self.last_checked_name:
            self.print_detail(str(self.last_checked_name))
        elif self.last_unchecked_name:
            self.print_detail(str(self.last_unchecked_name))

    def play(self):
        checked_indices = [idx for idx, var in enumerate(self.checkbox_vars) if var.get() == 1]
        for idx in checked_indices:
            key = str(idx + 1).zfill(2)  # Assuming keys start from 1 in your library
            count = lib.increment_play_count(key)
            play_count = lib.get_play_count(key)
            print(f"Play count for video {lib.get_name(key)}: {play_count}")
            self.entries[idx].delete(0, tk.END)  # Clear previous entry content
            self.entries[idx].insert(tk.END, str(play_count))  # Update entry with play count
            
    def reset(self):
        # Reset the last checked and unchecked names to empty strings
        self.last_checked_name = ""
        self.last_unchecked_name = ""
        self.show_detail()  # Update the detail label to reflect the reset

        # Reset the checkboxes and corresponding entry widgets
        for idx, var in enumerate(self.checkbox_vars):
            var.set(0)  # Uncheck the checkboxes
            self.entries[idx].delete(0, tk.END)  # Clear entry content
            self.entries[idx].insert(tk.END, " ")  # Insert 0 as play count

            # Reset the play count in the video library
            key = str(idx + 1)
            self.detail_label.config(text="")
            #lib.set_play_count(key, 0)  # Reset play count to 0 for the video
    def erase_label(self):
        self.detail_label.config(text="")

# def main():

if __name__ == "__main__":
    root = tk.Tk()
    app = CreateVideoList(root)
    root.mainloop()

