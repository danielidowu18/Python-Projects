from turtle import Turtle


FONT = ("courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lev_num = 1
        self.hideturtle()
        self.pu()
        self.goto(-280, 260)
        self.color("black")
        self.lev_writing()
        
    def lev_writing(self):
        self.write(arg=f"Level: {self.lev_num}", align="left", font=FONT)    
        
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over!", align="center", font=FONT)
        
    def level_up(self):
        self.lev_num += 1
        self.clear()
        self.lev_writing()