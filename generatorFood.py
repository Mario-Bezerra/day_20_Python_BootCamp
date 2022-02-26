from turtle import Turtle
import random


class FoodGenerator(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_food = random.randint(-280, 280)
        y_food = random.randint(-280, 280)
        self.goto(x_food, y_food)
