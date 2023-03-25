"""
Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int).
Implement the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0)
with the given step.
"""


class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.__current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            self.__current += self.step
            self.count -= 1
            return self.__current - self.step
        raise StopIteration
