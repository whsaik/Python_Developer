import turtle as tt
import random

tt.colormode(255)
tim = tt.Turtle()
tim.shape("circle")
tim.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

Challenge 2: Random walk with random color
tim.shapesize(0.5, 0.5, 0.5)
tim.pensize(10)

def random_walk(n):
    while n > 0:
        direction = random.randint(0, 3) * 90
        tim.color(random_color())
        tim.setheading(direction)
        tim.forward(20)
        n -= 1


random_walk(100)
