def even_parameters(function):
    def wrapper(*args):
        if all(type(param) is int and param % 2 == 0 for param in args):
            result = function(*args)
            return result
        return "Please use only even numbers!"

    return wrapper
