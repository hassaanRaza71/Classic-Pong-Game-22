from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(x_pos, 0)

    def move_up(self):
        if self.ycor() < 250:  # Ensure the paddle doesn't move out of the top boundary
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -240:  # Ensure the paddle doesn't move out of the bottom boundary
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
