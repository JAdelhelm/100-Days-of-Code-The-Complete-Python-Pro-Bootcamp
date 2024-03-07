from turtle import Turtle
from decimal import Decimal
def round_if_float(value):
    if isinstance(value, float):
        return Decimal(str(value)).quantize(Decimal('1.00'))
    else:
        return value

def rounded_tuple(tup):
    return tuple(round_if_float(value) for value in tup)

class Beater(Turtle):

    
    def __init__(self, position=""):
        super().__init__()

        self.direction_beater = "down"
        

        if position == "left":
            self.beater = self.create_beater_left()
            # print(self.beater)
            self.up(); self.up(); self.down(); self.down()

        elif position == "right": 
            self.beater = self.create_beater_right()
            self.up(); self.up(); self.down(); self.down(); 
        else: print("No position specified")


    def create_beater_left(self):
        squares = []
        for position in [(-260, -20), (-260, 0), (-260,20) ]:
            square = Turtle("square")
            #########
            square.shapesize(0.4,1,1)
            square.setheading(90)
            #########
            square.color("white")
            square.penup()
            square.goto(position)
            squares.append(square) 
        return squares

    def create_beater_right(self):
        squares = []
        for position in [(260, 20), (260, 0), (260,-20) ]:
            square = Turtle("square")     
            #########
            square.shapesize(0.4,1,1) 
            square.setheading(90)
            #########
            square.color("white")
            square.penup()
            square.goto(position)
            squares.append(square) 
        return squares    

    def up(self):
        if self.direction_beater == "down": self.beater[0].goto(self.beater[-1].xcor(), self.beater[-1].ycor())
        self.direction_beater = "up"

        [square.setheading(90) for square in self.beater] 
        for seg_num in range(len(self.beater) - 1 , 0, -1):

            new_y = self.beater[seg_num - 1].ycor()
            if self.beater[0].ycor() < 300.0:
                self.beater[seg_num].goto(self.beater[0].xcor(), new_y) 
                
        if self.beater[0].ycor() - 20 < 300:  self.beater[0].forward(20)

        

    def down(self):
        if self.direction_beater == "up": self.beater[0].goto(self.beater[-1].xcor(), self.beater[-1].ycor())
        self.direction_beater = "down"

        [square.setheading(270) for square in self.beater]
        for seg_num in range(len(self.beater) - 1 , 0, -1):
            new_y = self.beater[seg_num - 1].ycor()
            if self.beater[0].ycor() > -300.0:
                self.beater[seg_num].goto(self.beater[0].xcor(), new_y)  
        if self.beater[0].ycor() + 20 > -300:  self.beater[0].forward(20)
      
    def get_position_beater(self):
        pos_beater  =  [turt.pos() for turt in self.beater]
        # print(pos_beater)
        return pos_beater
