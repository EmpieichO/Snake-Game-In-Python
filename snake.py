from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_trail = []
        self.create_snake()
        self.snake_head = self.snake_trail[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def add_square(self, position):
        snake_sqr = Turtle()
        snake_sqr.penup()
        snake_sqr.shape("square")
        snake_sqr.color("white")
        snake_sqr.goto(position)
        self.snake_trail.append(snake_sqr)

    def snake_extend(self):
        self.add_square(self.snake_trail[-1].position())

    def move(self):
        for i in range(len(self.snake_trail)-1, 0, -1):
            new_x = self.snake_trail[i - 1].xcor()
            new_y = self.snake_trail[i - 1].ycor()
            self.snake_trail[i].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
