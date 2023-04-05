from abc import ABC, abstractmethod


class BaseDecoration(ABC):
    def __init__(self, comfort: int, price: float):
        self.comfort = comfort
        self.price = price

    @property
    @abstractmethod
    def default_price(self):
        pass

    @property
    @abstractmethod
    def default_comfort(self):
        pass
