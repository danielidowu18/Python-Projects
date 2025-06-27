import time
from turtle import Turtle, Screen
from score import Scoreboard
from ball import Ball
from paddle import Paddle

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.tracer(0)
dashes = Turtle()
dashes.hideturtle()
dashes.pu()
dashes.speed("fastest")
dashes.color("white")
dashes.goto(0, 400)
dashes.seth(270)
while dashes.ycor() > -350:
    dashes.pd()
    dashes.fd(10)
    dashes.pu()
    dashes.fd(10)
    
paddle1 = Paddle(-380)
paddle2 = Paddle(380)
ball = Ball()
score = Scoreboard()

paddle1.keys_for_1(paddle1)
paddle2.keys_for_2(paddle2) 
# ball.move_ball_key()   

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
        
    if (ball.distance(paddle1) < 50 and ball.xcor() < -360) or (ball.distance(paddle2) < 50 and ball.xcor() > 360):
        ball.bounce_x()    
    
    if ball.xcor() > 390:
        score.paddle1_scores()
        ball.reset_position()
        
    if ball.xcor() < -390:
        score.paddle2_scores()
        ball.reset_position()    



my_screen.exitonclick()