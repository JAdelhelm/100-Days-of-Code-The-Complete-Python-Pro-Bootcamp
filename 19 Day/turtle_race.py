from turtle import Turtle, Screen
from random import choice,randint

screen_1 = Screen()
screen_1.setup(width=800, height=600)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "white", "black"]

user_bet = screen_1.textinput("Make your bet", prompt="Which turtle will win the race? Enter a color: ")

NUMBER_OF_TURTLES = 8

turtle_list = [Turtle() for val in range(NUMBER_OF_TURTLES)]

[turtle.shape("turtle") for turtle in turtle_list]
[turtle_list[position].color(colors[position]) for position in range(NUMBER_OF_TURTLES)]
[turtle.penup() for turtle in turtle_list]
[turtle_list[position].setposition(-230,-200+position*50) for position in range(NUMBER_OF_TURTLES) ]


while True:
    pick_turtle = turtle_list[randint(0,NUMBER_OF_TURTLES-1)]
    pick_turtle.forward(10)

    color_of_actual_turtle = pick_turtle.color()
    position_of_actual_turtle = pick_turtle.position()

    if position_of_actual_turtle[0] >= 800:
        print(f"The {color_of_actual_turtle[0]} turtle won the race!")
        # print(position_of_actual_turtle)
        break
    # print(color_of_actual_turtle)
    # print(position_of_actual_turtle)









screen_1.exitonclick()
