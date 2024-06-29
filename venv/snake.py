from turtle import Turtle

STARTING_POSITION = [(0.00, 0.00), (-20.00, 0.00), (-40.00, 0.00)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.createTurtle()
        self.head = self.turtles[0]

    def createTurtle(self):
        for i in STARTING_POSITION:
            self.addturtle(i)

    def addturtle(self, i):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("red")
        new_turtle.penup()
        new_turtle.goto(i)
        self.turtles.append(new_turtle)

    def extend(self):
        i = self.turtles[-1].pos()
        self.addturtle(i)

    def moveTurtle(self):
        for x in range(len(self.turtles) - 1, 0, -1):
            end = self.turtles[x]
            end.goto(self.turtles[x - 1].pos())
        self.turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)

    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)

    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)
