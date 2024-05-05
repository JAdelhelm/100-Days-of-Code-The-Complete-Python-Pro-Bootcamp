#%%
from turtle import Turtle, Screen
from ball import Ball
from beater import Beater
from screenboard import Screenboard
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
screen.title("Pong")
screen.tracer(0,0)

screen_b = Screenboard()

beater_left = Beater(position="left")
beater_right = Beater(position="right")

screen.listen()
screen.onkeypress(beater_left.up, "W")
screen.onkeypress(beater_left.up, "w")
screen.onkeypress(beater_left.down, "S")
screen.onkeypress(beater_left.down, "s")

screen.onkeypress(beater_right.up, "Up")
screen.onkeypress(beater_right.down, "Down")


ball_1 = Ball()

SCORE_LEFT = 0
SCORE_RIGHT = 0

game_is_on = True
while game_is_on:
# for i in range(0,100,3):  
    screen.update()
    # time.sleep(0.07)
    ball_1.move()

    if ball_1.ycor() > 290 or ball_1.ycor() < -290:
        ball_1.bounce()

    position_beater_left =  beater_left.get_position_beater()
    position_beater_right =  beater_right.get_position_beater()


    if  ball_1.distance(position_beater_left[0]) < 20 or ball_1.distance(position_beater_left[1]) < 20 or ball_1.distance(position_beater_left[2]) < 20: 
        # ball_1.x_move *= -1   
        ball_1.bounce_x()
        # ball_1.speed *= 0.9
        # print(ball_1.speed())
        

    if  ball_1.distance(position_beater_right[0]) < 20 or ball_1.distance(position_beater_right[1]) < 20 or ball_1.distance(position_beater_right[2]) < 20: 
        # ball_1.x_move *= -1
        ball_1.bounce_x()
        # ball_1.speed *= 0.9
        # print(ball_1.speed())


    if ball_1.xcor() > 300: 
        # Logik einbinden, dass Score für links hochzählt und refresh
        print("point for left")
        SCORE_LEFT += 1
        screen_b.reset()
        screen_b = Screenboard(score_left=SCORE_LEFT, score_right=SCORE_RIGHT)
        
        time.sleep(2)
        
        ball_1.hideturtle()
        ball_1 = Ball()

    if ball_1.xcor() < -300: 
        # Logik einbinden, dass Score für rechts hochzählt und refresh
        print("point for right")
        SCORE_RIGHT += 1
        screen_b.reset()
        screen_b = Screenboard(score_left=SCORE_LEFT, score_right=SCORE_RIGHT)
        time.sleep(2)
        
        ball_1.hideturtle()
        ball_1 = Ball()
    
        

screen.exitonclick()
