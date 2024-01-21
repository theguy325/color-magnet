from turtle import Turtle

class Wall(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-290, 290)
        self.draw_wall()
    def draw_wall(self):
        self.pendown()
        i = 4
        while i > 0:
            self.forward(580)
            self.right(90)
            i -= 1
