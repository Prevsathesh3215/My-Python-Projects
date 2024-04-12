POS_ONE = (-300, 0)
from turtle import *

class Paddle:

    def __init__(self, x_cor, y_cor):
        self.paddle_obj = Turtle(shape= "square")
        self.paddle_obj.shapesize(stretch_len=8)
        self.paddle_obj.pu()
        self.paddle_obj.color("white")
        self.paddle_obj.goto((x_cor, y_cor))
        self.paddle_obj.setheading(90)

    def up(self):
        self.paddle_obj.setheading(90)
        self.paddle_obj.fd(10)
        print(self.paddle_obj.xcor())

    def down(self):
        self.paddle_obj.setheading(270)
        self.paddle_obj.fd(10)