def vowel_filter(function):

    def wrapper():

        result = function()
        result = [char for char in result if char.lower() in "aeiouy"]

        return result
    return wrapper
