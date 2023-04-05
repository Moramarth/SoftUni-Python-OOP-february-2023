from unittest import TestCase, main
from exam_preparation.python_oop_exam_10_april_2021.train.train.train import Train


class TrainTests(TestCase):
    def setUp(self) -> None:
        self.train = Train("Train", 5)

    def test_constructor(self):
        self.assertEqual("Train", self.train.name)
        self.assertEqual(5, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passengers(self):
        result = self.train.add("Gosho")
        expected_output = "Added passenger Gosho"
        self.assertEqual(expected_output, result)
        self.assertEqual(["Gosho"], self.train.passengers)

        result2 = self.train.add("Pesho")
        expected_output2 = "Added passenger Pesho"
        self.assertEqual(expected_output2, result2)
        self.assertEqual(["Gosho", "Pesho"], self.train.passengers)

    def test_add_passengers_errors(self):
        self.train.add("Gosho")
        self.train.add("Pesho")
        with self.assertRaises(ValueError) as context:
            self.train.add("Gosho")
        self.assertEqual("Passenger Gosho Exists", str(context.exception))

        self.train.add("Ivan")
        self.train.add("Dyan")
        self.train.add("Maria")
        with self.assertRaises(ValueError) as context:
            self.train.add("Not enough space")
        self.assertEqual("Train is full", str(context.exception))
        self.assertEqual(["Gosho", "Pesho", "Ivan", "Dyan", "Maria"], self.train.passengers)

    def test_train_zero_capacity(self):
        self.train.capacity = Train.ZERO_CAPACITY
        self.assertEqual(0, self.train.capacity)

        test_train = Train("Test Train", Train.ZERO_CAPACITY)
        self.assertEqual(0, test_train.capacity)

    def test_remove_passengers(self):
        self.train.passengers = ["Gosho", "Pesho", "Ivan", "Dyan", "Maria"]
        result = self.train.remove("Gosho")
        expected_output = "Removed Gosho"
        self.assertEqual(expected_output, result)
        self.assertEqual(["Pesho", "Ivan", "Dyan", "Maria"], self.train.passengers)

        with self.assertRaises(ValueError) as context:
            self.train.remove("Gosho")
        self.assertEqual("Passenger Not Found", str(context.exception))

        self.train.remove("Dyan")
        self.assertEqual(["Pesho", "Ivan", "Maria"], self.train.passengers)

    def test_constants_in_class(self):
        self.assertEqual("Train is full", Train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", Train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", Train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", Train.PASSENGER_ADD)
        self.assertEqual("Removed {}", Train.PASSENGER_REMOVED)
        self.assertEqual(0, Train.ZERO_CAPACITY)


if __name__ == '__main__':
    main()
