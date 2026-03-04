import time


def execution_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
    return wrapper

@execution_time
def example_function():
    print("This is an example function.")
    # time.sleep(2)  # Simulating a time-consuming task 

example_function()
