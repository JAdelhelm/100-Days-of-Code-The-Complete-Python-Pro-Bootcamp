from turtle import Turtle
import time
import random
class Ball(Turtle):
    
    START_CHOICES = [0.1, -0.1, 0.1, -0.1]
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.first = True
        self.lock = False
        if self.first == True:
            self.x_move = random.choice(Ball.START_CHOICES)
            self.y_move = random.choice(Ball.START_CHOICES)
            self.first = False
        else:
        # self._tracer(0,0)
            self.move_speed = 0.1
            self.x_move = 0.1
            self.y_move = 0.1


    def bounce_x(self):
        self.x_move *= -1
        if self.x_move >= 0.75:
            self.lock = True
        if self.lock == False:
            self.x_move *= 1.2
       
        # print(self.x_move)
        

    def move(self):
        new_x = self.xcor() + self.x_move 
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

