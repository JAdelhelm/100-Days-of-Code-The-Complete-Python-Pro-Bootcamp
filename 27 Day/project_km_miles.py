from tkinter import *
KILOMETERS = 0
WIDTH = 300
HEIGHT = 300


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=WIDTH,height=HEIGHT)
window.config(padx=round(WIDTH/2),pady=round(HEIGHT/2))
# my_label = Label(text="test")
# my_label.grid(column=0,row=0)

input_box_miles = Entry()
input_box_miles.grid(column=1,row=0)
input_box_miles.config(width=10)

input_box_label = Label(text="Miles",font=("Arial",12))
input_box_label.config(padx=10)
input_box_label.grid(column=2, row = 0)

def calculate_km():
    try:
        miles_calculated = round(1.609*int(input_box_miles.get()))
        km_result.config(text=miles_calculated)
    except:
        print("Calculation failed")


is_equal = Label(text="is equal to",font=("Arial",12))
is_equal.grid(column=0,row=1)

km_result = Label(text=str(KILOMETERS),font=("Arial",12,"bold"))
km_result.grid(column=1,row=1)

km_label = Label(text="Km",font=("Arial",12))
km_label.grid(column=2,row=1)

button_to_calculate = Button(text="Calculate", command=calculate_km)
button_to_calculate.grid(column=1,row=2)

mainloop()