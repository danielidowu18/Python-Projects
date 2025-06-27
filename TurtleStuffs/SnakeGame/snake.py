from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    
    def __init__(self):
        self.blocks = []
        self.create_snake()
    
    def create_snake(self):
        """Creates a new snake"""
        n = 0
        for _ in range(3):
            new_block = Turtle(shape="circle")
            new_block.color("white")
            new_block.shapesize(0.75, 0.75)
            new_block.pu()
            new_block.goto(x=n, y=0)
            n -= 20
            self.blocks.append(new_block)
    
    def create_tail(self):
        new_tail = Turtle(shape="circle")
        new_tail.color("white")
        new_tail.shapesize(0.75, 0.75)
        new_tail.pu()
        self.blocks.append(new_tail)
        self.move()
        
    def move(self):
        """Moves the snake"""
        for block_num in range(len(self.blocks) - 1, 0, -1):
            x_coord = self.blocks[block_num -1].xcor()
            y_coord = self.blocks[block_num -1].ycor()
            self.blocks[block_num].goto(x_coord, y_coord)
        self.blocks[0].fd(20)
        
    def up(self):
        if self.blocks[0].heading() != DOWN:
            self.blocks[0].seth(UP)    
        
    def down(self):
        if self.blocks[0].heading() != UP:
            self.blocks[0].seth(DOWN)  
        
    def right(self):
        if self.blocks[0].heading() != LEFT:
            self.blocks[0].seth(RIGHT)  
        
    def left(self):
        if self.blocks[0].heading() != RIGHT:
            self.blocks[0].seth(LEFT)  