

import unittest

from testing.exercise_02_vehicle.project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test_vehicle = Vehicle(10.0, 144.0)

    def test_constructor_is_working_properly(self):
        self.assertEqual(self.test_vehicle.fuel, 10)
        self.assertEqual(self.test_vehicle.capacity, 10)
        self.assertEqual(self.test_vehicle.horse_power, 144)
        self.assertEqual(self.test_vehicle.fuel_consumption, 1.25)

    def test_drive_when_fuel_is_enough(self):
        self.test_vehicle.drive(4)
        self.assertEqual(self.test_vehicle.fuel, 5)

    def test_drive_when_fuel_not_enough(self):
        with self.assertRaises(Exception) as context:
            self.test_vehicle.drive(55)
        self.assertEqual(str(context.exception), "Not enough fuel")

    def test_refuel_with_valid_data(self):
        self.test_vehicle.drive(4)
        self.test_vehicle.refuel(3)
        self.assertEqual(self.test_vehicle.fuel, 8)

    def test_refuel_with_too_much_fuel(self):
        self.test_vehicle.drive(4)
        with self.assertRaises(Exception) as context:
            self.test_vehicle.refuel(200)
        self.assertEqual(str(context.exception), "Too much fuel")

    def test_instance_to_string(self):
        self.test_vehicle.drive(4)
        result = str(self.test_vehicle)
        expected_output = f"The vehicle has 144.0 " \
                          f"horse power with 5.0 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
