from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from decimal import Decimal
def round_if_float(value):
    if isinstance(value, float):
        return Decimal(str(value)).quantize(Decimal('1.00'))
    else:
        return value

def rounded_tuple(tup):
    return tuple(round_if_float(value) for value in tup)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
# print(snake.position_tuple)

food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

SCORE = 0

score_board = Scoreboard()

positions_snake = []

game_is_on = True
while game_is_on:
# for i in range(0,100,3):  
    screen.update()
    time.sleep(0.1)
 
    snake.move()
    # if i%7 == 0: snake.append_new_square()

    if snake.snake_1[0].distance(food) < 15: 
        SCORE += 1
        score_board.reset()
        score_board = Scoreboard(SCORE)
        snake.append_new_square()
        print("Nom nom nom")
        food.refresh()

    if (300 in snake.position_tuple_x) or (300 in snake.position_tuple_y) or (-300 in snake.position_tuple_x) or (-300 in snake.position_tuple_y):
        score_board.game_over() ;  time.sleep(5) ; break
    # print(snake.position_tuple_x, snake.position_tuple_y)
    if rounded_tuple(snake.snake_1[0].pos()) in positions_snake: score_board.game_over() ; time.sleep(5) ; break
    

    positions_snake = snake.get_all_positions()
    