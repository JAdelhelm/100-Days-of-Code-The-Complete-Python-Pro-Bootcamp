# %%
from tkinter import *
from PIL import Image, ImageTk
import time
# ---------------------------- CONSTANTS ------------------------------- #
LILA = "#6A2C70"
RED = "#B83B5E"
ORANGE = "#F08A5D"
GREEN = "#17B978"
YELLOW = "#F9ED69"
FONT_NAME = "Courier"
WORK_MIN = 25
WORK_SECONDS = 59

SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIMER_ACTIVATED = None
sets = 1
timer = None

marks = ""
TIMER_ACTIVATED = FALSE
pop_window = True

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
      global marks
      global sets
      window.after_cancel(timer)
      sets = 1
      marks = ""
      canvas.itemconfig(timer_text, text=f"00:00")
      check_marks.config(text=marks)
      button_start["state"] = NORMAL
      


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():     
    button_start["state"] = DISABLED
    global sets
    global marks
    # print(sets)
    canvas_timer.itemconfig(break_text, text="Timer:")
    if sets < 4 and sets >= 0:
        break_time_mins = SHORT_BREAK_MIN
        count_down(WORK_MIN-1,WORK_SECONDS, break_time_mins-1)  
    elif sets == 4:
        break_time_mins = LONG_BREAK_MIN
        count_down(WORK_MIN-1,WORK_SECONDS, break_time_mins-1) 
        
    if sets == 5:marks = ""; sets = 1;check_marks.config(text=""); button_start["state"] = NORMAL; canvas_timer.itemconfig(break_text, text="Restart?")
    else:
        marks += "✅"
        check_marks.config(text=marks)
   
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(minutes,seconds, break_time_minutes):   
        global sets
        global timer
        global marks
        global pop_window
        if minutes != -1:
            if seconds > 9:
                canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
            else:
                canvas.itemconfig(timer_text, text=f"{minutes}:0{seconds}")
            if seconds == 0: seconds = 60; minutes -= 1
            timer = window.after(1000, count_down, minutes, seconds - 1, break_time_minutes)

        elif minutes <= -1: 
            if pop_window == True:
                window.wm_state('normal')
                window.attributes('-topmost', 1)
                window.attributes('-topmost', 0)
                pop_window = False
            canvas_timer.itemconfig(break_text, text="Break :)")
            if seconds > 9:
                canvas.itemconfig(timer_text, text=f"{break_time_minutes}:{seconds}")
            else:
                canvas.itemconfig(timer_text, text=f"{break_time_minutes}:0{seconds}")

            if seconds == 0: seconds = 60; break_time_minutes -= 1
            if break_time_minutes != -1:
                timer = window.after(1000, count_down,minutes, seconds -1, break_time_minutes)
            else:
                pop_window = True
                button_start["state"] = NORMAL   
                sets += 1 
            
           
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Timer Text Top
canvas_timer = Canvas(width=250,height=90, bg=YELLOW, highlightthickness=0)
## X / Y
break_text = canvas_timer.create_text(120,70,text="Timer:", fill=GREEN, font=(FONT_NAME, 35, "bold"))
canvas_timer.grid(row=1,column=2)

# Tomato + Timer
canvas = Canvas(width=200,height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100,115, image = tomato_img)
timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)


# Start Button
start_button_image = Image.open("./startbutton.png")
start_button_image = start_button_image.resize((round(80*1.5),round(30*1.5)))

start_img_resized = ImageTk.PhotoImage(start_button_image) # make sure to add "/" not "\"
button_start = Button(window, text="Start",fg=YELLOW, bg=YELLOW, command=start_timer,
                highlightthickness=0,border=0,highlightbackground=YELLOW, activebackground=YELLOW)
button_start.config(image=start_img_resized)
button_start.grid(row=3,column=1)

# Reset Button
reset_button_image = Image.open("./resetbutton.png")
reset_button_image = reset_button_image.resize((round(80*1.5),round(30*1.5)))

reset_img_resized = ImageTk.PhotoImage(reset_button_image) # make sure to add "/" not "\"
button_reset = Button(window, text="RESET",fg=YELLOW, bg=YELLOW, command=reset_timer,
                highlightthickness=0,border=0,highlightbackground=YELLOW, activebackground=YELLOW)
button_reset.config(image=reset_img_resized)
button_reset.grid(row=3,column=3)

# # Marks 

check_marks = Label(text="", bg=YELLOW,highlightthickness=0, fg=GREEN)
check_marks.grid(row = 3, column=2)



# marks_img = Image.open("./marks.png")
# marks_img_resized = marks_img.resize((round(30),round(30)))

# marks_img_resized = ImageTk.PhotoImage(marks_img_resized) # make sure to add "/" not "\"
# button = Button(window, text="RESET",fg=YELLOW, bg=YELLOW, 
#                 highlightthickness=0,border=0,highlightbackground=YELLOW, activebackground=YELLOW)
# button.config(image=marks_img_resized)
# button.grid(row=3,column=2)



window.mainloop()