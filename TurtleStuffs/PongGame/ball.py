from turtle import Turtle, Screen
# import random

class Ball(Turtle):
    my_screen = Screen()
    def __init__(self):
        super().__init__()
        self.speed("fast")
        self.pu()
        self.create_ball()
        # random_distance = random.randint(135, 225)
        # self.seth(random_distance)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    def create_ball(self):
        self.shape("circle")
        self.color("white")
        
    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)    
        
    # def move_ball_key(self):
    #     self.my_screen.listen()  
    #     self.my_screen.onkey(self.move_ball, key=" ")
        
    def bounce_y(self):
        self.y_move *= -1   
        
    def bounce_x(self):
        self.x_move *= -1    
        self.move_speed *= 0.9
        
    def reset_position(self):
        self.home()    
        self.bounce_x()
            