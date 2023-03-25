from snake import Snake
from turtle import Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


# create snake body
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

# to stop displaying things on the screen. It will again start to display when screen.update is called.
screen.tracer(0)

snake = Snake()

is_game_on = True


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()




screen.exitonclick()