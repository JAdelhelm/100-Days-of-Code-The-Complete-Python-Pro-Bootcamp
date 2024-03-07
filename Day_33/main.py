#%%
from tkinter import *
import requests
import json

def get_quote():
    # try:
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    json_content = response.json()
    kanye_quote = json_content["quote"]

    canvas.itemconfig(quote_text, text=kanye_quote)
    # except requests.exceptions as e:
    #     print(e)




window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

quote_text = canvas.create_text(150, 207, text="Kanye says...", width=250, font=("Arial", 16, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()