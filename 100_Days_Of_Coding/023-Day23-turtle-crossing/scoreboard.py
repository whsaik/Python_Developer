from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.score = 1
        self.goto((-220,260))
        self.display_score()
        
    def display_score(self):
        self.clear()
        self.write(f"Level = {self.score}", move=False, align=ALIGNMENT, font=FONT)
        
    def update_score(self):
        self.score += 1
        
    def game_over(self):
        self.goto((0, 0))
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
