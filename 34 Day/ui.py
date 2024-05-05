#%%
from tkinter import *
from PIL import Image, ImageTk

from quiz_brain import QuizBrain

import time

THEME_COLOR = "#375362"
# QUESTION_COLOR = 

ACTUAL_SCORE = 0
QUESTION = ""

class QuizzInterface():
    
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.window.minsize()

        self.create_score_text()

        self.canvas = Canvas(width=300, height=250, bg="white")
        
        # Die 150 und 125 sagt aus, wo das Element platziert werden soll.
        # Hier ist es genau in der Mitte
        self.question_text = self.canvas.create_text(150,125,width=280, text="Questions?", fill=THEME_COLOR, font=("Arial",14,"italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.create_buttons()

        self.get_next_question()
        self.score_text.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number-1}")
        
        self.window.mainloop()


    def create_score_text(self):
        self.score_text = Label(self.window,highlightthickness=0, border=0, height=2, width=20, bg=THEME_COLOR,fg="white", text=f"Score: {self.quiz.score}/{self.quiz.question_number-1}")
        self.score_text.grid(row=0, column=1)


    def create_buttons(self):
        self.true_image = PhotoImage(file="./images/true.png")
        self.false_image = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=self.true_image, highlightthickness=0,border=0, command=self.true_pressed)
        self.false_button = Button(image=self.false_image, highlightthickness=0,border=0, command=self.false_pressed)

        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)


    def true_pressed(self):
        self.check_answer = self.quiz.check_answer(user_answer="True")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.give_feedback(self.check_answer)
    
    def false_pressed(self):
        self.check_answer = self.quiz.check_answer(user_answer="False")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.give_feedback(self.check_answer)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

            self.score_text.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number-1}")

            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
        else:
            self.score_text.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)



# QuizzInterface()
# %%
