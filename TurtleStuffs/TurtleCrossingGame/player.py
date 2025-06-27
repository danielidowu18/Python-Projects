from turtle import Screen, Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

my_screen = Screen()
class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.pu()
        self.goto(STARTING_POSITION)
        self.seth(90)
        
    def move_player(self):
        self.fd(MOVE_DISTANCE)    
        
    def move_player_key(self):
        my_screen.listen()
        my_screen.onkey(fun=self.move_player, key="Up") 

    def player_finish_line(self):
        self.goto(STARTING_POSITION)
        
        


    