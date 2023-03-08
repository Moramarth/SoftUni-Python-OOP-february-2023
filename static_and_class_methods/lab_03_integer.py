"""
Create a class called Integer. Upon initialization, it should receive a single parameter value (int).
It should have 3 additional methods:

•	from_float(float_value) - creates a new instance by flooring the provided floating number.
If the value is not a float, return a message "value is not a float"

•	from_roman(value) - creates a new instance by converting the roman number (as string) to an integer

•	from_string(value) - creates a new instance by converting the string to an integer (if the value cannot be converted,
return a message "wrong type")
"""


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if type(float_value) is not float:
            return "value is not a float"

        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        for i in range(len(value)):
            if i != 0 and roman_symbols[value[i]] > roman_symbols[value[i - 1]]:
                result += roman_symbols[value[i]] - 2 * roman_symbols[value[i - 1]]
            else:
                result += roman_symbols[value[i]]

        return cls(result)

    @classmethod
    def from_string(cls, value: str):
        if type(value) is str:
            try:
                result = int(value)
                return cls(result)
            except ValueError:
                return "wrong type"
        return "wrong type"
