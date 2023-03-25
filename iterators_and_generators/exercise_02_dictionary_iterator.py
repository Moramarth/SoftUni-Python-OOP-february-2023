"""
Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object. Implement the
iterator to return each key-value pair of the dictionary as a tuple of two elements (the key and the value).
"""


class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.output = list(self.dictionary.items())
        self.__current_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.output) > self.__current_item:
            self.__current_item += 1
            return self.output[self.__current_item - 1]
        raise StopIteration
