from tkinter import *
import re
from random import randint, choice, sample
from tkinter import messagebox
import pyperclip
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
            if (pattern_check_mail == True or pattern_check_username == True) and pattern_check_password == True:
                with open("./passwords.txt","a") as file:
                    file.write(f"{input_website.get()} | {input_email_username.get()} | {input_password.get()}\n")
                    file.close()
                messagebox.showinfo(title="Sucessful",message="Your password was successfully added :)")
                pyperclip.copy(input_password.get())
            else:
                is_ok = messagebox.askyesno(title="Security check",
                                message=f"""Your password doesnt match the security criteria.\nHowever, do you want to add it anyway?\n\n\
Your Website:      {input_website.get()}\n\
Your Username:   {input_email_username.get()}\n\
Your Password:   {input_password.get()}""")
                if is_ok == True:
                    with open("./passwords.txt","a") as file:
                        file.write(f"{input_website.get()} | {input_email_username.get()} | {input_password.get()}\n")
                        file.close()
                    pyperclip.copy(input_password.get())
                # print("Please enter a valid password")
                # messagebox.showinfo(title="ERROR", message="Please enter a valid password.")
        else:
            messagebox.showwarning(message="Please make sure you haven't left any fields empty.")

    def create_password():
        input_password.delete(0,END)
        generated_pw = ''.join(sample(ALPHABET_BIG, randint(3,6)))  + ''.join(sample(NUMBERS, randint(3,6)))  + \
        ''.join(sample(ALPHABET_SMALL, randint(2,4))) + ''.join(sample(SYMBOLS, randint(1,4)))
        input_password.insert(0,generated_pw)


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
    input_website = Entry(justify="left", width=round(WIDTH/8), borderwidth=5)
    input_website.grid(row=1,column=1, columnspan=2, pady=5)
    input_website.focus()

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
