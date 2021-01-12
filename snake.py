from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)

    def add_body(self, position):
        new_snake_body = Turtle("square")
        new_snake_body.penup()
        new_snake_body.color("white")
        new_snake_body.goto(position)
        self.snake_body.append(new_snake_body)

    def extend(self):
        self.add_body(self.snake_body[-1].position())

    def move(self):
        """watch lecture No. 183 day 20 time stamp 9:23 to understand below code"""
        for snake_body_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake_body_num - 1].xcor()
            new_y = self.snake_body[snake_body_num - 1].ycor()
            self.snake_body[snake_body_num].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



