# Create a snake body
from turtle import Turtle, Screen
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

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

is_game_on = True


while is_game_on:
    screen.update()
    time.sleep(0.1)
    for segment_num in range(len(segments)-1, 0, -1):
        x_position = segments[segment_num-1].xcor()
        y_position = segments[segment_num-1].ycor()
        segments[segment_num].goto(x_position, y_position)
    segments[0].forward(20)
    segments[0].left(90)





screen.exitonclick()