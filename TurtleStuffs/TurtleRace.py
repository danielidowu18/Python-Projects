import random
from turtle import *

my_screen = Screen()
my_screen.setup(width=500, height=400)
is_on = False
user_bet = my_screen.textinput("Make your bet", "What color of turtle do you choose?")
colors = ["red", "orange", "purple", "yellow", "green", "blue"]
ypositions = [-60, -30, 0, 30, 60, 90]
all_turtles = []
hideturtle()

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, ypositions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_on = True

while is_on == True:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You've won. The {winning_turtle} turtle won the race.")
            else:
                print(f"You lost. The {winning_turtle} turtle won the race.")
    
        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)
        
my_screen.exitonclick()