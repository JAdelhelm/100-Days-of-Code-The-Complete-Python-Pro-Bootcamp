import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()

player_1 = Player()

screen.listen()
screen.onkeypress(player_1.up, "Up")

car_m = CarManager()

ACTUAL_LEVEL = 0
SPEED_INCREASE = 10

# Logik der Kollidierung noch reinbringen
got_hit = False

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # coordinates_of_cars = [(car.xcor(), car.ycor()) for car in car_m.car_collection]
    

    check_finish = player_1.finish_line()
    if check_finish == True:
        ACTUAL_LEVEL += 1
        SPEED_INCREASE += 2
        scoreboard.reset()
        scoreboard = Scoreboard(ACTUAL_LEVEL)
        car_m.reset_cars()
        car_m = CarManager(SPEED_INCREASE)
        
    for car in car_m.car_collection:   
        if player_1.distance(car) <= 20:
            got_hit = True
            
    if got_hit == True:
        break
    

    car_m.move_cars()
  
    
