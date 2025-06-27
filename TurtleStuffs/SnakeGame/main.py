from turtle import Screen
import time
from Scoreboard import ScoreTrack
from snake import Snake
from food import Food

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=600, height=600)
my_screen.title("Snake Game")
my_screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreTrack()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.right, "Right")
my_screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    
    my_screen.update()
    time.sleep(0.15)
    
    snake.move()
    if snake.blocks[0].distance(food) <= 16:
        food.refresh()
        score.eats_food()
        snake.create_tail()

    if snake.blocks[0].xcor() > 280 or snake.blocks[0].xcor() <= -305 or snake.blocks[0].ycor() >= 305 or snake.blocks[0].ycor() < -280:
        is_game_on = False
        score.game_over()
    
    for block in snake.blocks[1:]:
        if snake.blocks[0].distance(block) < 10:
            is_game_on = False 
            score.game_over()
        
 
my_screen.exitonclick()