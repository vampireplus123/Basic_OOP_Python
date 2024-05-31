# Define a class called LibraryItem
class LibraryItem:
    # Constructor method to initialize object attributes
    def __init__(self, name, director, rating=0, images=0):
        self.name = name            # Name of the library item
        self.director = director    # Director of the library item
        self.rating = rating        # Rating of the library item
        self.play_count = 0         # Play count of the library item (initially 0)
        self.images = images        # Number of images associated with the library item

    # Method to return information about the library item
    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"  # Format: Name - Director [Rating stars]

    # Method to generate a star rating string based on the 'rating' attribute
    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"  # Add a star for each unit of rating
        return stars

# Create an empty dictionary to store library items
library = {}