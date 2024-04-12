from turtle import *
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_squares = []
        self.head = Turtle()
        self.create_snake()

    def create_snake(self):

        for pos in STARTING_POS:
            snake_block = Turtle(shape="square")
            snake_block.pu()
            snake_block.color("white")
            snake_block.goto(pos)
            self.snake_squares.append(snake_block)

        self.head = self.snake_squares[0]


    def move(self):
        for i in range(len(self.snake_squares) - 1, 0, -1):
            next_seg = self.snake_squares[i - 1].pos()
            self.snake_squares[i].goto(next_seg)

        self.head.fd(MOVE_DISTANCE)

    def add_seg(self):
        snake_block = Turtle(shape="square")
        snake_block.pu()
        snake_block.color("white")
        snake_block.goto(self.snake_squares[len(self.snake_squares) - 1].pos())
        self.snake_squares.append(snake_block)

    def reset(self):
        for obj in self.snake_squares:
            obj.hideturtle()

        self.snake_squares.clear()
        self.create_snake()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
