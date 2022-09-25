from turtle import Turtle

pos = [(0, 0), (-20, 0), (-40, 00)]
move_distance = 20


class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in pos:
            self.add_segment(position)

    def add_segment(self, position):
        i = Turtle("square")
        i.color("white")
        i.pu()
        i.goto(position)
        self.segments.append(i)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def refresh(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x_cor = self.segments[i - 1].xcor()
            new_y_cor = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x_cor, new_y_cor)
        self.head.fd(move_distance)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

