from exam_preparation.python_oop_exam_16_august_2020.system_split.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = list()
        self.capacity_used = 0
        self.memory_used = 0

    def install(self, software: Software):
        if self.capacity_used + software.capacity_consumption <= self.capacity \
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
