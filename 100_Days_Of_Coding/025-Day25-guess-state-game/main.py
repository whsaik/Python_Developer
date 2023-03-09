import turtle
import pandas as pd

ALIGN = 'center'

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

data = pd.read_csv("50_states.csv")

turtle.shape(image)

pointer = turtle.Turtle()
pointer.hideturtle()
pointer.penup()
pointer.color('black')

guessed_states = []

states_list = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 correct state", \
        prompt="What's another state name?").title()

    if answer_state == "Exit":
        for guess in guessed_states:
            states_list.remove(guess)
        missed_guess = pd.DataFrame(states_list)
        missed_guess.to_csv("Missed guess.csv")
        break
    
    if answer_state in states_list:
        x_loc = int(data[data.state == answer_state]['x'])
        y_loc = int(data[data.state == answer_state]['y'])
        pointer.goto((x_loc, y_loc))
        pointer.write(answer_state, align=ALIGN)
        
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
