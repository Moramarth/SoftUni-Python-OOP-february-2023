from decorators.exercise_09_computer_store.project.computer_types.desktop_computer import DesktopComputer
from decorators.exercise_09_computer_store.project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = list()
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer == "Desktop Computer":
            new_computer = DesktopComputer(manufacturer, model)
        elif type_computer == "Laptop":
            new_computer = Laptop(manufacturer, model)
        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        config = new_computer.configure_computer(processor, ram)

        self.warehouse.append(new_computer)
        return config

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.processor == wanted_processor and computer.ram >= wanted_ram:
                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)
                return f"{computer} sold for {client_budget}$."
        raise Exception("Sorry, we don't have a computer for you.")
