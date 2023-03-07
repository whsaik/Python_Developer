from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 15, "normal")

    
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 275)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f'Score = {self.score}   High Score = {self.high_score}', move=False, \
            align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.display_score()
