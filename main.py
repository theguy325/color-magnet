from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
from wall import Wall

screen = Screen()
screen.bgcolor('black')
screen.setup(width=650, height=650)
screen.listen()
screen.title("The Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
wall = Wall()
game_on = True

screen.onkey(key='Left', fun=snake.turn_left)
screen.onkey(key='Down', fun=snake.turn_down)
screen.onkey(key='Right', fun=snake.turn_right)
screen.onkey(key='Up', fun=snake.turn_up)
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    # collision with the wall
    cur_x = snake.head.xcor()
    cur_y = snake.head.ycor()
    if cur_x > 285 or cur_y > 285 or cur_x < -285 or cur_y < -285:
        score.game_over()
        game_on = False

    # collision with tail
    if snake.tail_collision():
        score.game_over()
        game_on = False


    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score += 1
        score.update_score()


screen.exitonclick()
