from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 275)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f'Score = {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', move=False, align=ALIGNMENT, font=FONT)
