from turtle import Turtle
from random import choice, randint
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10


        
class CarManager(Turtle):
    def __init__(self, speed_blocks=10):
        self.car_collection = self.initiate_cars()
        self.speed_blocks = speed_blocks

    def initiate_cars(self):
        cars = [Turtle() for car in range(0,50*5)]
        [car.penup() for car in cars]
        [car.goto((randint(-280*13,280*7),randint(-240,280))) for car in cars]
        [car.shape("square") for car in cars]
        [car.shapesize(1,2,1) for car in cars]
        [car.color(choice(COLORS)) for car in cars]
        return cars

    
    def move_cars(self):
        [car.goto(car.xcor()-self.speed_blocks,car.ycor()) for car in self.car_collection]

    def reset_cars(self):
        [car_r.hideturtle() for car_r in self.car_collection]
  


