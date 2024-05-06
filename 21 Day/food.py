"""Spawn randomly, just not in the snake position"""
from turtle import Turtle, Screen
import random


class Food(Turtle):

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

        
    def __init__(self, current_positions_of_snake=None):
        self.current_positions_of_snake = current_positions_of_snake

        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()



        # while (random_x, random_y) in self.current_positions_of_snake:
        #     random_x = random.randint(-280, 280)
        #     random_y = random.randint(-280, 280)

        