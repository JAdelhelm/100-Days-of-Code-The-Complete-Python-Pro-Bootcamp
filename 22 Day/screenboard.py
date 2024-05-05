from turtle import Turtle, Screen
import time


class Screenboard(Turtle):

    def __init__(self, score_left=0, score_right=0):

        super().__init__()
        self.score_left = score_left
        self.score_right = score_right
        self.goto((0, 260))
        self.color("white")
        self.shape("blank")
        self.write(f"{score_left}     {score_right}", align="center", font=("Arial", 24, "normal"))
        self.mid_lane()

    def mid_lane(self):
        for pos in range(280,-280,-40):
            line = Turtle("square")
            line.penup()
            line.shapesize(1,0.1,1)
            line.color("white")
            line.setposition(0,pos)  


    def game_over(self):
        self.goto((0, 0))
        self.color("white")
        self.shape("blank")
        self.write(f"GAME OVER", align="center", font=("Arial", 18, "normal"))

        