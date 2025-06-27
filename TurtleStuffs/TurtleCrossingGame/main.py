import random
import time
from turtle import Screen
from score import Scoreboard
from player import Player
from cars_manager import Cars


my_screen = Screen()
my_screen.setup(600, 600)
my_screen.tracer(0)

player = Player()

score = Scoreboard()
def plenty_cars():
    for _ in range(random.randint(5, 10)): 
        global car
        car = Cars()
        car.car_list.append(car)
player.move_player_key()

plenty_cars()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    # plenty_cars()
    car.move_cars()
    if car.car_list[-1].xcor() < 100:
        plenty_cars()
    
    for car_item in car.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
        
    if player.ycor() > 280:
        player.player_finish_line()
        score.level_up()    
        car.new_level()
    

my_screen.exitonclick()    