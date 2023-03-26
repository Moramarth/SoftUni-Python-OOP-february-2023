def multiply(times):

    def decorator(function):

        def wrapper(*args):

            result = function(*args) * times
            return result

        return wrapper
    return decorator
