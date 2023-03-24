"""
We want to print books, but before printing the book, we should format it.
To accomplish this, we have a class Printer that can print books and a class Formatter which is used by the Printer.
Refactor the provided code that breaks the DIP because both Printer and Formatter depend on concretions,
not abstractions, by creating abstractions and injecting them wherever needed.
"""
from abc import abstractmethod, ABC


class Book:
    def __init__(self, content: str):
        self.content = content


class IFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class IPrinter(ABC):
    @abstractmethod
    def get_book(self, book: Book):
        pass


class Printer:
    def __init__(self, formatter: IFormatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        formatted_book = self.formatter.format(book)
        return formatted_book
