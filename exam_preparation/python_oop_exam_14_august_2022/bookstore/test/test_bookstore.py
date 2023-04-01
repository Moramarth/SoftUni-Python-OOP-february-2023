from unittest import TestCase, main
from exam_preparation.python_oop_exam_14_august_2022.bookstore.bookstore import Bookstore


class BookstoreTests(TestCase):
    def setUp(self) -> None:
        self.store = Bookstore(5)
        self.test_dict = {"Book1": 2, "Book2": 2, "Book3": 1}

    def test_constructor_working_properly(self):
        self.assertEqual(5, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_books_limit_setter_with_negative_number(self):
        with self.assertRaises(ValueError) as context:
            self.store.books_limit = -4
        self.assertEqual("Books limit of -4 is not valid", str(context.exception))

    def test_books_limit_setter_with_zero(self):
        with self.assertRaises(ValueError) as context:
            self.store.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(context.exception))

    def test_len_method(self):
        self.store.availability_in_store_by_book_titles = self.test_dict
        self.assertEqual(5, len(self.store))

    def test_receive_book_no_space(self):
        with self.assertRaises(Exception) as context:
            self.store.receive_book("Book1", 15)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(context.exception))

        self.store.availability_in_store_by_book_titles = self.test_dict

        with self.assertRaises(Exception) as context:
            self.store.receive_book("Book1", 1)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(context.exception))

    def test_receive_book_when_space_is_available(self):
        self.store.books_limit += 4
        self.store.availability_in_store_by_book_titles = self.test_dict
        result = self.store.receive_book("Book1", 2)
        expected_output = "4 copies of Book1 are available in the bookstore."
        self.assertEqual(expected_output, result)
        self.assertEqual({"Book1": 4, "Book2": 2, "Book3": 1}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(7, len(self.store))
        result = self.store.receive_book("Book1", 1)
        expected_output = "5 copies of Book1 are available in the bookstore."
        self.assertEqual(expected_output, result)
        self.assertEqual({"Book1": 5, "Book2": 2, "Book3": 1}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(8, len(self.store))
        result = self.store.receive_book("Book4", 1)
        expected_output = "1 copies of Book4 are available in the bookstore."
        self.assertEqual(expected_output, result)
        self.assertEqual({"Book1": 5, "Book2": 2, "Book3": 1, "Book4": 1},
                         self.store.availability_in_store_by_book_titles)
        self.assertEqual(9, len(self.store))

    def test_receive_book_when_no_books_in_store(self):
        result = self.store.receive_book("Book1", 2)
        expected_output = "2 copies of Book1 are available in the bookstore."
        self.assertEqual(expected_output, result)
        self.assertEqual({"Book1": 2}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(2, len(self.store))

    def test_sell_book_when_book_is_not_available(self):
        self.store.availability_in_store_by_book_titles = self.test_dict
        with self.assertRaises(Exception) as context:
            self.store.sell_book("Book4", 1)
        self.assertEqual("Book Book4 doesn't exist!", str(context.exception))

    def test_sell_book_not_enough_copies(self):
        self.store.availability_in_store_by_book_titles = self.test_dict
        with self.assertRaises(Exception) as context:
            self.store.sell_book("Book1", 10)
        self.assertEqual("Book1 has not enough copies to sell. Left: 2", str(context.exception))

    def test_sell_book_with_valid_data(self):
        self.store.availability_in_store_by_book_titles = self.test_dict
        result = self.store.sell_book("Book1", 1)
        expected_output = "Sold 1 copies of Book1"
        self.assertEqual(expected_output, result)
        self.assertEqual({"Book1": 1, "Book2": 2, "Book3": 1}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(4, len(self.store))
        self.assertEqual(1, self.store.total_sold_books)
        result2 = self.store.sell_book("Book1", 1)
        expected_output2 = "Sold 1 copies of Book1"
        self.assertEqual(expected_output2, result2)
        self.assertEqual({"Book1": 0, "Book2": 2, "Book3": 1}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(3, len(self.store))
        self.assertEqual(2, self.store.total_sold_books)
        self.store.sell_book("Book2", 2)
        self.store.sell_book("Book3", 1)
        self.assertEqual(0, len(self.store))
        self.assertEqual(5, self.store.total_sold_books)

    def test_str_method(self):
        self.store.availability_in_store_by_book_titles = self.test_dict
        result = str(self.store)
        expected_output = "\n".join([
            "Total sold books: 0",
            'Current availability: 5',
            " - Book1: 2 copies",
            " - Book2: 2 copies",
            " - Book3: 1 copies",
        ])
        self.assertEqual(expected_output, result)


if __name__ == '__main__':
    main()
