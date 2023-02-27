# Challenge 3: Draw a Spirograph
import turtle as tt
import random

tt.colormode(255)
tim = tt.Turtle()
tim.shape("circle")
tim.speed('fastest')
tim.shapesize(0.1, 0.1, 0.1)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def spirograph(space, size):
    for i in range(360//space + 1):
        tim.color(random_color())
        tim.circle(size)
        tim.left(space)

        
spirograph(5, 100)

screen = tt.Screen()
screen.exitonclick()
