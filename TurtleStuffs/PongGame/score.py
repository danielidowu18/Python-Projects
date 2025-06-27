from turtle import Turtle

class Scoreboard(Turtle):
    paddle1_score = 0
    paddle2_score = 0
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-5, 270)
        self.pd()
        self.write(arg=f" {self.paddle1_score}: {self.paddle2_score}", font=("Arial", 20, "normal"), align="center")
        
    def paddle1_scores(self): 
        self.clear()
        self.paddle1_score += 1
        self.write(arg=f" {self.paddle1_score}: {self.paddle2_score}", font=("Arial", 20, "normal"), align="center")   
    
    def paddle2_scores(self): 
        self.clear()
        self.paddle2_score += 1
        self.write(arg=f" {self.paddle1_score}: {self.paddle2_score}", font=("Arial", 20, "normal"), align="center")
        
        