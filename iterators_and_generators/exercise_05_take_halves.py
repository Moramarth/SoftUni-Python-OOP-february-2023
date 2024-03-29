"""
Implement the three generator functions:
•	integers() - generates an infinite amount of integers (starting from 1)
•	halves() - generates the halves of those integers (each integer / 2)
•	take(n, seq) - takes the first n halves of those integers
"""


def solution():

    def integers():
        integer = 1
        while True:
            yield integer
            integer += 1

    def halves():

        for i in integers():
            yield i / 2

    def take(n, seq):
        result = list()
        for _ in range(n):
            result.append(next(seq))
        return result

    return take, halves, integers
