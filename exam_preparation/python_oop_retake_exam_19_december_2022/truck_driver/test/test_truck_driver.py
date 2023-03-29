from unittest import TestCase, main
from exam_preparation.python_oop_retake_exam_19_december_2022.truck_driver.truck_driver import TruckDriver


class TruckDriverTests(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Pesho", 5)

    def test_constructor_working_properly(self):
        self.assertEqual("Pesho", self.driver.name)
        self.assertEqual(5, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_setter(self):
        with self.assertRaises(ValueError) as context:
            self.driver.earned_money = -50
        self.assertEqual("Pesho went bankrupt.", str(context.exception))

    def test_adding_new_cargo_offer(self):
        result = self.driver.add_cargo_offer("Sofia", 100)
        expected_output = "Cargo for 100 to Sofia was added as an offer."
        self.assertEqual(expected_output, result)
        self.assertEqual({"Sofia": 100}, self.driver.available_cargos)

    def test_adding_existing_cargo_location_offer(self):
        self.driver.add_cargo_offer("Sofia", 100)
        with self.assertRaises(Exception) as context:
            self.driver.add_cargo_offer("Sofia", 100)
        self.assertEqual("Cargo offer is already added.", str(context.exception))

    def test_drive_best_cargo_offer_no_offers(self):
        result = self.driver.drive_best_cargo_offer()
        expected_output = "There are no offers available."
        self.assertEqual(expected_output, result)

    def test_drive_best_cargo_offer_valid_offers(self):
        self.driver.add_cargo_offer("Sofia", 100)
        self.driver.add_cargo_offer("Pleven", 101)
        result = self.driver.drive_best_cargo_offer()
        expected_output = "Pesho is driving 101 to Pleven."
        self.assertEqual(expected_output, result)
        self.assertEqual(505, self.driver.earned_money)
        self.assertEqual(101, self.driver.miles)

    def test_drive_best_offer_and_go_bankrupt(self):
        self.driver.money_per_mile = 0.5
        self.driver.add_cargo_offer("Sofia", 20000)
        with self.assertRaises(ValueError) as context:
            self.driver.drive_best_cargo_offer()
        self.assertEqual("Pesho went bankrupt.", str(context.exception))

    def test_check_for_activity_and_do_nothing(self):
        self.driver.earned_money = 100
        self.driver.check_for_activities(100)
        self.assertEqual(100, self.driver.earned_money)

    def test_check_for_activity_and_go_bankrupt(self):
        with self.assertRaises(ValueError) as context:
            self.driver.check_for_activities(500)
        self.assertEqual("Pesho went bankrupt.", str(context.exception))

    def test_check_for_activity_and_eat(self):
        self.driver.earned_money = 100
        self.driver.check_for_activities(250)
        self.assertEqual(80, self.driver.earned_money)

    def test_check_for_activity_and_sleep(self):
        self.driver.earned_money = 125
        self.driver.check_for_activities(1000)
        self.assertEqual(0, self.driver.earned_money)

    def test_check_for_activity_and_pump_gas(self):
        self.driver.earned_money = 665
        self.driver.check_for_activities(1500)
        self.assertEqual(0, self.driver.earned_money)

    def test_check_for_activity_and_repair_truck(self):
        self.driver.earned_money = 11750
        self.driver.check_for_activities(10000)
        self.assertEqual(0, self.driver.earned_money)

    def test_representation(self):
        result = str(self.driver)
        expected_output = "Pesho has 0 miles behind his back."
        self.assertEqual(expected_output, result)


if __name__ == '__main__':
    main()
