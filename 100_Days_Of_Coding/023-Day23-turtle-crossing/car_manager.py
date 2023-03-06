from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
END_LINE = -300


class CarManager():
    
    def __init__(self):
        self.all_cars = []
        self.increment = 0
        
    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=random.randint(1,2), stretch_wid=1)
            new_car.setheading(180)
            new_car.goto(300, random.randint(-220, 220))
            self.all_cars.append(new_car)
        
    def move(self):
        speed = STARTING_MOVE_DISTANCE + self.increment * MOVE_INCREMENT
        for car in self.all_cars:
            car.forward(speed)
            
    def cars_clear(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars = []
        
    