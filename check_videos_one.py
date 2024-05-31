import tkinter as tk  # Importing the tkinter library for creating GUI
import tkinter.scrolledtext as tkst  # Importing scrolledtext for a scrollable text area
import font_manager as fonts  # Importing font_manager for font configurations (not a standard library, might be custom)
import video_library as lib  # Importing a custom video_library module
from PIL import ImageTk, Image  # Importing necessary modules from PIL library for image handling
from tkinter import messagebox  # Importing messagebox from tkinter for displaying messages
import ttkbootstrap as ttk #import  ttkbootstrap
from ttkbootstrap.constants import *
# Function to set text content in a text area
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Deleting the existing text in the text area
    text_area.insert(1.0, content)  # Inserting new content into the text area

# Class to check and display video details
class CheckVideos():
    def __init__(self, window):
        window.geometry("950x500")  # Setting the initial size of the window
        window.title("Check Videos")  # Setting the title of the window

        # Creating buttons, labels, text entry, and text areas within the window
        list_videos_btn = ttk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        # Grid placement of the 'List All Videos' button
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = ttk.Label(window, text="Enter Video Number (01-05)")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  # Grid placement of the label

        self.input_txt = ttk.Entry(window, width=3)  # Entry widget for input
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)  # Grid placement of the entry widget

        check_video_btn = ttk.Button(window, text="Check Video", command=self.check_video_clicking)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)  # Grid placement of the 'Check Video' button

        # ScrolledText widget for displaying a list of videos
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=2, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Text widget for displaying video details
        self.video_txt = tkst.ScrolledText(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Label for displaying images from the video library
        self.photo_lib = ttk.Canvas(window)
        self.photo_lib.grid(row=2, column=3, rowspan=2, sticky="W", padx=10, pady=10)

        # Label for displaying status or messages
        self.status_lbl = ttk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=3, columnspan=4, sticky="W", padx=10, pady=10)

        # Entry widget for searching videos
        self.search_entry = ttk.Entry(window, width=30)
        self.search_entry.grid(row=1, column=0, padx=5, pady=0, columnspan=1)

        search_video_btn = ttk.Button(window, text="Search", command=self.search_video_clicking)
        search_video_btn.grid(row=1, column=1, padx=0, pady=0)

        fonts.configure()  # Configuring fonts (custom function)
        self.list_videos_clicked()  # Calling a method to list all videos upon initialization

    # Function to display details of a specific video
    def check_video_clicking(self):
        key = self.input_txt.get().zfill(2)  # Getting the input value
        name = lib.get_name(key)  # Fetching the name of the video using the input key
        if name is not None:
            # Displaying video details and images
            self.loadContent(key, name)
            self.loadImageForCheking(key)
        else:
            set_text(self.video_txt, f"Video {key} not found")  # If video not found, display a message
            messagebox.showwarning("Video not found",f"Not Found {key}")
            self.photo_lib.configure(image=" ")
        self.status_lbl.configure(text="Check Video button was clicked!")  # Updating status label

    # Function to list all videos in the library
    def list_videos_clicked(self):
        video_list = lib.list_all()  # Fetching a list of all videos from the library
        set_text(self.list_txt, video_list)  # Setting the fetched list in the text area
        self.status_lbl.configure(text="List Videos button was clicked!")  # Updating status label

    # Function to handle search functionality
    def search_video_clicking(self):
        key = self.input_txt.get()  # Getting the input value
        query = self.search_entry.get()  # Getting the search query
        
        self.search_videos(query, key)  # Calling a method to search for videos
        self.checkingSearchIsNumber(query)  # Checking if the search query is a number

    # Function to search videos based on a query
    def search_videos(self, query, key):
        matching_videos = [] #for saving the matching videos

        #using loop for finding video
        for key in lib.library:
            item = lib.library[key] #get the key
            if query.lower() in item.name.lower() or query.lower() in item.director.lower(): #loweer the input search value
                matching_videos.append(f"{key} {item.info()}")  #put the video in the list and get the info
                self.loadImageForCheking(key) #call the load image
                self.loadContent(key, lib.get_name(key)) #call the load content
                
        if matching_videos:
            set_text(self.list_txt, '\n'.join(matching_videos)) #show the vide content
            self.status_lbl.configure(text=f"Search results for '{query}'")
        else:
            set_text(self.list_txt, "No matching videos found.") #show up when the video not
            self.status_lbl.configure(text=f"No results for '{query}'")
    
    # Function to check if the search query is a number
    def checkingSearchIsNumber(self, query):
        switch = False
        try:
            int(query)
            switch = True  # If it's a number, set the switch to True
            if switch == True:
                self.search_videos_by_rating(query)  # If it's a number, search videos by play count
        except ValueError:
            switch = False  # If it's not a number, set the switch to False

    # Function to search videos by play count
    def search_videos_by_rating(self, query):
        matching_videos = [] #for saving the matching videos
        i = int(query) #checking if query is number

        for key in lib.library:
            item = lib.library[key] #get the item 
            if i == lib.get_rating(key): #checking rating of item == query
                matching_videos.append((key, item.info())) #append the item into the list

        if matching_videos:
            # Set up all the video details to display 
            video_details = ""
            for idx, (video_key, video_info) in enumerate(matching_videos, start=1): #get the infor
                video_name = lib.get_name(video_key) #get name
                video_director = lib.get_director(video_key) #get director
                video_rating = lib.get_rating(video_key)# get rating
                video_plays = lib.get_play_count(video_key)# get play count
                
                #format the video details
                video_details += f"{idx} {video_name}\nDirector: {video_director}\nRating: {video_rating}\nPlays: {video_plays}\n\n"
                
                #set the text
                set_text(self.video_txt, video_details)

                # Set the list of matching videos in list_txt
                matching_videos_list = [f"{idx:02d} {lib.get_name(key)} - {lib.get_director(key)} **" for idx, (key, _) in enumerate(matching_videos, start=1)]
                set_text(self.list_txt, '\n'.join(matching_videos_list))
                self.status_lbl.configure(text=f"Search results for '{query}'")
                
                # Clear the image when searching by rating
                self.photo_lib.delete("all")
        else:
                set_text(self.video_txt, "No matching videos found.")
                set_text(self.list_txt, "No matching videos found.")
        
    def loadImageForCheking(self,key):
        self.video_photo = lib.get_image(key)  # Get image details
        self.new_photo = Image.open(self.video_photo)  # Open the image
        self.new_photo = self.new_photo.resize((220, 120), resample=Image.NEAREST)  # Resize the image
        self.appear_the_photo = ImageTk.PhotoImage(self.new_photo)  # Convert to ImageTk format
        
        # Clear previous images on the canvas
        self.photo_lib.delete("all")
        
        # Display the image on the canvas
        self.photo_lib.create_image(0, 0, anchor="nw", image=self.appear_the_photo)

#Load content 
    def loadContent(self,key,name):
        director = lib.get_director(key)#get the director details from the director library
        rating = lib.get_rating(key)#get the rating
        play_count = lib.get_play_count(key)#get the play count
        video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"# format the detail
        set_text(self.video_txt, video_details) #appear the details



if __name__ == "__main__":
    window = tk.Tk()
    CheckVideos(window)
    window.mainloop()
