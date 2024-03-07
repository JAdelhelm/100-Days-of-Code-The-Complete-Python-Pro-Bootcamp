from tkinter import *
import re
from random import randint, choice, sample
from tkinter import messagebox
import pyperclip
import json
WIDTH = 500
HEIGHT = 400

ALPHABET_BIG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_SMALL = "abcdefghijklmnopqrstuvwxyz"
NUMBERS = "0123456789"
SYMBOLS = "-*$-_"

if __name__ == "__main__":
    window = Tk()
    window.minsize(width=WIDTH,height=HEIGHT)
    window.config(background="#454545", padx=50, pady=20)
######################## SAVE PW    ########################
    def create_pw_email():
        if len(input_website.get()) != 0 and len(input_email_username.get()) != 0 and len(input_password.get()) != 0:
            pattern_check_mail = bool(re.search(r"^\S+@\S+\.\S+$", input_email_username.get()))
            pattern_check_username = bool(re.search(r"^[a-zA-Z0-9_.-]+$", input_email_username.get()))
            pattern_check_password = bool(re.search(r"[A-Za-z0-9@#$%^&+=]{8,}", input_password.get()))
            # print(pattern_check_mail,pattern_check_username,pattern_check_password)
            email = input_email_username.get()
            website = input_website.get()
            password = input_password.get()

            if (pattern_check_mail == True or pattern_check_username == True) and pattern_check_password == True:
            # Abspeichern der Daten in JSON
                new_data = {website: {
                    "email":email,
                    "password":password,
                }}
                try:
                    with open("passwords.json","r") as data_file:
                        # Aktuelle Daten einladen
                        load_dict = json.load(data_file)
                except FileNotFoundError:
                    with open("passwords.json","w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                        # Aktuelle Daten mit den neuen Werten aktualisieren
                        load_dict.update(new_data)

                        with open("passwords.json","w") as data_file:
                            # Alle Daten mitsamt den aktualisierten Daten in das JSON File schreiben.
                            json.dump(load_dict, data_file, indent=4)
                            data_file.close()
                finally:
                    messagebox.showinfo(title="Sucessful",message="Your password was successfully added :)")
                    pyperclip.copy(input_password.get())

                    input_email_username.delete(0,END)
                    input_password.delete(0, END)
                    input_website.delete(0,END)

        else:
            messagebox.showwarning(message="Please make sure you haven't left any fields empty.")

    def create_password():
        input_password.delete(0,END)
        generated_pw = ''.join(sample(ALPHABET_BIG, randint(3,6)))  + ''.join(sample(NUMBERS, randint(3,6)))  + \
        ''.join(sample(ALPHABET_SMALL, randint(2,4))) + ''.join(sample(SYMBOLS, randint(1,4)))
        input_password.insert(0,generated_pw)

    def find_data():
        website = input_website.get()
        with open("passwords.json","r") as f:
            get_data = json.load(f)
            f.close()
        
        get_email = get_data[website]["email"]
        get_password = get_data[website]["password"]
        
        input_email_username.delete(0,END)
        input_password.delete(0, END)

        input_email_username.insert(0, get_email)
        input_password.insert(0, get_password)


######################## UI - SETUP ########################
    canvas_bg = Canvas(width = WIDTH/2,height=HEIGHT/2, bg="#454545", highlightthickness=0)
    image_bg = PhotoImage(file="./logo.png")
    canvas_bg.create_image(WIDTH/4,HEIGHT/4,image=image_bg)
    canvas_bg.grid(row=0, column= 1)

# Textfelder - Keine Funktion
    text_website = Label(text="Website:",bg="#454545",justify="left", fg="white")
    text_website.grid(row=1, column=0, pady=5)

    text_email = Label(text="Email/Username:", bg="#454545", justify="left", fg="white")
    text_email.grid(row=2,column=0, pady=5)

    text_password = Label(text="Password:", bg="#454545", justify="left", fg="white")
    text_password.grid(row=3, column=0, pady=5)
# Inputfelder - Funktionen
    input_website = Entry(justify="left", width=round(WIDTH/13), borderwidth=5)
    input_website.grid(row=1,column=1,sticky=W, columnspan=1, pady=5)
    input_website.focus()

    button_search = Button(justify="left",width=18, text="Search", command=find_data)
    button_search.grid(row=1,column=2,columnspan=1)

    input_email_username = Entry(justify="left",width=round(WIDTH/8), borderwidth=5)
    input_email_username.grid(row=2, column=1, columnspan=2, pady=5)
    input_email_username.insert(0, "default@gmail.com")
    input_email_username.focus()


    input_password = Entry(justify="left",width=round(WIDTH/13), borderwidth=5)
    input_password.grid(row=3, column=1, sticky=W, pady=5)
    input_password.focus()

    button_generate = Button(text="Generate Password", justify="right", width=18, command=create_password)
    button_generate.grid(row=3, column=2, pady=5)

    add_button = Button(text="Add",width=54, command=create_pw_email)
    add_button.grid(row=4, column=1, columnspan=2, pady=5)



    window.mainloop()

# # Tomato + Timer
# canvas = Canvas(width=200,height=230, bg=YELLOW, highlightthickness=0)
# tomato_img = PhotoImage(file="./tomato.png")
# canvas.create_image(100,115, image = tomato_img)
# timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.grid(row=2, column=2)
