from turtle import Screen, Turtle

class Paddle(Turtle):
    my_screen = Screen()
    
    def __init__(self, xcoor):
        super().__init__()
        self.create_paddle(xcoor)
        
    def create_paddle(self, xcoord):
        self.hideturtle()
        self.pu()
        self.color("white")
        self.speed("fastest")
        self.goto(xcoord, 0)
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=0.8)
        self.seth(90)
        self.showturtle()    
    
    def keys_for_1(self, paddle):
        self.my_screen.listen()
        self.my_screen.onkey(paddle.up, "w")    
        self.my_screen.onkey(paddle.down, "s")
        
    def keys_for_2(self, paddle):
        self.my_screen.listen()
        self.my_screen.onkey(paddle.up, "Up")    
        self.my_screen.onkey(paddle.down, "Down")    
        
    def up(self):
        self.fd(30)
    
    def down(self):
        self.backward(30)            
        
# paddle = Paddle()

# screen = Screen()
# screen.exitonclick()