from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
TEXT_COLOR = ('black', 'white')
WORD_LIST = []
CARD_INDEX = 1

#-------------------------------- Languages Data --------------------------------#
try:
    data = pd.read_csv("data/new_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    data_list = data.to_dict('records')

def rand_word():
    global WORD, WORD_LIST, CARD_INDEX, flip_timer
    CARD_INDEX = 1
    
    window.after_cancel(flip_timer)
    
    WORD = random.choice(data_list)
    WORD_LIST = [(l, w) for (l, w) in WORD.items()]
    canvas_main.itemconfig(canvas_lang_text, text=WORD_LIST[0][0], fill=TEXT_COLOR[0])
    canvas_main.itemconfig(canvas_word_text, text=WORD_LIST[0][1], fill=TEXT_COLOR[0])
    canvas_main.itemconfig(canvas_img, image=CARD_DISPLAY[0])
    CARD_INDEX *= -1
    
    flip_timer = window.after(3000, func=flip)
    
def flip():
    global CARD_INDEX
    if CARD_INDEX < 0: n = 1
    else: n = 0

    canvas_main.itemconfig(canvas_lang_text, text=WORD_LIST[n][0], fill=TEXT_COLOR[n])
    canvas_main.itemconfig(canvas_word_text, text=WORD_LIST[n][1], fill=TEXT_COLOR[n])
    canvas_main.itemconfig(canvas_img, image=CARD_DISPLAY[n])
    
    CARD_INDEX *= -1
    
def correct():
    global data_list
    data_list.remove(WORD)
    new_data = pd.DataFrame(data_list)
    new_data.to_csv("data/new_learn.csv", index=False)
    rand_word()
    
#-------------------------------- Saving Progress --------------------------------#

    
#-------------------------------- UI Design --------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)

WRONG_IMG = PhotoImage(file="./images/wrong.png")
RIGHT_IMG = PhotoImage(file="./images/right.png")
CARD_BACK = PhotoImage(file="./images/card_back.png")
CARD_FRONT = PhotoImage(file="./images/card_front.png")
CARD_DISPLAY = (CARD_FRONT, CARD_BACK)

# create canvas
canvas_main = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# add image to canvas
canvas_img = canvas_main.create_image(400, 263, image=CARD_FRONT)
# add text to canvas
canvas_lang_text = canvas_main.create_text(400, 150, text="", font=("Arial", 40, "italic"))
canvas_word_text = canvas_main.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas_main.grid(column=0, row=0, columnspan=3)

# create buttons
right_button = Button(image=RIGHT_IMG, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, \
    command=correct)
right_button.grid(column=2, row=1)

wrong_button = Button(image=WRONG_IMG, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, \
    command=rand_word)
wrong_button.grid(column=0, row=1)

flip_button = Button(text="Flip",highlightthickness=0, borderwidth=0, command=flip)
flip_button.grid(column=1, row=1)

rand_word()




window.mainloop()