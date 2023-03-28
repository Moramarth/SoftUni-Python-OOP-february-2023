import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test_worker = Worker("Petar Yordanov", 2300, 3)

    def test_if_constructor_is_properly_working(self):
        self.assertEqual(self.test_worker.name, "Petar Yordanov")
        self.assertEqual(self.test_worker.salary, 2300)
        self.assertEqual(self.test_worker.energy, 3)

    def test_if_energy_is_increased_after_resting(self):
        self.test_worker.rest()
        self.assertEqual(self.test_worker.energy, 4)

    def test_working_with_zero_energy_raised_error(self):
        self.test_worker.energy = 0

        with self.assertRaises(Exception) as context:
            self.test_worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_working_with_negative_energy_raised_error(self):
        self.test_worker.energy = -11

        with self.assertRaises(Exception) as context:
            self.test_worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_salary_increase_after_work_method(self):
        self.test_worker.work()
        self.assertEqual(self.test_worker.money, 2300)

    def test_energy_is_decreased_after_work_method(self):
        self.test_worker.work()
        self.assertEqual(self.test_worker.energy, 2)

    def test_method_get_info_returns_proper_string(self):
        result = self.test_worker.get_info()
        expected_output = 'Petar Yordanov has saved 0 money.'
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
