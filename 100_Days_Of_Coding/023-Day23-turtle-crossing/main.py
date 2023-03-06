import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
level = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    cars.create_car()
    cars.move()
        
    for i in cars.all_cars:
        if i.xcor() < -350:
            cars.all_cars.remove(i)
        
        if i.distance(player) < 20:
            game_is_on = False
            level.game_over()
        
    if player.is_at_finish_line():
        level.update_score()
        level.display_score()
        cars.increment += 1
        cars.cars_clear()
        player.refresh()
        
        
    screen.listen()
    screen.onkey(player.move, "Up")
    
 
screen.exitonclick()
