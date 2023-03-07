from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# set up the screen of the game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)  # turn off the tracer
screen.title('My Snake Game')

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True


# control the movement of the snake
while game_is_on:
    screen.update()  # turn on the tracer for once to show the current state of the snake
    time.sleep(0.1)  # delay for 0.1s, control the speed of snake movement

    # user can turn the direction of snake
    screen.listen()
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")

    snake.move()

    # Detect the collision with food and relocate the food
    if snake.head.distance(food) < 15:
        scoreboard.update_score()
        scoreboard.display_score()
        food.refresh()

        # Snake get longer every 2 foods being eaten
        if scoreboard.score % 2 == 0:
            snake.extend()

    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
        snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset_game()
        scoreboard.reset_game()

    # Detect collision with the tail
    for seg in snake.snake_body[1:]:
        if snake.head.distance(seg) < 10:
            snake.reset_game()
            scoreboard.reset_game()











screen.exitonclick()
