from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with the food; food size is 10 by 10; snake size is 20 by 20;so half of both to get center is 15.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()


screen.exitonclick()
