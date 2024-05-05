# %%
from turtle import Turtle, Screen, bgcolor, window_height, window_width
import random
import time

# START_CHOICES_X = [-0.6, 0.6]
START_CHOICES_X = [random.uniform(-1.0, 1.0) for val in range(0,100)]
START_CHOICES_Y =  [-1.3]   

LIST_OF_TURTLES = []
class Breakout(Turtle):
    def __init__(self,shape="square", width_window=1280, heigth_window=768) -> None:
        super().__init__(shape)
        self.width_window = width_window
        self.heigth_window = heigth_window

        # Start direction ball
        self.x_move = random.choice(START_CHOICES_X)
        self.y_move = random.choice(START_CHOICES_Y)

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
        self.screen.setup(self.width_window,self.heigth_window)
        # Automatic refresh of screen deactivated
        self.screen.tracer(0,0)
        # Add Logo
        self.breakout_game_logo()
        # Add Scoreboard
        self.add_scoreboard()

        # Setup Brackets
        self.build_all_brackets()
        # self.screen.update()
        # self.screen.tracer(8, 25)


        # Setup Keyboard Binding

        self.screen.onkeypress(self.keyboard_left, "Left")
        self.screen.onkeypress(self.keyboard_right, "Right")
        self.screen.listen()
        # Setup Ball
        self.ball_control()
        self.screen.update()

        self.game_started = False

        self.game_is_on = True
        while self.game_is_on:
            if len(LIST_OF_TURTLES) <= 0:
                self.breakout_game_logo(text="GAME IS OVER! YOU WON!")
                # print("GAME IS OVER, YOU WON!")
                break

            self.screen.update()
            # print(len(LIST_OF_TURTLES))
            # time.sleep(0.5)
            if self.game_started == True:
                self.move_ball()

            self.screen.update()
            self.check_collision()
            self.screen.update()
            # print(self.ball.xcor())
            # print(self.ball.ycor())

            if abs(self.ball.xcor() - self.xcor()) < 70 and abs(self.ball.ycor() - self.ycor()) < 25:
                # print(self.ball.xcor() - self.xcor())
                if (self.ball.xcor() - self.xcor() < -32.0) or (self.ball.xcor() - self.xcor() > 32.0):
                    self.x_move *= -1

                self.y_move *= -1

                if self.y_move < 0:
                    if self.y_move <= 1.9:
                        self.x_move += -0.1
                        self.y_move += -0.1       
                    else:             
                        self.x_move += -0.05
                        self.y_move += -0.05
                    
                    self.x_move = round(self.x_move,3)
                    self.y_move = round(self.y_move,3)
                else:
                    if self. x_move <= 1.9:
                        self.x_move += 0.1
                        self.y_move += 0.1
                    else:
                        self.x_move += 0.05
                        self.y_move += 0.05
                    
                self.x_move = round(self.x_move,2)
                self.y_move = round(self.y_move,2)
                # print(self.y_move)
                # print(LIST_OF_TURTLES)

            

            ### Bouncing of Walls ###
            # Bottom - Lost game
            if self.ball.ycor() <= -1*self.heigth_window / 2:
                print("Game Over")
                break

            # Bottom / Top
            # if self.ball.ycor() <= -1*self.heigth_window / 2 or self.ball.ycor() >= self.heigth_window / 2:
            if  self.ball.ycor() >= self.heigth_window / 2:
                # print("Out of window")
                self.y_move *= -1
            # Left / Right
            if self.ball.xcor() <= -1*self.width_window / 2 or self.ball.xcor() >= self.width_window / 2:
                self.x_move *= -1


        # 
        self.screen.exitonclick()



    def check_collision(self):
        for single_turtle in LIST_OF_TURTLES:
            if abs(self.ball.xcor() - single_turtle.xcor()) < 60 and abs(self.ball.ycor() - single_turtle.ycor()) < 30: 
                # print("COLLISION")   
                single_turtle.reset()
                # single_turtle.hideturtle()

                LIST_OF_TURTLES.remove(single_turtle)
                # print(len(LIST_OF_TURTLES))
                self.y_move *= -1

                self.current_score += 3
                self.add_scoreboard()
                break
    
    def player_name(self):
        self.screen.textinput("NIM", "Name of first player:")

    def add_scoreboard(self):
        try: self.score_turtle.reset()
        except: pass

        self.score_turtle = Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.penup()

        self.score_turtle.goto(self.width_window/2-200, self.heigth_window/2-100)
        self.score_turtle.color("white")
        self.score_turtle.write(f"Score: {self.current_score}", align="center", font=("Arial", 24, "normal"))
        self.screen.update()
    
    def breakout_game_logo(self, text="BREAKOUT GAME"):
        try: self.title_turtle.reset()
        except: pass

        self.title_turtle = Turtle()
        self.title_turtle.hideturtle()
        self.title_turtle.penup()

        self.title_turtle.goto(0, self.heigth_window/2-100)
        self.title_turtle.color("white")
        self.title_turtle.write(text, align="center", font=("Arial", 24, "normal"))
        self.screen.update()


    def build_all_brackets(self):
        self.yellow_brackets()
        self.green_brackets()
        self.orange_brackets()
        self.red_brackets()
        # self.screen.tracer(None,None)
        
    def yellow_brackets(self):
        self.build_brackets(color="yellow", y_position=0)
        self.build_brackets(color="yellow", y_position=30)


    def green_brackets(self):
        self.build_brackets(color="green", y_position=60)
        self.build_brackets(color="green", y_position=90)

    def orange_brackets(self):
        self.build_brackets(color="orange", y_position=120)
        self.build_brackets(color="orange", y_position=150)

    def red_brackets(self):
        self.build_brackets(color="red", y_position=180)
        self.build_brackets(color="red", y_position=210)


    def build_brackets(self, color, y_position): 
        # print(int(self.width_window/30))
        # window_width/pixels of bracket in integer format

        tick = 40
        for bracket in range(int(self.width_window/80)):
            bracket = Turtle(shape="square")
            # print(bracket.getturtle())
            LIST_OF_TURTLES.append(bracket.getturtle())

            bracket.hideturtle()
            bracket.speed("fastest")
            bracket.color(color)
            bracket.shapesize(0.5, 3, 1)
            bracket.penup()
            # bracket.goto(-1*self.width_window/2+tick, y_position)
            bracket.setpos(-1*self.width_window/2+tick, y_position)
            bracket.showturtle()
            tick += 80   

    def keyboard_left(self):
        if self.game_started == False:
            self.game_started = True
            
        # 70 pixels bracket size
        if self.xcor() > -1*self.width_window/2+30:
            self.goto(self.xcor()-30, self.ycor())
        self.screen.update()

    def keyboard_right(self):   
        if self.game_started == False:
            self.game_started = True

        if self.xcor() < self.width_window/2-30:
            self.goto(self.xcor()+30, self.ycor())
        self.screen.update()

    def ball_control(self):
        self.ball = Turtle(shape="circle")
        self.ball.shapesize(1,1,1)
        # self.ball.speed("fastest")
        self.ball.penup()
        self.ball.color("white")
        self.ball.setposition(0,-50)


    def move_ball(self):
        self.screen.update()

        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.setheading(self.ball.towards(new_x, new_y))

        self.ball.goto(new_x, new_y)


        

        



if __name__ == "__main__":
    breakout_game = Breakout()

# %%
