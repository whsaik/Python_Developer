from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 50, "normal")

class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(self.score, move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', move=False, align=ALIGNMENT, font=FONT)