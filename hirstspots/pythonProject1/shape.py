from turtle import *
import random

bob = Turtle()
screen = Screen()
bob.shape("turtle")
bob.pencolor("blue2")


class Shape:
    def __init__(self, paces, angle, no_of_sides, colors):
        self.paces = paces
        self.angle = angle
        self.no_of_sides = no_of_sides
        self.colors = colors


    def set_colour(self):
        screen.colormode(255)
        colour = []
        for i in range(3):
            colour.append(random.randrange(0, 255))
        return colour


    def move_shape(self):
        bob.pencolor(self.set_colour())
        for i in range(self.no_of_sides):
            bob.fd(self.paces), bob.rt(self.angle)


    def move_rand(self):
        bob.width(10)
        bob.speed(0)

        nums = [1, 2]

        while True:

            bob.pencolor(self.set_colour())
            elem = random.choice(nums)
            elem2 = random.choice(nums)

            if elem2 == 1:
                bob.fd(self.paces)

            elif elem2 == 2:
                bob.bk(self.paces)

            if elem == 1:
                bob.rt(90)

            elif elem == 2:
                bob.lt(90)


    def move_rand_two(self):
        bob.width(15)
        bob.speed(0)
        nums = [0, 90, 100, 270]

        for i in range(50):
            bob.pencolor(self.set_colour())
            bob.fd(self.paces)
            bob.setheading(random.choice(nums))


    def spirograph(self):
        bob.speed(0)
        while True:
            bob.pencolor(self.set_colour())
            bob.circle(100)
            bob.lt(5)

            if bob.heading() == 355:
                break


    def draw_dots(self):
        x = -200
        y = -200
        screen.colormode(255)

        for j in range(10):
            bob.pu()
            bob.setpos(x, y)
            bob.pd()
            for i in range(10):
                color = random.choice(self.colors)
                bob.dot(20, list(color))
                bob.pu()
                bob.fd(50)
                bob.pd()

            x = -200
            y += 50

        bob.pu()
        bob.circle(-100)
        bob.hideturtle()





