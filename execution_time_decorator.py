import time


def execution_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
    return wrapper

def parameter_func(func):
    def wrapper(*args, **kwargs):
        print("Before executing the function.")
        func(*args, **kwargs)
        print("After executing the function.")
    return wrapper

@parameter_func
def add(a ,b):
    print(f"The sum of {a} and {b} is: {a + b}")
add(5, 10)

# @execution_time
# def example_function():
#     print("This is an example function.")
#     # time.sleep(2)  # Simulating a time-consuming task 

# example_function()
