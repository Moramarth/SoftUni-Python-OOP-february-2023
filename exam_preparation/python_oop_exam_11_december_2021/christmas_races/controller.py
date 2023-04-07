from exam_preparation.python_oop_exam_11_december_2021.christmas_races.car.muscle_car import MuscleCar
from exam_preparation.python_oop_exam_11_december_2021.christmas_races.car.sports_car import SportsCar
from exam_preparation.python_oop_exam_11_december_2021.christmas_races.driver import Driver
from exam_preparation.python_oop_exam_11_december_2021.christmas_races.race import Race


class Controller:
    def __init__(self):
        self.cars = list()  # stores instances of class Car
        self.drivers = list()  # stores instances of class Driver
        self.races = list()  # stores instances of class Race

    @staticmethod
    def attribute_collection_search(value, attribute, collection):
        for item in collection:
            if getattr(item, attribute) == value:
                return item

    def create_car(self, car_type: str, model: str, speed_limit: int):
        type_of_cars = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

        if self.attribute_collection_search(model, "model", self.cars):
            raise Exception(f"Car {model} is already created!")

        if car_type in type_of_cars:
            self.cars.append(type_of_cars[car_type](model, speed_limit))
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.attribute_collection_search(driver_name, "name", self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self.attribute_collection_search(race_name, "name", self.races):
            raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.attribute_collection_search(driver_name, "name", self.drivers)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car_type == "MuscleCar":
            if not any(car for car in self.cars if car.__class__.__name__ == car_type):
                raise Exception(f"Car {car_type} could not be found!")
            if all(car.is_taken for car in self.cars if car.__class__.__name__ == car_type):
                raise Exception(f"Car {car_type} could not be found!")
        elif car_type == "SportsCar":
            if not any(car for car in self.cars if car.__class__.__name__ == car_type):
                raise Exception(f"Car {car_type} could not be found!")
            if all(car.is_taken for car in self.cars if car.__class__.__name__ == car_type):
                raise Exception(f"Car {car_type} could not be found!")
        else:
            return

        new_car = None
        for i in range(len(self.cars) - 1, -1, -1):
            if car_type == self.cars[i].__class__.__name__ and not self.cars[i].is_taken:
                new_car = self.cars[i]
                break

        if driver.car:
            old_car = driver.car
            old_car.is_taken = False
            driver.car = new_car
            new_car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_car.model} to {new_car.model}."

        driver.car = new_car
        new_car.is_taken = True
        return f"Driver {driver_name} chose the car {new_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.attribute_collection_search(race_name, "name", self.races)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.attribute_collection_search(driver_name, "name", self.drivers)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.attribute_collection_search(race_name, "name", self.races)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_three_cars = list()
        car_speeds = [driver.car.speed_limit for driver in race.drivers]
        for i in range(3):
            driver = [driver for driver in race.drivers if driver.car.speed_limit == max(car_speeds)][0]
            fastest_three_cars.append(driver)
            car_speeds.remove(max(car_speeds))

        result = list()
        for driver in fastest_three_cars:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return "\n".join(result)
