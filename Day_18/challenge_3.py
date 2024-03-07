from turtle import Turtle, Screen
from random import randint

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")


screen = Screen()
screen.colormode(255)

DEGREE = 360
START = 2

BIGGER = 60

while True:
    r,g,b = randint(0,255), randint(0,255), randint(0,255)
    actual_degree = DEGREE / START
    for val in range(0, START):
        timmy_the_turtle.forward(BIGGER)
        timmy_the_turtle.right(actual_degree)
    timmy_the_turtle.color(r,g,b)
    START += 1


    



screen.exitonclick()


