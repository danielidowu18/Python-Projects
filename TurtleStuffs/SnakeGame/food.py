from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.refresh()
    
    def refresh(self):
        xcoor = random.randint(-280, 280)
        ycoor = random.randint(-280, 260)
        self.goto(xcoor, ycoor)    
        
        
        
# food = Food()
# print(food)        

# screen = Screen()
# screen.exitonclick()