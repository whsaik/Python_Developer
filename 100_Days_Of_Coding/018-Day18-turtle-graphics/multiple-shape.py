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
  
# Challenge 1: Draw the shape from triangle up to desired sided polygon
def draw_shape(sides):
    '''
    Function that takes the maximum number of sides needed and start drawing the shapes from Triangle
    up until the shape with number of sides inserted.
    '''
    for i in range(3, sides+1):
        d = 360 / i
        tim.color(random_color())
        while i > 0:
            tim.forward(100)
            tim.right(d)
            i -= 1


draw_shape(10)
