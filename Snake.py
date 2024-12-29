import turtle
from turtle import Turtle, Screen
import time

SEGMENT_POSITION = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for posistion in SEGMENT_POSITION:
           self.add_new_segments(posistion)
    
    def add_new_segments(self, position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
            
    def extend(self):
        self.add_new_segments(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


            
    def move(self):
        for seg_index in range(len(self.segments) - 1, 0, -1):       # range(start, stop, step)
                new_x =  self.segments[seg_index - 1].xcor()              # need x cord of the swgment ahead 
                new_y =  self.segments[seg_index - 1].ycor()              # need y cord of sgement ahead
                self.segments[seg_index].goto(new_x, new_y)              # making it go to the postion of segment ahead
        self.segments[0].forward(20)
    
    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)






