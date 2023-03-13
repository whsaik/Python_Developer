from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKER = ""
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1
timer_w = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_count():
    global CHECKER, REPS
    window.after_cancel(timer_w)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    CHECKER = ""
    REPS = 1
    checker_label.config(text=CHECKER)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global REPS
    if REPS % 2 != 0:
        title_label.config(text="WORK", fg=GREEN)
        countdown(WORK_MIN * 60)
    else:
        if REPS % 8 == 0:
            title_label.config(text="BREAK", fg=RED)
            countdown(LONG_BREAK_MIN * 60)
        else:
            title_label.config(text="BREAK", fg=PINK)
            countdown(SHORT_BREAK_MIN * 60)
    
    REPS += 1
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(t):
    global CHECKER, timer_w
    mins, secs = divmod(t, 60)
    count_timer = '{:02d}:{:02d}'.format(mins, secs)
    canvas.itemconfig(timer_text, text=count_timer)
    if t >= 0:
        timer_w = window.after(1000, countdown, t - 1)
    else:
        if REPS % 2 == 0:
            CHECKER += "✓"
            checker_label.config(text=CHECKER)
        start_count()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

# create canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./256 - pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# creates labels
title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg= YELLOW)
title_label.grid(column=1, row=0)

checker_label = Label(text=CHECKER, font=(FONT_NAME, 10, "bold"), fg=GREEN, bg= YELLOW)
checker_label.grid(column=1, row=3)
    
start_button = Button(text="Start", highlightthickness=0, command=start_count)
start_button.grid(column=0, row=2)
start_button.config(padx=5, pady=5)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_count)
reset_button.grid(column=2, row=2)
reset_button.config(padx=5, pady=5)

window.mainloop()