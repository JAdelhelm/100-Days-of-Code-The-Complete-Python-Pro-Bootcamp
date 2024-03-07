from turtle import Turtle, Screen
from random import randint, choice

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("blank")
timmy_the_turtle.color("red")
timmy_the_turtle.pensize(5)
timmy_the_turtle.speed(0)

screen = Screen()
screen.colormode(255)


START = 50
WALK =  10

while True:
    for val in range(0, START): 
        r,g,b = randint(0,255), randint(0,255), randint(0,255)
        choice_direction = randint(0,1)
        if choice_direction == 0:timmy_the_turtle.right(90)
        
        timmy_the_turtle.forward(10)
        timmy_the_turtle.color(r,g,b)

  



    



screen.exitonclick()


