from turtle import Turtle, Screen


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")


screen = Screen()

def square_turtle(turtle):
    for val in range(0,5+1):
        turtle.forward(5)
        timmy_the_turtle.penup()
        turtle.forward(5)
        timmy_the_turtle.pendown()

    timmy_the_turtle.left(90)

for val in range(4):
    square_turtle(timmy_the_turtle)


screen.exitonclick()


