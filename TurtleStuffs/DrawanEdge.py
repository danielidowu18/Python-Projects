from  turtle import *

dan = Turtle()
my_screen = Screen()
def move_fd():
    dan.fd(10)
def move_bd():
    dan.backward(10)
def turn_clockwise():
    dan.right(20)
def turn_anticlockwise():
    dan.left(20) 
def page_clear():
    dan.penup()
    dan.clear()
    dan.goto(0, 0)
    dan.seth(0)
    dan.pendown()              
my_screen.onkey(key="w", fun=move_fd)
my_screen.onkey(key="s", fun=move_bd)
my_screen.onkey(key="a", fun=turn_anticlockwise)
my_screen.onkey(key="d", fun=turn_clockwise)
my_screen.onkey(key="c", fun=page_clear)


my_screen.listen()
my_screen.exitonclick()