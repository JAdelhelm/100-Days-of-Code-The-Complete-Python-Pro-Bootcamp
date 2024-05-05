"""
Disappearing Text Writing App

You are going to build a desktop app that has similar functionality. 
The design is up to you, but it should allow a user to type and if they stop for more than 5 seconds, it should delete everything they've written so far.
"""

#%%
from PIL import Image, ImageTk, ImageFont, ImageDraw
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from tkinter import font
import time

from random import randint

class DisappearingTextWritingApp(tk.Tk):
    """
    A Tkinter GUI desktop application that tests your typing speed.
    """
    def __init__(self, title, size, timer_duration) -> None:
        super().__init__()
        self.title(title)
        
        self.minsize(width=size[0], height=size[1])
        # geometry sets the size of the window
        self.geometry(f"{size[0]}x{size[1]}")
        # self.geometry(f"1400x1200")

        self.starting_time = timer_duration
        self.timer_duration = timer_duration

        self.words_collection = open("./words_collection.txt").read().splitlines()

        self.typing_time_ended = False

        self.label_advice()
        self.input_textfield()

        self.bind("<Key>", self.start_timer)
        self.timer_has_been_started = False


    def start_timer(self, event):
        if self.timer_has_been_started == False:
            self.timer_has_been_started = True
            self.timer()

    def reset_timer_duration(self, event):
        self.timer_duration = self.starting_time+1
    
    def timer(self):
        try: self.timer_text.destroy()
        except: pass

        highlightFont_timer = font.Font(family='Helvetica', name='font_counter_1', size=10)
        self.timer_text = tk.Label(self, text=f"Time left: {self.timer_duration}", font=highlightFont_timer)
        self.timer_text.place(relx=.85, rely=.85)

        self.bind("<Key>", self.reset_timer_duration)


        if self.timer_duration <= 0:
            return self.time_ended()

        self.after(1000, self.decrease_timer)

    def decrease_timer(self):
        self.timer_duration -= 1
        self.timer()

    
    def time_ended(self):
        self.typing_time_ended = True

        self.input_textfield()

        self.inputWords.config(state="disabled")


    def input_textfield(self):
        try: self.inputWords.destroy();  
        except: pass

        self.inputWords = tk.Text(self, width=60, height=15)
        self.inputWords.place(relx=.2, rely=.3)


    def label_advice(self):
        try: self.label_help.destroy()
        except: pass
        highlightFont = font.Font(family='Helvetica', name='font_label_advice', size=14, weight='bold')

        self.label_help = tk.Label(self, text="If you stop writing, your work will disappear after 5 seconds.", font=highlightFont)
        self.label_help.place(relx=.2, rely=.1)


    def enter_pressed(self, event):
        # print(self.inputWords.get("1.0",tk.END).replace("\n",""))
        if self.typing_time_ended != True:


            if self.inputWords.get("1.0","end-1c").replace("\n","") == self.current_word_showed: self.counter_right_words += 1; self.right_character_counter += 1
            else: self.counter_wrong_words += 1

            self.inputWords.delete('0.0', tk.END)
            

            self.show_current_word()

            # print("Enter has been pressed.")


if __name__ == "__main__":
    app = DisappearingTextWritingApp(title="DisappearingTextWritingApp", size=(800,400), timer_duration=5)
    app.mainloop()
