"""
Create a class called vowels, which should receive a string. Implement the __iter__ and __next__ methods,
so the iterator returns only the vowels from the string.
"""


class vowels:
    __vowels = ["a", "e", "i", "u", "y", "o"]

    def __init__(self, random_string: str):
        self.random_string = random_string
        self.vowels_in_string = [letter for letter in self.random_string if letter.lower() in self.__vowels]
        self.__current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_index < len(self.vowels_in_string):
            self.__current_index += 1
            return self.vowels_in_string[self.__current_index - 1]
        raise StopIteration
