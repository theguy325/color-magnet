from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.listen()
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
game_on = True

screen.onkey(key='Left', fun=snake.turn_left)
screen.onkey(key='Down', fun=snake.turn_down)
screen.onkey(key='Right', fun=snake.turn_right)
screen.onkey(key='Up', fun=snake.turn_up)
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()










screen.exitonclick()