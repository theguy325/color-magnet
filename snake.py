from turtle import Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in POSITION:
            new_segment = Turtle()
            new_segment.penup()
            new_segment.shape('square')
            new_segment.color('white')
            new_segment.goto(pos)
            self.segments.append(new_segment)
    def snake_move(self):
        for each in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[each - 1].xcor()
            new_y = self.segments[each - 1].ycor()
            self.segments[each].goto(new_x, new_y)
        self.head.forward(20)


    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def tail_collision(self):

        for each in range(len(self.segments) - 1, 0, -1):
            if self.segments[each].distance(self.head) < 5:
                return True






