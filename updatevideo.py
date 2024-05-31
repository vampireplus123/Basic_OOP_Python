import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts
import ttkbootstrap as ttk
# Function to set text content in a text area
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateVideos():
# Class to handle updating videos
    # Constructor for the update videos window
    def __init__(self, root):
        # Create a new main or top-level window, depending on root parameter
        if root == None:
            window = tk.Tk()
            fonts.configure()  # Configure fonts
        else:
            window = tk.Toplevel(root)
            
        # Set window dimensions and title
        window.geometry("1000x580")
        window.title("Update Videos")
        
        # Create labels, text entry fields, and buttons
        enter_new_lbl = ttk.Label(window, text="Enter Video Number to update")
        enter_new_lbl.grid(row=1, column=0, padx=0, pady=0)
        
        self.input_new_txt = ttk.Entry(window, width=3)
        self.input_new_txt.grid(row=1, column=1, padx=0, pady=0)
        
        rating_lbl = ttk.Label(window, text="Enter New Rating")
        rating_lbl.grid(row=1, column=3, padx=10, pady=10)

        self.rating_input_txt = ttk.Entry(window, width=20)
        self.rating_input_txt.grid(row=1, column=4, padx=10, pady=10)

        # name_lbl = ttk.Label(window, text="Enter New Name")
        # name_lbl.grid(row=2, column=3, padx=10, pady=10)

        # self.name_input_txt = ttk.Entry(window, width=20)
        # self.name_input_txt.grid(row=2, column=4, padx=5, pady=5)

        # director_lbl = ttk.Label(window, text="Enter New Director")
        # director_lbl.grid(row=3, column=3, padx=5, pady=5)

        # self.director_input_txt = ttk.Entry(window, width=20)
        # self.director_input_txt.grid(row=3, column=4, padx=10, pady=10)
        
       
        check_video_btn = ttk.Button(window, text="Update Video", command=self.update_video_clicked)
        check_video_btn.grid(row=4, column=3, padx=10, pady=10)
        
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=3, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=4, column=0, sticky="NW", padx=10, pady=10)
        
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=5, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        
        # Populate the video list and start the GUI main loop if not a child window
        self.list_videos_clicked()
        if root == None:
            window.mainloop()  

    # Function to list all videos
    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

    """
    This function updates the ratings of videos using the set_rating function
    from the videolibrary.py file and displays it in the text box using the 
    get_rating function.
    """
    def update_video_clicked(self):
        try:
            key = self.input_new_txt.get().zfill(2)
            # changeName = self.name_input_txt.get()
            # changeDirector = self.director_input_txt.get()
            chanegRating = int(self.rating_input_txt.get())

            if key == "":
                set_text(self.video_txt, f"Video {key} not found")
            else:
                name = lib.get_name(key)
                director = lib.get_director(key)
                rating = lib.get_rating(key)
                play_count = lib.get_play_count(key)

                if chanegRating != "" and (chanegRating >= 1) and (chanegRating <= 5):
                    self.ChangeTheRating(key,chanegRating)
                    rating = chanegRating
                else:
                    messagebox.showwarning("invalid rating", "Rating must be between 1 and 5")
                    
                # if changeName != "":
                #     self.ChangeTheName(key, changeName)
                #     name = changeName

                # if changeDirector != "":
                #     self.ChangeTheDirector(key, changeDirector)
                #     director = changeDirector

                video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
                set_text(self.video_txt, video_details)
                self.list_videos_clicked()
                
        except ValueError:
            pass

        self.status_lbl.configure(text="Update Video button was clicked!")

    def ChangeTheRating(self,key,rating):
        r = lib.set_rating(key, rating)
        name = lib.get_name(key)
        director = lib.get_director(key)
        rating = lib.get_rating(key)
        play_count = lib.get_play_count(key)
        video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
        set_text(self.video_txt, video_details)
        self.list_videos_clicked()
        
    def ChangeTheName(self,key,name):
        name = lib.set_name(key, name)
        director = lib.get_director(key)
        rating = lib.get_rating(key)
        play_count = lib.get_play_count(key)
        video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
        set_text(self.video_txt, video_details)
        self.list_videos_clicked()

    def ChangeTheDirector(self,key,director):
        name = lib.get_name(key)
        director = lib.set_ditector(key,director)
        rating = lib.get_rating(key)
        play_count = lib.get_play_count(key)
        video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
        set_text(self.video_txt, video_details)
        self.list_videos_clicked()

# Entry point of the script
if __name__ == "__main__":
    # Create an instance of UpdateVideos class with a main window (None)
    UpdateVideos(None)