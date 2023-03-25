from turtle import Turtle
import random
# Food class inherit from Turtle class


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        x_position = random.randint(-280, 280)
        y_position = random.randint(-280, 280)
        self.goto(x_position, y_position)

