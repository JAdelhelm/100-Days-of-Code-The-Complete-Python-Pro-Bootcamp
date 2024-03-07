from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        # print("UP")
        # print(self.xcor(), self.ycor())
        self.goto(self.xcor(), self.ycor() + 10)

    def finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True

        


