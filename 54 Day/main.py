#%%
import time

def speed_decorator(function):
    name_of_function = function.__name__
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{name_of_function} run speed: {end_time - start_time}")
    return wrapper_function

@speed_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_decorator
def slow_function():
    for i in range(10000000):
        i*i

fast_function()
slow_function()