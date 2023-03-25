"""
Create a class called countdown_iterator. Upon initialization, it should receive a count. Implement the iterator to
return each countdown number (from count to 0 inclusive), separated by a single space.
"""


class countdown_iterator:
    def __init__(self, number):
        self.number = number
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number >= self.end:
            self.number -= 1
            return self.number + 1
        raise StopIteration
