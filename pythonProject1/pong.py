
import time
from paddles import *
from ball import *
from scoreboard import *

screen = Screen()
screen.setup(width= 800, height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
screen.listen()

paddle1 = Paddle(x_cor=-300, y_cor=0)
paddle2 = Paddle(x_cor=300, y_cor=0)
s_board_one = Scoreboard(-200, 230, 1)
s_board_two = Scoreboard(200, 230, 2)

screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

ball = Ball()
game_on = True

while game_on:
    screen.update()
    time.sleep(0.05)

    ball.move()

    if ball.obj.ycor() > 270:
        if ball.obj.heading() == 135:
            ball.obj.setheading(ball.obj.heading() + 90)

        elif ball.obj.heading() == 45:
            ball.obj.setheading(ball.obj.heading() - 90)

    if ball.obj.ycor() < -270:
        if ball.obj.heading() == 225:
            ball.obj.setheading(ball.obj.heading() - 90)

        elif ball.obj.heading() == 315:
            ball.obj.setheading(ball.obj.heading() + 90)

    if ball.obj.xcor() > 370:
        if ball.obj.heading() == 315:
            ball.obj.setheading(ball.obj.heading() - 90)

        elif ball.obj.heading() == 45:
            ball.obj.setheading(ball.obj.heading() + 90)

    if ball.obj.xcor() < -370:
        if ball.obj.heading() == 135:
            ball.obj.setheading(ball.obj.heading() - 90)

        elif ball.obj.heading() == 225:
            ball.obj.setheading(ball.obj.heading() + 90)



    if ball.obj.distance(paddle1.paddle_obj) < 50\
            and ball.obj.xcor() < -285:
        print("made contact")
        if ball.obj.heading() == 225:
            ball.obj.setheading(ball.obj.heading() + 90)

        elif ball.obj.heading() == 135:
            ball.obj.setheading(ball.obj.heading() - 90)

    if ball.obj.distance(paddle2.paddle_obj) < 50\
            and ball.obj.xcor() > 285:
        print("made contact")
        if ball.obj.heading() == 45:
            ball.obj.setheading(ball.obj.heading() + 90)

        elif ball.obj.heading() == 315:
            ball.obj.setheading(ball.obj.heading() - 90)


    if ball.obj.xcor() < -370 or ball.obj.xcor() > 370:
        game_on = False

        if ball.obj.xcor() < -370:
            s_board_two.add_one()

        elif ball.obj.xcor() > 370:
            s_board_one.add_one()
        time.sleep(2)
        ball.obj.setpos((0, 0))
        ball.set_dir()
        game_on = True

    if (s_board_one.score == 2 and s_board_two.score < 2):
        game_on = False
        s_board_one.game_over()
    elif s_board_two.score == 2 and s_board_one.score < 2:
        game_on = False
        s_board_two.game_over()

    elif s_board_two.score == 2 and s_board_one.score == 2:
        game_on = False
        s_board_one.game_over_draw()

screen.exitonclick()