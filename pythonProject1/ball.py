import random as rd
from turtle import *
DIR = [45, 135, 225, 315]

class Ball:
    def __init__(self):
        self.obj =  Turtle("circle")
        self.obj.pu()
        self.obj.color("white")
        self.xcor = self.obj.xcor()
        self.ycor = self.obj.ycor()
        self.obj.goto((self.xcor, self.ycor))
        self.obj.setheading(rd.choice(DIR))

    def set_dir(self):
        self.obj.setheading(rd.choice(DIR))

    def move(self):
        self.obj.fd(10)
        print((self.obj.heading(),self.obj.xcor(), self.obj.ycor()))
#        print(self.obj.ycor())
#        print(self.obj.xcor())
