def cache(function):
    def wrapper(number):
        if number not in wrapper.log:
            wrapper.log[number] = function(number)

        return wrapper.log[number]

    wrapper.log = dict()

    return wrapper


@cache
def fibonacci(n):

    if n < 2:

        return n

    else:

        return fibonacci(n - 1) + fibonacci(n - 2)
