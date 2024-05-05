def add(*args):
    print(type(args))
    return sum([num for num in args])

print(add(5,5,5,10))

def calculate(**kwargs):
    print(type(kwargs))
    print(kwargs)


calculate(add=3, multiply=5)


class Car:
    def __init__(self, **kw) -> None:
        self.make = kw["make"]
        # Get gibt kein Error zurück
        self.model = kw.get("model")


my_car = Car(make="Nissan",model="GT-R")

print(my_car.model)

my_car_2 = Car(make="Audi")
print(my_car_2.model)