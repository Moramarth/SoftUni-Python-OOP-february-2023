from exam_preparation.python_oop_exam_16_august_2020.system_split.software.software import Software


class LightSoftware(Software):

    __CAPACITY_CONSUMPTION_INCREASE = 0.5
    __MEMORY_CONSUMPTION_DECREASE = 0.5

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.default_type, capacity_consumption, memory_consumption)
        self.capacity_consumption = int(self.capacity_consumption
                                          + (self.capacity_consumption * self.__CAPACITY_CONSUMPTION_INCREASE))
        self.memory_consumption = int(self.memory_consumption
                                        - (self.memory_consumption * self.__MEMORY_CONSUMPTION_DECREASE))

    @property
    def default_type(self):
        return "Light"
