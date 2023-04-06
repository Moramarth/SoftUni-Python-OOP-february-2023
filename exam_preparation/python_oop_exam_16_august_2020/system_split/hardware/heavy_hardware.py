from exam_preparation.python_oop_exam_16_august_2020.system_split.hardware.hardware import Hardware
from exam_preparation.python_oop_exam_16_august_2020.system_split.software.software import Software


class HeavyHardware(Hardware):
    __CAPACITY_INCREASE = 2
    __MEMORY_DECREASE = 0.75

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self.default_type, capacity, memory)
        self.capacity *= self.__CAPACITY_INCREASE
        self.memory = int(self.memory * self.__MEMORY_DECREASE)
        self.capacity_used = 0
        self.memory_used = 0

    @property
    def default_type(self):
        return "Heavy"

    def install(self, software: Software):
        if self.capacity_used + software.capacity_consumption <= self.capacity\
                and self.memory_used + software.memory_consumption <= self.memory:
            self.software_components.append(software)
            self.capacity_used += software.capacity_consumption
            self.memory_used += software.memory_consumption
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        self.software_components.remove(software)
        self.capacity_used -= software.capacity_consumption
        self.memory_used -= software.memory_consumption
