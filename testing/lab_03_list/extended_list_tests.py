from testing.lab_03_list.extended_list import IntegerList
import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test_list = IntegerList(1, 2, 3, 4, 5, 6, "This is not an integer", 2.77)

    def test_constructor_for_valid_data(self):
        expected_output = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.test_list.get_data(), expected_output)

    def test_adding_integer_to_the_list(self):
        expected_output = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(self.test_list.add(7), expected_output)

    def test_add_method_with_invalid_data_error(self):
        with self.assertRaises(ValueError) as context:
            self.test_list.add("7")
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_remove_element_with_valid_index(self):
        expected_output = 1
        self.assertEqual(self.test_list.remove_index(0), expected_output)

    def test_remove_element_with_invalid_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.test_list.remove_index(6)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_get_element_with_valid_index(self):
        expected_output = 1
        self.assertEqual(self.test_list.get(0), expected_output)

    def test_get_element_with_invalid_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.test_list.get(6)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_element_with_valid_index_and_data(self):
        expected_output = [1, 2, 3, 4, 5, 7, 6]
        self.test_list.insert(-1, 7)
        self.assertEqual(self.test_list.get_data(), expected_output)

    def test_insert_element_with_invalid_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.test_list.insert(6, 7)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_element_with_invalid_data_error(self):
        with self.assertRaises(ValueError) as context:
            self.test_list.insert(0, "7")
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_get_the_biggest_integer_in_list(self):
        self.assertEqual(self.test_list.get_biggest(), 6)

    def test_get_index_of_a_chosen_element(self):
        self.assertEqual(self.test_list.get_index(6), 5)


if __name__ == '__main__':
    unittest.main()
