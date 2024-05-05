from turtle import Turtle

class TextTurtle(Turtle):
    def __init__(self, text_state, x_cor, y_cor) -> None:
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("blank")
        self.goto(x_cor, y_cor)
        self.write(f"{text_state}", font=["Arial", 10])
        self.score = 0
