"""
Refactor the provided code, so there is a separate class called Library, which contains books and has a method called
find_book(title) that returns the book with the given title. Remove the unnecessary code from the Book class
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = list()

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        try:
            book = next(filter(lambda b: b.title == title, self.books))
            return book
        except StopIteration:
            return "Book is not in this library"
