from turtle import Turtle, Screen
from random import randint

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("blank")
timmy_the_turtle.color("red")
timmy_the_turtle.pensize(1)
timmy_the_turtle.speed(0)

screen = Screen()
screen.colormode(255)

DEGREE = 360
START = 0

BIGGER = 60

while True:
    r,g,b = randint(0,255), randint(0,255), randint(0,255)
    # timmy_the_turtle.right(START)
    timmy_the_turtle.circle(100)
    current_heading = timmy_the_turtle.heading()
    timmy_the_turtle.setheading(current_heading +10)
    timmy_the_turtle.color(r,g,b)
    START += 1


    



screen.exitonclick()


