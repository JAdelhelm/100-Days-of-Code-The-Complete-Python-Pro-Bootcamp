from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(20)
def move_backwards():
    tim.backward(20)
def turn_left():
    tim.left(10)
def turn_right():
    tim.right(10)

def clean_screen():
    tim.reset()

    


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clean_screen)

screen.exitonclick() 
