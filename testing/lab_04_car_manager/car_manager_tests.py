from testing.lab_04_car_manager.car_manager import Car
import unittest


class CarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("Opel", "Meriva", 5, 52)

    def test_constructor_with_valid_data(self):
        self.assertEqual(self.car.make, "Opel")
        self.assertEqual(self.car.model, "Meriva")
        self.assertEqual(self.car.fuel_consumption, 5)
        self.assertEqual(self.car.fuel_capacity, 52)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_car_make_with_invalid_data_error(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ""
        self.assertEqual(str(context.exception), "Make cannot be null or empty!")

    def test_car_model_with_invalid_data_error(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ""
        self.assertEqual(str(context.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_with_invalid_data_error(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_with_invalid_data_error(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -10
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_with_negative_value_error(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -5
        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test_refuel_with_valid_data(self):
        self.car.refuel(20)
        self.assertEqual(self.car.fuel_amount, 20)

    def test_refuel_with_value_higher_than_capacity(self):
        self.car.refuel(2000)
        self.assertEqual(self.car.fuel_amount, 52)

    def test_refuel_with_zero_as_value(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(0)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_with_negative_value(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(-16)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_drive_with_enough_fuel(self):
        self.car.refuel(20)
        self.car.drive(200)
        self.assertEqual(self.car.fuel_amount, 10)

    def test_drive_with_not_enough_fuel(self):
        self.car.refuel(5)
        with self.assertRaises(Exception) as context:
            self.car.drive(200)
        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")


if __name__ == '__main__':
    unittest.main()
