"""
Create a generator function called reverse_text that receives a string and yields all string characters on one line
in reversed order.
"""


def reverse_text(text):
    for char in reversed(text):
        yield char
