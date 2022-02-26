from snakepast import Snake
from turtle import Screen
from generatorFood import FoodGenerator
from scoreboard import ScoreBoard
import random
import time

# creating the screen for the snake game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("pink")
screen.title("Snake Game")
screen.tracer(0)

# creating the snake body && calling the food generator && calling scoreboar
snake = Snake()
food = FoodGenerator()
scoreboard = ScoreBoard()

# modulizing the screen
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
# game in action
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    # checking snake vs food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.increase_size()

    # checking colision
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()

    # checking snake tails
    for piece in snake.snake_body[1:-1:1]:
        if snake.head.distance(piece) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
