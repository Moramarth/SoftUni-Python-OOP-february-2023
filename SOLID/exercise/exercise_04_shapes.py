"""
Tasks come in all shapes and sizes

Test examples provided at the end of file.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, base: float, side_b: float, side_c: float, height: float):
        self.base = base
        self.side_b = side_b
        self.side_c = side_c
        self.height = height

    def calculate_area(self) -> float:
        return self.base * self.height / 2

    def calculate_perimeter(self) -> float:
        return self.base + self.side_b + self.side_c


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return pi * self.radius ** 2

    def calculate_perimeter(self) -> float:
        return 2 * pi * self.radius


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def calculate_area(self) -> float:
        return self.side ** 2

    def calculate_perimeter(self) -> float:
        return 4 * self.side


class Trapezium(Shape):
    def __init__(self, base_a: float, base_b: float, side_c: float, side_d: float, height: float):
        self.base_a = base_a
        self.base_b = base_b
        self.side_c = side_c
        self.side_d = side_d
        self.height = height

    def calculate_area(self) -> float:
        return (self.base_a + self.base_b) * self.height / 2

    def calculate_perimeter(self) -> float:
        return self.base_a + self. base_b + self.side_c + self.side_d


class ShapeCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise ValueError("`shapes` should be of type `list`.")
        self.__shapes = value


class AreaCalculator(ShapeCalculator):
    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()

        return total


class PerimeterCalculator(ShapeCalculator):
    @property
    def total_perimeter(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_perimeter()

        return total


geometric_figures = [
    Rectangle(2, 3),
    Rectangle(1, 6),
    Circle(6.2),
    Square(7),
    Trapezium(10, 4, 3, 3.5, 2),
    Triangle(9, 4, 7, 5)
]

area_calculator = AreaCalculator(geometric_figures)
print(f"The total area is:  {area_calculator.total_area:.2f}")

perimeter_calculator = PerimeterCalculator(geometric_figures)
print(f"The total perimeter is:  {perimeter_calculator.total_perimeter:.2f}")

try:
    area_calculator_2 = AreaCalculator("Rectangle(2, 3), Rectangle(1, 6), Circle(6.2), Square(7)")
except ValueError as error:
    print(error)

try:
    perimeter_calculator_2 = PerimeterCalculator({"Rectangle": (2, 3), "Circle": 6.2, "Square": 7})
except ValueError as error:
    print(error)
