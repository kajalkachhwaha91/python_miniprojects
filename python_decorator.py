"""Example demonstrating a simple Python decorator."""

def my_decorator(func):
    def wrapper():
        print("executing the function...")
        func()
        print("function execution completed.")

    return wrapper


@my_decorator
def hello():
    print("In between the function execution.")

hello()
