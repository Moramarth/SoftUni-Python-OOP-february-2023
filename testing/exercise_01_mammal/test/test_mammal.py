import unittest

from testing.exercise_01_mammal.project.mammal import Mammal


class MammalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test_mammal = Mammal("Subject", "Monkey", "Ooh Ooh ah ah")

    def test_constructor_working_properly(self):
        self.assertEqual(self.test_mammal.name, "Subject")
        self.assertEqual(self.test_mammal.type, "Monkey")
        self.assertEqual(self.test_mammal.sound, "Ooh Ooh ah ah")

    def test_making_sound_method(self):
        result = self.test_mammal.make_sound()
        expected_output = "Subject makes Ooh Ooh ah ah"
        self.assertEqual(result, expected_output)

    def test_getting_kingdom_information(self):
        self.assertEqual(self.test_mammal.get_kingdom(), "animals")

    def test_getting_info_for_the_instance_of_mammal(self):
        result = self.test_mammal.info()
        expected_output = "Subject is of type Monkey"
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
