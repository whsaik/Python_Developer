from turtle import Turtle

MOVE_DISTANCE = 50

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.speed('fastest')
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)


    def up(self):
        self.goto((self.xcor(), self.ycor() + MOVE_DISTANCE))

    def down(self):
        self.goto((self.xcor(), self.ycor() - MOVE_DISTANCE))