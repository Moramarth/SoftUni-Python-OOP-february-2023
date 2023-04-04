from unittest import TestCase, main
from exam_preparation.python_oop_retake_exam_23_august_2021.library.library import Library


class LibraryTests(TestCase):
    def setUp(self) -> None:
        self.library = Library("Library")

    def test_constructor(self):
        self.assertEqual("Library", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_setter_error(self):
        with self.assertRaises(ValueError) as context:
            self.library.name = ""
        self.assertEqual("Name cannot be empty string!", str(context.exception))

    def test_add_book(self):
        self.library.add_book("Author1", "Title1")
        self.assertEqual({"Author1": ["Title1"]}, self.library.books_by_authors)
        self.library.add_book("Author1", "Title2")
        self.assertEqual({"Author1": ["Title1", "Title2"]}, self.library.books_by_authors)
        self.library.add_book("Author2", "Title1")
        self.assertEqual({"Author1": ["Title1", "Title2"], "Author2": ["Title1"]}, self.library.books_by_authors)

    def test_add_reader(self):
        self.library.add_reader("Reader")
        self.assertEqual({"Reader": []}, self.library.readers)
        self.library.add_reader("Reader2")
        self.assertEqual({"Reader": [], "Reader2": []}, self.library.readers)
        result = self.library.add_reader("Reader")
        expected_output = f"Reader is already registered in the Library library."
        self.assertEqual(expected_output, result)

    def test_rent_book(self):
        self.library.books_by_authors = {"Author1": ["Title1", "Title2"], "Author2": ["Title1"]}
        result = self.library.rent_book("Reader", "Author1", "Title1")
        expected_output = "Reader is not registered in the Library Library."
        self.assertEqual(expected_output, result)

        self.library.add_reader("Reader")
        result2 = self.library.rent_book("Reader", "Author3", "Title1")
        expected_output2 = "Library Library does not have any Author3's books."
        self.assertEqual(expected_output2, result2)

        result3 = self.library.rent_book("Reader", "Author1", "Title4")
        expected_output3 = """Library Library does not have Author1's "Title4"."""
        self.assertEqual(expected_output3, result3)

        self.library.rent_book("Reader", "Author1", "Title1")
        self.assertEqual({"Reader": [{"Author1": "Title1"}]}, self.library.readers)
        self.assertEqual({"Author1": ["Title2"], "Author2": ["Title1"]}, self.library.books_by_authors)

        self.library.rent_book("Reader", "Author2", "Title1")
        self.assertEqual({"Reader": [{"Author1": "Title1"}, {"Author2": "Title1"}]}, self.library.readers)
        self.assertEqual({"Author1": ["Title2"], "Author2": []}, self.library.books_by_authors)

        self.library.rent_book("Reader", "Author1", "Title2")
        self.assertEqual({"Reader": [{"Author1": "Title1"}, {"Author2": "Title1"}, {"Author1": "Title2"}]}, self.library.readers)
        self.assertEqual({"Author1": [], "Author2": []}, self.library.books_by_authors)


if __name__ == '__main__':
    main()
