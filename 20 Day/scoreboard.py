from turtle import Turtle, Screen
import time


class Scoreboard(Turtle):

    def __init__(self, actual_score=0):
        super().__init__()
        self.actual_score = actual_score
        self.goto((0, 260))
        self.color("white")
        self.shape("blank")
        self.write(f"Score: {actual_score}", align="center", font=("Arial", 18, "normal"))

    def game_over(self):
        self.goto((0, 0))
        self.color("white")
        self.shape("blank")
        self.write(f"GAME OVER", align="center", font=("Arial", 18, "normal"))

        
        
        

