"""
Create a class called PhotoAlbum. Upon initialization, it should receive pages (int). It should also have one more
contain only 4 photos. The class should also have 3 more methods:

•	from_photos_count(photos_count: int) - creates a new instance of PhotoAlbum. Note: Each page can contain 4 photos.

•	add_photo(label:str) - adds the photo in the first possible page and slot and return "{label} photo added
successfully on page {page_number(starting from 1)} slot {slot_number(starting from 1)}".
If there are no free slots left, return "No more free slots"

•	display() - returns a string representation of each page and the photos in it.
Each photo is marked with "[]", and the page separation is made using 11 dashes (-). For example, if we have 1 page
and 2 photos:
-----------
[] []
-----------
and if we have 2 empty pages:
-----------

-----------

-----------
"""
from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label: str):
        try:
            row = [row for row in self.photos if len(row) < 4][0]
            column = len(row) + 1
            row.append(label)
            return f"{label} photo added successfully on page {self.photos.index(row) + 1} slot {column}"
        except IndexError:
            return "No more free slots"

    def display(self):
        display = list()
        for i in range(len(self.photos)):
            display.append("-" * 11)
            display.append("[] " * (len(self.photos[i]) - 1) + "[]" if len(self.photos[i]) else "")
        display.append("-" * 11)

        return "\n".join(display)
