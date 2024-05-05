from turtle import Turtle
FONT = ("Courier", 24, "normal")
POSITION = (-280, 260)
class Scoreboard(Turtle):
    def __init__(self, actual_level = 0 ):
        super().__init__()
        self.penup()
        self.goto(POSITION)
        self.color("black")
        self.shape("blank")
        self.write(f"Level: {actual_level}", align="left", font=FONT)


