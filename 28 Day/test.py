import tkinter

window = tkinter.Tk()

limit = 10
score = 0

def update():
    global score
    score += 1
    ScoreL.configure(text=score)
    if score < limit:
        # schedule next update 1 second later
        window.after(1000, update)

ScoreL = tkinter.Label(window, text=score)
ScoreL.pack()

window.after(1000, update) # start the update 1 second later
window.mainloop()