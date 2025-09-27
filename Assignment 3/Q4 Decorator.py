def upper_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


@upper_decorator
def display_greeting():
    return "Hello World!"


print(display_greeting())
