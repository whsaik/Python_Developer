from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        """Building a snake with 3 squares long"""
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake_block = Turtle(shape='square')
        snake_block.color('white')
        snake_block.penup()
        snake_block.goto(position)
        self.snake_body.append(snake_block)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        """Movement of the whole snake"""
        for seg in range(len(self.snake_body) - 1, 0, -1):
            x_new = self.snake_body[seg - 1].xcor()
            y_new = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(x_new, y_new)

        # head of the snake will move forward
        self.head.forward(MOVE_DISTANCE)

    def reset_game(self):
        for seg in self.snake_body:
            seg.hideturtle()
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
        
    
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
