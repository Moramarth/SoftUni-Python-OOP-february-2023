"""
Create a class called Point. Upon initialization, it should receive x and y (numbers).
Create 3 instance methods:
-	set_x(new_x) - changes the x value of the point
-	set_y(new_y) - changes the y value of the point
-	__str__() - returns the coordinates of the point in the format "The point has coordinates ({x},{y})"
"""


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x: int):
        self.x = new_x

    def set_y(self, new_y: int):
        self.y = new_y

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"
