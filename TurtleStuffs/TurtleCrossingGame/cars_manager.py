import random
from turtle import Screen, Turtle


CAR_COLOURS = ["red", "green", "blue", "purple", "orange", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# my_screen = Screen()
class Cars(Turtle):
    car_list = []
    def __init__(self):
        super().__init__()
        self.starting_move_distance = STARTING_MOVE_DISTANCE
        self.create_car()
            # car_.pu()
            # rand_x = random.randint(0, 300)
            # rand_y = random.randint(-250, 250)
            # car_.goto(rand_x, rand_y)
        # self.move_cars()
        
        
    def create_car(self):
            self.shape("square")
            self.shapesize(stretch_len=1.5, stretch_wid=1)
            self.pu()      
            self.color(random.choice(CAR_COLOURS))
            # self.seth(180)
            rand_x = random.randint(270, 500)
            rand_y = random.randint(-240, 250)
            self.goto(rand_x, rand_y)
            # self.car_list.append(self.create_car)
                
            
    def move_cars(self):
        for car_item in self.car_list:
            car_item.backward(self.starting_move_distance)       
        
    def new_level(self):
        self.starting_move_distance += MOVE_INCREMENT
        
# car = Cars()        

# my_screen.exitonclick()       