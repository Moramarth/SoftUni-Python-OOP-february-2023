"""
Create a class called store_results. It should be used as a decorator and store information about the executed functions
in a file called results.txt in the format: "Function {func_name} was called. Result: {func_result}"
"""


class store_results:
    _file_path = "results.txt"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        text_for_file = f"Function {self.func.__name__} was called. Result: {self.func(*args, **kwargs)}"
        with open(self._file_path, "a") as storage:
            storage.write(text_for_file + "\n")
        return self.func(*args, **kwargs)


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


print(add(2, 2))
print(mult(6, 4))
