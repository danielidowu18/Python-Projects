from turtle import *
import random
dan = Turtle()
colormode(255)
my_screen = Screen()
dan.speed("fastest")
dan.hideturtle()
def colour():    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    # OR
    # dan.color(random_color)
    return random_color
def basic_move():
    for _ in range(10):
        # colour()
        dan.dot(20, colour())
        dan.penup()
        dan.fd(50)        
n = 50
for _ in range(10):
    basic_move()
    dan.goto(0, n)
    n += 50

my_screen.exitonclick()