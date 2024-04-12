
from snake import *
import time
from food import *
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
s_board = scoreboard.Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    # Create a scoreboard
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_seg()
        s_board.add_one()

    # Detect collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or \
            snake.head.ycor() < -280 or snake.head.ycor() > 300:
        s_board.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.snake_squares[1:len(snake.snake_squares)]:
        if snake.head.distance(segment) < 10:
            s_board.reset()
            snake.reset()


screen.exitonclick()
