import pytest

from library_item import LibraryItem

@pytest.mark.parametrize("name, director, rating, images, expected_info", [
    ("The Shawshank Redemption", "Frank Darabont", 5, 10, "The Shawshank Redemption - Frank Darabont *****"),
    ("The Godfather", "Francis Ford Coppola", 5, 15, "The Godfather - Francis Ford Coppola *****"),
    ("The Dark Knight", "Christopher Nolan", 5, 12, "The Dark Knight - Christopher Nolan *****"),
])
def test_library_item_info(name, director, rating, images, expected_info):
    item = LibraryItem(name, director, rating, images)
    assert item.info() == expected_info

@pytest.mark.parametrize("name", ["The Shawshank Redemption", "The Godfather", "The Dark Knight"])
def test_library_item_name_access(name):
    item = LibraryItem(name, "Frank Darabont", 5, 10)
    assert item.name == name

@pytest.mark.parametrize("director", ["Frank Darabont", "Francis Ford Coppola", "Christopher Nolan"])
def test_library_item_director_access(director):
    item = LibraryItem("The Shawshank Redemption", director, 5, 10)
    assert item.director == director

@pytest.mark.parametrize("rating", [3, 4, 5])
def test_library_item_rating_access(rating):
    item = LibraryItem("The Shawshank Redemption", "Frank Darabont", rating, 10)
    assert item.rating == rating

@pytest.mark.parametrize("images", [10, 15, 12])
def test_library_item_images_access(images):
    item = LibraryItem("The Shawshank Redemption", "Frank Darabont", 5, images)
    assert item.images == images

def test_library_item_stars():
    item = LibraryItem("The Shawshank Redemption", "Frank Darabont", 5, 10)
    assert item.stars() == "*****"