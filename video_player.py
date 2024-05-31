import tkinter as tk
import tkinter.font as tkfont
import font_manager as fonts
from check_videos_one import CheckVideos #import check_videos as lib
from updatevideo import UpdateVideos  # Import the UpdateVideos class from update_videos.py
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from CreateVideoList import CreateVideoList

#main class
class VideoPlayer:
    def __init__(self):
        #main window
        self.window = tk.Tk()
        self.window.geometry("570x150")
        self.window.title("Video Player")

        fonts.configure()
        #create the text
        header_lbl = ttk.Label(self.window, text="Select an option by clicking one of the buttons below")
        header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        #Check video button and add function
        check_videos_btn = ttk.Button(self.window, text="Check Videos", command=self.check_videos_clicked)
        check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

        #Create video list button and add function
        create_video_list_btn = ttk.Button(self.window, text="Create Video List", command=self.create_video_list_clicked)
        create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

        #update video button and add function
        self.update_videos_btn = ttk.Button(self.window, text="Update Videos", command=self.update_videos_clicked)
        self.update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

        self.status_lbl = ttk.Label(self.window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.window.mainloop()

    #check video function
    def check_videos_clicked(self):
        self.status_lbl.configure(text="Check Videos button was clicked!")
        CheckVideos(tk.Toplevel(self.window))
    #update video function
    def update_videos_clicked(self):
        self.status_lbl.configure(text="Update Videos button was clicked!")
        UpdateVideos(self.window)
    #create video function
    def create_video_list_clicked(self):
        self.status_lbl.configure(text="Create Video List button was clicked!")
        CreateVideoList(tk.Toplevel(self.window))
        #CheckboxesApp(tk.Toplevel(self.window))
if __name__ == "__main__":
    VideoPlayer()
