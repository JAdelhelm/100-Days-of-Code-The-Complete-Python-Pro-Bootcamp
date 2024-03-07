def make_bold(function):
    def wrapper_function():
        result_of_function = function()
        modified_result_of_function = "<b>"+result_of_function+"</b>"
        return modified_result_of_function

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        result_of_function = function()
        modified_result_of_function = "<em>"+result_of_function+"</em>"
        return modified_result_of_function

    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        result_of_function = function()
        modified_result_of_function = "<u>"+result_of_function+"</u>"
        return modified_result_of_function

    return wrapper_function