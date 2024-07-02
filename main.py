from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setting up the screen
game_screen = Screen()
game_screen.bgcolor("black")
game_screen.setup(width=800, height=600)
game_screen.title("Classic Pong Game 🎮")
game_screen.tracer(0)  # Turn off automatic screen updates

# Creating paddles
right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

# Setting up key bindings
game_screen.listen()
game_screen.onkeypress(right_paddle.move_up, "Up")
game_screen.onkeypress(right_paddle.move_down, "Down")
game_screen.onkeypress(left_paddle.move_up, "w")
game_screen.onkeypress(left_paddle.move_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    game_screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with right paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320):
        if ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50:
            ball.hit()

    # Detect collision with left paddle
    if (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        if ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50:
            ball.hit()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score_increase()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score_increase()

game_screen.mainloop()
