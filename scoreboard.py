from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 300)
        self.write(f"Score: {self.score}", align='center', font=("Verdana", 12, "normal"))
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align='center', font=("Verdana", 12, "normal"))
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align='center', font=("Verdana", 15, "normal"))

