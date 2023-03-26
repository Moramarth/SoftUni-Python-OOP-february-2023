def tags(tag):
    def decorator(func):
        def wrapper(*args):
            result = f"<{tag}>{func(*args)}</{tag}>"
            return result
        return wrapper
    return decorator
