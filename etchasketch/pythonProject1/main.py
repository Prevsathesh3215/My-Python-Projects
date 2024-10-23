import turtle
from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()


def move_fd():
    bob.fd(10)


def move_bd():
    bob.bk(10)


def turn_right():
    bob.rt(10)

def turn_left():
    bob.lt(10)

def clear_and_reset():
    bob.reset()

def circle_ccw():
    bob.circle(30)

def circle_cw():
    bob.circle(-30)

screen.listen()


screen.onkey(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_bd)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_and_reset)
screen.onkey(key="f", fun=circle_ccw)
screen.onkey(key="z", fun=circle_cw)

turtle.mainloop()
screen.exitonclick()