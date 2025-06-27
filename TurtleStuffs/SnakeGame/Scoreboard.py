from turtle import Turtle

class ScoreTrack(Turtle):
    
    score_num = 0
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(0, 268)
        self.color("white")
        self.write(align="center", arg=f"Score: {self.score_num}", font=("Arial", 15, "normal"))
        
    def game_over(self):
        self.home()
        self.write(align="center", arg="GAME OVER", font=("Arial", 15, "normal"))    
        
        
    def eats_food(self):
        self.score_num += 1
        self.clear()    
        self.write(align="center", arg=f"Score: {self.score_num}", font=("Arial", 15, "normal"))
        
        
