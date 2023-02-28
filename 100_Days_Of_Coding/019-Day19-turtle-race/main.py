from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

# lists for the race
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_log = {}
items = ['bomb', 'boost', 'banana skin']

# determiner for the race loop
is_race_on = False

# ask for user guess
user_bet = screen.textinput(title='Make a bet', prompt='Which turtle will win the race? Enter a color: ')

# generate list of 6 turtles with different colors
for n in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[n])
    new_turtle.penup()  # to avoid line drawn during turtle moving
    new_turtle.goto(-230, (-125 + 50 * n))  # turtle line up at the same x-axis but different y-axis
    turtle_log[n] = {'turtle': new_turtle, 'factor': 1.0}

# after user have inserted the guess, the race can start
if user_bet:
    is_race_on = True


# define function for select items
def random_items():
    item = random.choice(items)
    user_item = screen.textinput(title='Use item', prompt=f'You got {item}, who you want to use on?'
                                                          f'{colors}: ')
    if item == 'bomb':
        turtle_index = colors.index(user_item)
        turtle_log[turtle_index]['factor'] = 0
    elif item == 'boost':
        turtle_index = colors.index(user_item)
        turtle_log[turtle_index]['factor'] = 2
    elif item == 'banana skin':
        turtle_index = colors.index(user_item)
        turtle_log[turtle_index]['factor'] = 0.5


while is_race_on:
    for k, v in turtle_log.items():
        screen.listen()
        screen.onkey(random_items, "space")
        # check whether any of the turtles reached the ending line
        if v['turtle'].xcor() > 230:
            winning_color = v['turtle'].pencolor()
            is_race_on = False  # since there is a winner, we can stop the race
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        v['turtle'].forward(int(random.randint(0, 10) * v['factor']))  # turtle moves with random movement


screen.exitonclick()
