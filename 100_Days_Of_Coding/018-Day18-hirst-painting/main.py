import colorgram
import turtle as tt
import random as rd

# change the colormode of the turtle module
tt.colormode(255)

# extract color from image
colors = colorgram.extract('image.jpg', 30)
color_list = []

# get each color from the extracted object
for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    color_list.append((r, b, g))

# remove the first two colors that probably extracted from the white color background
new_color = color_list[2:]

# create turtle object
tim = tt.Turtle()

# setting up our turtle
tim.shape('circle')
tim.speed('fastest')
tim.pensize(20)
tim.hideturtle()
tim.penup()

# start with lower-left position (-250, -200)

for j in range(10):
    y_position = -200 + 50 * j
    tim.goto(-250, y_position)

    for i in range(10):
        tim.dot(20, rd.choice(new_color))
        tim.forward(50)

screen = tt.Screen()
screen.exitonclick()
