from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.shape("square")
        self.penup()
        self.color("green")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.goto(rand_x, rand_y)

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)

    def clear_screen(self):
        self.hideturtle()