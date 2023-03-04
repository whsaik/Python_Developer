from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time


# setting up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# building the middle line
middle_line = []
for i in range(12):
    middle_block = Turtle('square')
    middle_block.color('white')
    middle_block.shapesize(stretch_len=0.2)
    middle_block.penup()
    middle_block.goto((0, 280 - 50 * i))

# creating two paddles
paddleA = Paddle((-350, 0))
paddleB = Paddle((350, 0))

# creates the ball object
ball = Ball()

# creates scoreboard
scoreA = Score((-150, 200))
scoreB = Score((150, 200))

# game start
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the upper and lower boundary - bounce back
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with the paddles
    if ball.xcor() > 320 and ball.distance(paddleB) < 40 \
            or ball.xcor() < -320 and ball.distance(paddleA) < 40:
        ball.bounce_x()

    # detect ball missed
    if ball.xcor() > 380:
        scoreA.update_score()
        scoreA.display_score()
        ball.refresh()

    elif ball.xcor() < -380:
        scoreB.update_score()
        scoreB.display_score()
        ball.refresh()

    screen.listen()
    screen.onkey(paddleA.up, "w")
    screen.onkey(paddleA.down, "s")
    screen.onkey(paddleB.up, "Up")
    screen.onkey(paddleB.down, "Down")




screen.exitonclick()
