from library_item import LibraryItem
from PIL import Image

#create a library
library = {}
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 2, r"File image\Tom and Jerry.jpg")
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 2, r"File image\Breakfast.jpg")
library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2, r"File image\Casablanca.jpg")
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1, r"File image\The Sound of Music.jpg")
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3, r"File image\Gone with the Wind.jpg")
library["06"] = LibraryItem("Bille Jean", "Micheal Jackson", 4, r"File image\Billie Jean.jpg")

# Rest of the code (e.g., list_all, get_name, get_director, etc.) should remain unchanged.


#list_all item in the lib
def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output

#get the name of the library
def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None

#get the directory of the library
def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None

#get the rating of the library
def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1
#get the image of the library
def get_image(key):
    try:
        item = library[key]
        image_path = item.images
        return image_path  # Return the path to the image file
    except KeyError:
        return None

#set the rating of library
def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return
    
def set_ditector(key, director):
    try:
        item = library[key]
        item.director = director
        return item.director 
    except KeyError:
        return

def set_name(key, name):
    try:
        item = library[key]
        item.name = name
        return item.name
    except KeyError:
        return
    
#get the play_count of library
def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

#increment of library
def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
        str(item.play_count)
    except KeyError:
        return
def set_play_count(key, playcount):
    try:
        item = library[key]
        item.play_count = playcount
        return item.name
    except KeyError:
        return