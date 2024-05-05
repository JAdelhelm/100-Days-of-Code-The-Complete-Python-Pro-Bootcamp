# %%

# TODO: Create the logging_decorator() function
def logging_decorator(function):
    # Arguments and Keyword-Arguments from function
    def wrapper_function(*args, **kwargs):
        print(f"Name of the function: {function.__name__}")
        print(f"Arguments: {args} / Keyword-Arguments {kwargs}")
        result_function = function(*args)
        print(f"It returned: {result_function}")

    return wrapper_function

# TODO: Use the decorator
@logging_decorator
def a_function(a,b,c):
    return a*b*c

a_function(1,2,3)