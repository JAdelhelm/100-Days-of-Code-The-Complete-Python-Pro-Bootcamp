import turtle 
import pandas as pd
import text_turtle
CURRENT_SCORE = 0
correct_answer_list = []

while len(correct_answer_list) < 50:
    screen = turtle.Screen()
    screen.title("U.S. States Game")

    

    img = "blank_states_img.gif"
    screen.addshape(img)

    turtle.shape(img)

    answer_state = screen.textinput(title=f"Guess the State - {CURRENT_SCORE} / 50 Correct", prompt="What's another state's name?").lower()
    print(answer_state)




    df_states = pd.read_csv("50_states.csv")
    df_states["state"] = [state.lower() for state in df_states["state"]]


    if answer_state not in correct_answer_list and answer_state in list(df_states["state"]):
        """CORRECT ANSWER"""
        correct_answer_list.append(answer_state)

        correct_state = df_states[df_states.state == answer_state]
        x_cor = int(correct_state["x"])
        y_cor = int(correct_state["y"])
        # print(correct_state)
        try:
            write_state = text_turtle.TextTurtle(text_state=answer_state.title(), x_cor=x_cor, y_cor=y_cor)
            CURRENT_SCORE += 1
            screen.update()
        except:
            pass
    else:
        print("FALSE")


    def get_mouse_click_coor(x,y):
        print(x,y)

    turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

