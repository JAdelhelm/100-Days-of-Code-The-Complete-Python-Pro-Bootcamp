import colorgram
from turtle import Turtle, Screen
from random import randint, choice
# colors = colorgram.extract("Day_18\image.jpg",30)
colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colorgram.extract("Day_18\image.jpg",30)]
print(colors)


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("blank")
# timmy_the_turtle.pensize(1)
timmy_the_turtle.penup()
timmy_the_turtle.speed(0)

screen = Screen()
screen.colormode(255)

timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(450)
timmy_the_turtle.setheading(0)

number_of_dots = 50

for dot_count in range(1, number_of_dots+1):
    timmy_the_turtle.fd(50); timmy_the_turtle.dot(15,choice(colors))

    if dot_count % 10 == 0:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(50)
        timmy_the_turtle.setheading(180)
        timmy_the_turtle.forward(500)
        timmy_the_turtle.setheading(0)
