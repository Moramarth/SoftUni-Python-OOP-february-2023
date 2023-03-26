def logged(function):
    def wrapper(*args):
        name = function.__name__
        output = function(*args)

        return f"you called {name}{args}\nit returned {output}"
    return wrapper
