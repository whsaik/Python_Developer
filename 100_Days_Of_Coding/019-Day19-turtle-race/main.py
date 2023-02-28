from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

# determiner for the race loop 
is_race_on = False

# ask for user guess 
user_bet = screen.textinput(title='Make a bet', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_list = []

# generate list of 6 turtles with different colors
for n in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[n])
    new_turtle.penup()  # to avoid line drawn during turtle moving
    new_turtle.goto(-230, (-125 + 50 * n))  # turtle line up at the same x-axis but different y-axis
    turtle_list.append(new_turtle)  # after creating new turtle store them in a list

# after user have inserted the guess, the race can start
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        # check whether any of the turtles reached the ending line
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False  # since there is a winner, we can stop the race
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        turtle.forward(random.randint(0, 10))  # turtle moves with random movement


screen.exitonclick()
