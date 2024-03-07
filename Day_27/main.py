from tkinter import *

window = Tk()

window.title("My First GUI Program")

window.minsize(width=500, height=300)

# Label 

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.place(x=0,y=0)
# my_label.pack()
my_label.grid(column=0,row=0)

# my_label["text"] = "New Text"
# my_label.config(text = "New Text")


def button_clicked():
    # my_label["text"] = "Changed Text"
    callback = input.get()
    my_label.config(text=callback)

button = Button(text="Click me", command=button_clicked)
# button.place(x=0, y=50)
button.grid(column=0, row = 1)


# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=1,row=1)





# import turtle

# tim = turtle.Turtle()
# tim.write()


window.mainloop()
