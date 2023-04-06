from exam_preparation.python_oop_exam_16_august_2020.system_split.software.software import Software


class ExpressSoftware(Software):
    __MEMORY_CONSUMPTION_INCREASE = 2

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.default_type, capacity_consumption, memory_consumption)
        self.memory_consumption *= self.__MEMORY_CONSUMPTION_INCREASE

    @property
    def default_type(self):
        return "Express"
