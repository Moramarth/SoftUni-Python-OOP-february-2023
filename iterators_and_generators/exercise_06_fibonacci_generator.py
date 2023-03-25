"""
Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely.
The first two numbers in the sequence are always 0 and 1. Each following Fibonacci number is created by the sum of the
current number with the previous one.
"""


def fibonacci():
    yield 0

    yield 1
    current = 1
    previous = 0
    while True:
        yield current + previous
        current = current + previous
        previous = current - previous
