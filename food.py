from turtle import Turtle, Screen
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.penup()
        self.refresh()
        
    def refresh(self):
        x_cord = random.randint(-280,280)
        y_cord = random.randint(-280,280)
        self.goto(x_cord,y_cord)
        