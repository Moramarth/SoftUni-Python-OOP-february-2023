def type_check(needed_type):
    def decorator(function):
        def wrapper(*args):
            if all(type(param) is needed_type for param in args):
                return function(*args)
            return "Bad Type"
        return wrapper
    return decorator
