"""
Build the classic arcade game where you shoot down alien ships.
"""

#%%
from turtle import Turtle, Screen, bgcolor, window_height, window_width
import random
import time







class SpaceInvader(Turtle):
    def __init__(self, width_window=1280, heigth_window=768) -> None:
        super().__init__()

        self.list_of_enemies = []
        self.list_of_shots = []
        self.list_of_enemy_shots = []

        self.width_window = width_window
        self.heigth_window = heigth_window

        self.current_score = 0

        bgcolor("black")
        # Setup Turtle - Design and Position
        self.hideturtle()
        self.penup()
        self.goto(0,-300)
        self.showturtle()
        self.shapesize(0.5,4,1)
        self.color("blue")

        # Setup Screen
        self.screen = self.getscreen()
        self.screen.register_shape("./player.gif")
        self.screen.title("Space Invaders")
        self.shape("./player.gif")

        self.screen.register_shape("./enemy.gif")
        self.screen.setup(self.width_window,self.heigth_window)

        # Automatic refresh of screen deactivated
        self.screen.tracer(0,0)
        # Build enemies
        y_position = 150
        for i in range(0,4):
            self.build_enemies(y_position=y_position)
            y_position += 30
        self.screen.update()

        self.start_life = 3
        self.current_life = self.start_life

        self.allowed_shots = 1
        self.removed_enemies = 0

        # Start game when pressing a key
        self.game_started = False


        

        # Setup Keyboard Binding

        self.screen.onkeypress(self.keyboard_left, "Left")
        self.screen.onkeypress(self.keyboard_right, "Right")
        self.screen.onkeypress(self.shoot, "space")
        self.screen.listen()

        self.y_move = 0.9

        self.screen.update()     
        self.game_has_started = True
        while self.game_has_started:
            self.random_shots_enemies()
            self.control_enemy_shots()

            self.control_shots()
            self.check_if_player_hitted()
            self.hitted_enemy_check()

            # Speed up shots
            # if self.removed_enemies >= 20 and self.y_move <= 1.1:
            self.y_move += 0.01

            self.scoreboard()
            self.lifeboard()
            if self.current_life == 0:
                # print("GAME OVER")
                self.game_over_board()
                self.screen.update()
                break

            self.destroy_old_shots()
            self.screen.update()



        self.screen.exitonclick()

    def destroy_old_shots(self):
        for shot in self.list_of_enemy_shots:
            if shot.ycor() <= -1*self.heigth_window / 2:
                shot.hideturtle()
                self.list_of_enemy_shots.remove(shot)

    def game_over_board(self):
        try: self.game_b.reset()
        except: pass

        self.game_b = Turtle()
        self.game_b.hideturtle()
        self.game_b.penup()

        self.game_b.goto(0, self.heigth_window/2-100)
        self.game_b.color("white")
        self.game_b.write(f"Game Over!", align="center", font=("Arial", 24, "bold"))

    def scoreboard(self):
        try:  self.score_b.reset()
        except: pass

        self.score_b = Turtle()
        self.score_b.hideturtle()
        self.score_b.penup()

        self.score_b.goto(-1*self.width_window/2+100, self.heigth_window/2-100)
        self.score_b.color("white")
        self.score_b.write(f"Score: {self.removed_enemies*3}", align="center", font=("Arial", 24, "bold"))

    def lifeboard(self):
        try: self.life_b.reset()
        except: pass

        self.life_b = Turtle()
        self.life_b.hideturtle()
        self.life_b.penup()

        self.life_b.goto(self.width_window/2-100, self.heigth_window/2-100)
        self.life_b.color("white")
        self.life_b.write(f"Life: {self.current_life}", align="center", font=("Arial", 24, "normal"))



    def random_shots_enemies(self):
        random.seed(random.randint(0,1000), random.randint(0,1000))
        pick_enemy = random.choice(self.list_of_enemies)

        if self.game_started == False:
            self.game_started = True

        if len(self.list_of_enemy_shots) < self.allowed_shots:
            shot_turtle = Turtle(shape="square")
            shot_turtle.color("blue")
            shot_turtle.shapesize(0.5,0.5,0.5)
            shot_turtle.penup()

            x_pos, y_pos = pick_enemy.position()
            shot_turtle.setpos(x=x_pos, y=y_pos-15)

            self.list_of_enemy_shots.append(shot_turtle)  

        # self.screen.update()


    def control_enemy_shots(self):
        for shot in self.list_of_enemy_shots:
            new_y = shot.ycor() - self.y_move
            shot.setheading(shot.towards(shot.xcor(), new_y))
            shot.goto(shot.xcor(), new_y)

    def build_enemies(self, y_position):
        tick = 40
        for enemy in range(int(self.width_window/60)):
            enemy = Turtle(shape="./enemy.gif")
            # print(bracket.getturtle())
            self.list_of_enemies.append(enemy.getturtle())
            # enemy.hideturtle()
            enemy.shapesize(0.5, 3, 1)
            enemy.penup()
            # bracket.goto(-1*self.width_window/2+tick, y_position)
            enemy.setpos(-1*self.width_window/2+tick, y_position)
            enemy.showturtle()
            tick += 60  

    def check_if_player_hitted(self):
        player_got_hitted = False
        for shot in self.list_of_enemy_shots:
            if player_got_hitted == False and abs(self.xcor() - shot.xcor()) < 30 and abs(self.ycor() - shot.ycor()) < 30:
                player_got_hitted = True
                self.current_life -= 1
                shot.hideturtle()
                self.list_of_enemy_shots.remove(shot)
                break




    def shoot(self):
        if self.game_started == False:
            self.game_started = True

        shot_turtle = Turtle(shape="circle")
        shot_turtle.color("red")
        shot_turtle.shapesize(0.5,0.5,0.5)
        shot_turtle.penup()
        # shot_turtle.speed("fastest")

        x_pos, y_pos = self.position()
        shot_turtle.setpos(x=x_pos, y=y_pos+10)

        self.list_of_shots.append(shot_turtle)

        # self.screen.update()
        # print(self.current_life)
        # print(len(self.list_of_enemies), len(self.list_of_enemy_shots), len(self.list_of_shots))


    def hitted_enemy_check(self):
        for enemy in self.list_of_enemies:
            for shot in self.list_of_shots:
                if abs(enemy.xcor() - shot.xcor()) < 40 and abs(enemy.ycor() - shot.ycor()) < 40:
                    enemy.hideturtle()
                    shot.hideturtle()
                    # enemy.reset()
                    # shot.reset()
                    self.list_of_enemies.remove(enemy)
                    self.list_of_shots.remove(shot)

                    self.removed_enemies += 1
                    if self.removed_enemies % 5 == 0 and self.removed_enemies <= 35: 
                        self.allowed_shots += 1
                    elif self.removed_enemies > 35:
                        self.allowed_shots = 5
                if shot.ycor() <= -1*self.heigth_window / 2 or shot.ycor() >= self.heigth_window / 2:
                    # Remove Shot if out of window
                    shot.hideturtle()
                    self.list_of_shots.remove(shot)

    def control_shots(self):
        for shot in self.list_of_shots:
            new_y = shot.ycor() + self.y_move
            shot.setheading(shot.towards(shot.xcor(), new_y))
            shot.goto(shot.xcor(), new_y)

    def keyboard_left(self):
        if self.game_started == False:
            self.game_started = True
            
        # 70 pixels bracket size
        if self.xcor() > -1*self.width_window/2+30:
            self.goto(self.xcor()-30, self.ycor())
        # self.screen.update()

    def keyboard_right(self):   
        if self.game_started == False:
            self.game_started = True

        if self.xcor() < self.width_window/2-30:
            self.goto(self.xcor()+30, self.ycor())
        # self.screen.update()
# 








        
if __name__ == "__main__":
    game = SpaceInvader()