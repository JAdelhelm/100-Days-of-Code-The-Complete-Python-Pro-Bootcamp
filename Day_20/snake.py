from turtle import Turtle, Screen
from decimal import Decimal
def round_if_float(value):
    if isinstance(value, float):
        return Decimal(str(value)).quantize(Decimal('1.00'))
    else:
        return value

def rounded_tuple(tup):
    return tuple(round_if_float(value) for value in tup)

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]

MOVE_DISTANCE = 20

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_1 = self.create_snake()
        self.position_tuple_x = None
        self.position_tuple_y = None 
        self.absolute_position_tuple = self.get_all_positions()

    def create_snake(self):
        squares = []

        for position in STARTING_POSITIONS:
            square = Turtle("square")
            square.color("white")
            square.penup()
            square.goto(position)
            squares.append(square)
        return squares


    def move(self):
        # Das muss hier 20 sein, da ansonsten mehr gegangen wird und die Würfel
        # dann auseinander gehen
        snake_pos_tuple_x = []
        snake_pos_tuple_y = []

        for seg_num in range(len(self.snake_1) - 1 , 0, -1):
            new_x = self.snake_1[seg_num - 1].xcor()
            new_y = self.snake_1[seg_num - 1].ycor()
            self.snake_1[seg_num].goto(new_x, new_y)  

        for square_pos in range(len(self.snake_1)):
            snake_pos_tuple_x.append(round(self.snake_1[square_pos].pos()[0])) 
            snake_pos_tuple_y.append(round(self.snake_1[square_pos].pos()[1])) 


        self.position_tuple_x = snake_pos_tuple_x   
        self.position_tuple_y  = snake_pos_tuple_y


        self.snake_1[0].forward(MOVE_DISTANCE)

    def get_all_positions(self):

        check = [rounded_tuple(turt.pos()) for turt in self.snake_1[1:]]
        return check
        # print(check)
        # check = []
        # for squar_pos in range(len(self.snake_1) - 1, 0, -1):
        #     check.append(self.snake_1[squar_pos - 1].pos())

        # return check
  





    def up(self):
        actual_heading = int(self.snake_1[0].heading())
        # print(actual_heading)
        if actual_heading == 270: print("Wrong direction!")
        else:  self.snake_1[0].setheading(90)    
     

    def down(self):
        actual_heading = int(self.snake_1[0].heading())
        if actual_heading == 90: print("Wrong direction!")
        else: self.snake_1[0].setheading(270)

    def right(self):
        actual_heading = int(self.snake_1[0].heading())
        if actual_heading == 180: print("Wrong direction!")
        else: self.snake_1[0].setheading(0)     

    def left(self):
        actual_heading = int(self.snake_1[0].heading())
        if actual_heading == 0: print("Wrong direction!")
        else: self.snake_1[0].setheading(180)    

    def append_new_square(self):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(self.snake_1[-1].xcor(), self.snake_1[-1].ycor())

        self.snake_1.append(square)
    






          
