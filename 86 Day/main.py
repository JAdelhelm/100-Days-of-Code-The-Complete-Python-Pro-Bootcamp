#%%
from PIL import Image, ImageTk, ImageFont, ImageDraw
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from tkinter import font
import time

from random import randint

class SpeedTest(tk.Tk):
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

        self.typing_time_ended = False

        self.possible_words_to_show = open("./words_collection.txt").read().splitlines()
        self.current_word_showed = None
        # print(self.possible_words_to_show)

        self.counter_right_words = 0
        self.counter_wrong_words = 0

        self.right_character_counter = 0



        self.input_textfield()
        self.show_current_word()

        # Starts timer when typing has been started
        self.bind("<Key>", self.start_timer)
        self.timer_has_been_started = False

    def start_timer(self, event):
        if self.timer_has_been_started == False:
            self.timer_has_been_started = True
            self.timer()
    
    def timer(self):
        try: self.timer_text.destroy()
        except: pass

        highlightFont = font.Font(family='Helvetica', name='font_counter_1', size=14, weight='bold')
        self.timer_text = tk.Label(self, text=f"Time left: {self.timer_duration}", font=highlightFont)
        self.timer_text.place(relx=.75, rely=.1)

        if self.timer_duration <= 0:
            return self.time_ended()

        self.after(1000, self.decrease_timer)

    def decrease_timer(self):
        self.timer_duration -= 1
        self.timer()

    
    def time_ended(self):
        self.typing_time_ended = True

        self.inputWords.config(state="disabled")
        try: self.current_word.destroy()
        except: pass
        highlightFont = font.Font(family='Helvetica', name='current_word_highlight', size=16, weight='bold')

        # Normalization with division through 60
        words_per_minute = self.right_character_counter / (self.starting_time / 60)

        self.words_per_minute = self.right_character_counter


        # Show right words, wrong words, etc.
        self.current_word = tk.Label(self, text=f"Time has ended.\n\n You had {self.counter_right_words} words right and\n{self.counter_wrong_words} words wrong.\n\nWords per minute: {words_per_minute}", font=highlightFont)
        self.current_word.place(relx=.35, rely=.2)  
        # print(f"Time has ended.")
        


    def show_current_word(self):
        try: self.current_word.destroy(); 
        except: pass


        self.current_word_showed = self.possible_words_to_show[randint(0,len(self.possible_words_to_show)-1)]

        highlightFont = font.Font(family='Helvetica', name='current_word_highlight', size=24, weight='bold')

        self.current_word = tk.Label(self, text=self.current_word_showed, font=highlightFont)
        self.current_word.place(relx=.4, rely=.5)    



    def input_textfield(self):
        try: self.inputWords.destroy();  
        except: pass

        self.inputWords = tk.Text(self, width=20, height=1)
        self.inputWords.place(relx=.4, rely=.8)
        
        self.inputWords.bind('<Return>', self.enter_pressed)


    def enter_pressed(self, event):
        # print(self.inputWords.get("1.0",tk.END).replace("\n",""))
        if self.typing_time_ended != True:


            if self.inputWords.get("1.0","end-1c").replace("\n","") == self.current_word_showed: self.counter_right_words += 1; self.right_character_counter += 1
            else: self.counter_wrong_words += 1

            self.inputWords.delete('0.0', tk.END)
            

            self.show_current_word()

            # print("Enter has been pressed.")


if __name__ == "__main__":
    app = SpeedTest(title="SpeedTest", size=(800,250), timer_duration=10)
    app.mainloop()
