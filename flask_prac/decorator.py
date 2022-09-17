import time
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do Something before
        function()
        # function()
        # Do something after
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

say_hello()

decorated_function = delay_decorator(say_bye)