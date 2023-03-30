from unittest import TestCase, main
from exam_preparation.python_oop_exam_10_december_2022.toy_store.toy_store import ToyStore


class ToyStoreTests(TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()

    def test_constructor(self):
        self.assertEqual(7, len(self.store.toy_shelf))
        self.assertIn("A", self.store.toy_shelf)
        self.assertIn("B", self.store.toy_shelf)
        self.assertIn("C", self.store.toy_shelf)
        self.assertIn("D", self.store.toy_shelf)
        self.assertIn("E", self.store.toy_shelf)
        self.assertIn("F", self.store.toy_shelf)
        self.assertIn("G", self.store.toy_shelf)

    def test_add_toy_with_no_errors(self):
        result = self.store.add_toy("A", "Toy")
        expected_output = f"Toy:Toy placed successfully!"
        self.assertEqual(expected_output, result)
        self.assertEqual("Toy", self.store.toy_shelf["A"])

    def test_add_toy_shelf_is_not_valid(self):
        with self.assertRaises(Exception) as context:
            self.store.add_toy("W", "Toy")
        self.assertEqual("Shelf doesn't exist!", str(context.exception))

    def test_add_toy_with_toy_already_on_the_shelf(self):
        self.store.add_toy("A", "Toy")
        with self.assertRaises(Exception) as context:
            self.store.add_toy("A", "Toy")
        self.assertEqual("Toy is already in shelf!", str(context.exception))

    def test_add_toy_shelf_already_taken(self):
        self.store.add_toy("A", "Toy")
        with self.assertRaises(Exception) as context:
            self.store.add_toy("A", "Car")
        self.assertEqual("Shelf is already taken!", str(context.exception))

    def test_remove_toy_no_errors(self):
        self.store.add_toy("A", "Toy")
        result = self.store.remove_toy("A", "Toy")
        expected_output = "Remove toy:Toy successfully!"
        self.assertEqual(expected_output, result)
        self.assertEqual(None, self.store.toy_shelf["A"])

    def test_remove_toy_with_different_name(self):
        self.store.add_toy("A", "Toy")
        with self.assertRaises(Exception) as context:
            self.store.remove_toy("A", "Car")
        self.assertEqual("Toy in that shelf doesn't exists!", str(context.exception))
        self.assertEqual("Toy", self.store.toy_shelf["A"])

    def test_remove_toy_from_non_existing_shelf(self):
        with self.assertRaises(Exception) as context:
            self.store.remove_toy("W", "Car")
        self.assertEqual("Shelf doesn't exist!", str(context.exception))


if __name__ == '__main__':
    main()
