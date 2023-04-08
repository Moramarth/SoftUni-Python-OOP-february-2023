from abc import ABC, abstractmethod


class BaseService(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots = list()  # stores instances of class BaseRobot

    @property
    @abstractmethod
    def type_of_service(self):
        pass

    @property
    @abstractmethod
    def default_capacity_for_type(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Service name cannot be empty!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")
        self.__capacity = value

    def details(self):
        return f"{self.name} {self.type_of_service}:\n" \
               f"Robots: {', '.join(r.name for r in self.robots) if self.robots else 'none'}"
