"""
Create a class called sequence_repeat which should receive a sequence and a number upon initialization.
Implement an iterator to return the given elements, so they form a string with a length - the given number.
If the number is greater than the number of elements, then the sequence repeats as necessary
"""


class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.number = number
        self.sequence = sequence
        self.__current_index = 0

    @property
    def sequence(self):
        return self.__sequence

    @sequence.setter
    def sequence(self, value):
        while len(value) < self.number:
            value += value
        self.__sequence = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_index < self.number:
            self.__current_index += 1
            return self.sequence[self.__current_index - 1]
        raise StopIteration
