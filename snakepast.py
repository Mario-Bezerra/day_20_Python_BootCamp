from turtle import Turtle

INITIAL_POSITION = [(-20, 0), (0, 0), (20, 0)]
MOVE_SIZE = 20
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
        for position in INITIAL_POSITION:
            self.add_new_body(position)

    def add_new_body(self,position):
        snake_part = Turtle(shape="square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake_body.append(snake_part)

    def increase_size(self):
        self.add_new_body(self.snake_body[-1].position())

    def snake_move(self):
        for snake in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[snake - 1].xcor()
            new_y = self.snake_body[snake - 1].ycor()
            self.snake_body[snake].goto(new_x, new_y)
        self.head.forward(MOVE_SIZE)

    def reset(self):
        for piece in self.snake_body:
            piece.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

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



