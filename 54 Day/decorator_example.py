#%%
import time


def delay_decorator(function):
    # Interne Funktion wird zweimal aufgerufen
    # 
    # Es wird eine Funktion ummantelt, so dass diese die ursprüngliche Funktion
    # sozusagen überschreibt.
    def wrapper_function():
        print("Die Wrapper Funktion wird aufgerufen, welche das Verhalten der übergebenen Funktion bestimmt")
        time.sleep(2)
        function()
        time.sleep(2)
        function()
    # Funktion wird zurückgegeben
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")



if __name__ == "__main__":
    say_hello()