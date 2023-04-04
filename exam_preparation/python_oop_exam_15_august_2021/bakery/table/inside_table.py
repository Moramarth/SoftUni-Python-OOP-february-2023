from exam_preparation.python_oop_exam_15_august_2021.bakery.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number_range(self):
        return range(1, 51)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value not in self.table_number_range:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
        self.__table_number = value
