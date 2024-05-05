BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import json
from random import randint
import pandas as pd

seconds = 5
DF_LANGUAGE = pd.read_csv("./data/EnglishGermanTop5000_fixed.csv")

rand_german = ""
rand_english = ""
random_index = randint(0,4999)
if __name__ == "__main__":

    def get_random_word():
        global rand_german
        global rand_english
        global random_index        
        try:
            # Checken, ob der Index schon im Json File ist
            with open("right_answers.json","r") as data_file:
                dict_words = json.load(data_file)
                data_file.close()
            
            index_list = []
            for index in dict_words.keys():
                index_list.append(index)

            if len(index_list) < 5000:
                while str(random_index) in index_list:
                    random_index = randint(0,4999)
                    # print(random_index)
            else:
                print("Congratulations! You have learned every word!")


        except Exception as msg:
            pass

        rand_german = DF_LANGUAGE["German"][random_index]
        rand_english = DF_LANGUAGE["English"][random_index]

        return rand_german, rand_english

    #  Wenn richtig, dann mit json überprüfen
    def start_timer_flip_right():
        global seconds
        global rand_german
        global rand_english
        global random_index
        try:
            right_answer = {
                random_index: {
                "English":rand_english,
                "German":rand_german
                }
                }
            
            # Einlesen der aktuellen Daten
            with open("right_answers.json","r") as data_file:
                right_dict = json.load(data_file)
                data_file.close()

            if str(random_index) not in right_dict.keys():
                with open("right_answers.json","w") as f:
                    right_dict.update(right_answer)
                    json.dump(right_dict, f, indent=4)
                    f.close()
        except Exception as msg:
            print("Creating new file.")
            with open("right_answers.json","w") as f:
                json.dump(right_answer,f, indent=4)
                f.close()

        get_random_word()
        language_canvas.itemconfigure(card_back, state="normal")
        language_canvas.itemconfigure(language_setting, text="English")
        language_canvas.itemconfigure(shown_word, text=rand_english)
        card_to_background(seconds=seconds)

    def start_timer_flip_wrong():
        global seconds
        global rand_german
        global rand_english
        global random_index
        random_index = randint(0,4999)
        get_random_word()
        language_canvas.itemconfigure(card_back, state="normal")
        language_canvas.itemconfigure(language_setting, text="English")
        language_canvas.itemconfigure(shown_word, text=rand_english)
        card_to_background(seconds=seconds)

    def card_to_background(seconds):
        global rand_german
        global rand_english
        if seconds >= 0:
            window.after(1000,card_to_background, seconds-1)
        else:
            language_canvas.itemconfigure(language_setting, text="German")
            language_canvas.itemconfigure(shown_word, text=rand_german)
            language_canvas.itemconfigure(card_back, state="hidden")



    # USER INTERFACE
    window = Tk(screenName="Flashy - FlashCard")
    window.title("Flashy - FlashCard")
    window.minsize(width=820,height=540)
    window.config(background=BACKGROUND_COLOR, padx=50, pady=50, highlightthickness=0)

    card_back_img = PhotoImage(file="./images/card_back.png")
    card_front_img = PhotoImage(file="./images/card_front.png")
    right_img = PhotoImage(file="./images/right.png")
    wrong_img = PhotoImage(file="./images/wrong.png")


    # CANVAS - MIDFIELD
    language_canvas = Canvas(width=820,height=540,bg=BACKGROUND_COLOR, highlightthickness=0)
    # Card Front
    card_front = language_canvas.create_image((800/2,526/2), image=card_front_img)
    # Card Back
    card_back = language_canvas.create_image((800/2,526/2), image=card_back_img)

    # Language  
    language_setting = language_canvas.create_text((400,150),text="English", font=("Arial",25,"italic"))
    shown_word = language_canvas.create_text((400,263), text=rand_english, font=("Arial",45,"bold"))

    language_canvas.grid(row=1, column=2, columnspan=2)


    start_timer_flip_wrong()
    # BUTTONS - RIGHT/WRONG
    right_button = Button(image=right_img, highlightthickness=0, 
                          highlightbackground=BACKGROUND_COLOR, fg=BACKGROUND_COLOR, command=start_timer_flip_right)
    right_button.grid(row=2,column=3)

    wrong_button = Button(image=wrong_img, highlightthickness=0, 
                          highlightbackground=BACKGROUND_COLOR, fg=BACKGROUND_COLOR, command=start_timer_flip_wrong)
    wrong_button.grid(row=2,column=2)

   
    











    window.mainloop()



    
