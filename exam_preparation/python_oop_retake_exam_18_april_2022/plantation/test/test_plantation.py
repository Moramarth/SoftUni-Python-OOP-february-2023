from plantation.plantation import Plantation
from unittest import TestCase, main


class PlantationTests(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(5)

    def test_constructor(self):
        self.assertEqual(5, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_setter_error(self):
        with self.assertRaises(ValueError) as context:
            self.plantation.size = -2
        self.assertEqual("Size must be positive number!", str(context.exception))

    def test_size_with_zero(self):
        self.plantation.size = 0
        self.assertEqual(0, self.plantation.size)

    def test_hire_worker_successfully(self):
        result = self.plantation.hire_worker("Pesho")
        expected_output = "Pesho successfully hired."
        self.assertEqual(expected_output, result)

    def test_hire_worker_already_in_list(self):
        self.plantation.hire_worker("Pesho")
        with self.assertRaises(ValueError) as context:
            self.plantation.hire_worker("Pesho")
        self.assertEqual("Worker already hired!", str(context.exception))

    def test_len_no_plants(self):
        self.assertEqual(0, len(self.plantation))

    def test_planting_not_a_valid_worker(self):
        with self.assertRaises(ValueError) as context:
            self.plantation.planting("Worker", "Plant")
        self.assertEqual("Worker with name Worker is not hired!", str(context.exception))

    def test_planting(self):
        self.plantation.hire_worker("Pesho")
        self.plantation.hire_worker("Worker")
        self.assertEqual(["Pesho", "Worker"], self.plantation.workers)
        result = self.plantation.planting("Worker", "Plant1")
        expected_output = "Worker planted it's first Plant1."
        self.assertEqual(expected_output, result)
        self.assertEqual(1, len(self.plantation))
        self.plantation.planting("Pesho", "Plant1")
        self.assertEqual(2, len(self.plantation))
        self.assertEqual({"Worker": ["Plant1"], "Pesho": ["Plant1"]}, self.plantation.plants)
        result2 = self.plantation.planting("Worker", "Plant2")
        expected_output2 = "Worker planted Plant2."
        self.assertEqual(expected_output2, result2)
        self.assertEqual({"Worker": ["Plant1", "Plant2"], "Pesho": ["Plant1"]}, self.plantation.plants)
        self.assertEqual(3, len(self.plantation))
        self.plantation.planting("Worker", "Plant3")
        self.plantation.planting("Worker", "Plant4")
        with self.assertRaises(ValueError) as context:
            self.plantation.planting("Worker", "Plant5")
        self.assertEqual("The plantation is full!", str(context.exception))
        self.assertEqual(5, len(self.plantation))

    def test_str(self):
        self.plantation.hire_worker("Pesho")
        self.plantation.hire_worker("Worker")
        self.plantation.planting("Pesho", "Plant1")
        self.plantation.planting("Worker", "Plant1")
        self.plantation.planting("Worker", "Plant2")
        self.plantation.planting("Worker", "Plant3")
        self.plantation.planting("Worker", "Plant4")
        result = str(self.plantation)
        expected_output = "Plantation size: 5\n" \
                          "Pesho, Worker\n" \
                          "Pesho planted: Plant1\n" \
                          "Worker planted: Plant1, Plant2, Plant3, Plant4"
        self.assertEqual(expected_output, result)

    def test_repr(self):
        self.plantation.hire_worker("Pesho")
        self.plantation.hire_worker("Worker")
        self.plantation.planting("Pesho", "Plant1")
        self.plantation.planting("Worker", "Plant1")
        self.plantation.planting("Worker", "Plant2")
        self.plantation.planting("Worker", "Plant3")
        self.plantation.planting("Worker", "Plant4")
        result = self.plantation.__repr__()
        expected_output = "Size: 5\nWorkers: Pesho, Worker"
        self.assertEqual(expected_output, result)


if __name__ == '__main__':
    main()
