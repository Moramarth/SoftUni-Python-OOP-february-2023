from classes_and_objects.exercise_08_library.user import User


class Library:
    def __init__(self):
        self.user_records = list()  # stores instances of the User class
        self.books_available = dict()  # keys = author names values = list(available books names)
        self.rented_books = dict()  # keys = usernames values = dict( book name: days to return)

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if author in self.books_available and book_name in self.books_available[author]:
            if user.username not in self.rented_books:
                self.rented_books[user.username] = dict()
            self.rented_books[user.username][book_name] = days_to_return
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        else:
            for key, value in self.rented_books.items():
                if tuple(value)[0] == book_name:
                    days_to_return = self.rented_books[key][tuple(value)[0]]
                    break
            return f'The book "{book_name}" is already rented' \
                   f' and will be available in {days_to_return} days!'

    def return_book(self, author: str, book_name: str, user: User) -> str:
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
        else:
            return f"{user.username} doesn't have this book in his/her records!"
