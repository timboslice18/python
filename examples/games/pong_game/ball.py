from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        #reverse the direction of y_move by multiplying by -1
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        #reverse the direction of x_move by multiplying by -1
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        #set move speed back to original value since the game has reset
        self.move_speed = 0.1
        #reverse direction of initial bounce
        self.bounce_x()