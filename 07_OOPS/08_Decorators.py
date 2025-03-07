# Decorator in python is a function that modifies the behavior of another function or class without changing its actual code. Decorators allow for code reusability, cleaner syntax and seperation of concerns.


def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    return wrapper

@my_decorator  # Using decorator
def say_hello():
    print("Hello, world!")

say_hello()
