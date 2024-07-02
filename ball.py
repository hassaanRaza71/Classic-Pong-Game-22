from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed=0.1
        self.cooldown = False  # Flag to indicate cooldown after collision

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        if not self.cooldown:  # Check if cooldown is active
            self.x_move *= -1
            self.move_speed*=0.9
            self.cooldown = True  # Activate cooldown
            self.after_hit()

    def after_hit(self):
        # Reset cooldown after 0.5 seconds
        self.screen.ontimer(self.reset_cooldown, 500)

    def reset_cooldown(self):
        self.cooldown = False  # Reset cooldown

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed=0.1
        self.hit()  # Reset cooldown when resetting position
