from turtle import Turtle
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):

        self.square_list = []
        self.create_snake()

    def create_snake(self):
        x_position = 0
        y_position = 0
        for i in range(3):
            square = Turtle("square")
            square.color("white")
            square.penup()
            square.setposition(x=x_position, y=y_position)
            self.square_list.append(square)
            x_position += -20

    def extend(self):
        extend_square = Turtle("square")
        extend_square.color("white")
        extend_square.penup()
        position = self.square_list[-1].position()
        extend_square.setposition(position)
        self.square_list.append(extend_square)

    def move(self):

        for square_num in range(len(self.square_list) - 1, 0, -1):
            new_x = self.square_list[square_num - 1].xcor()
            new_y = self.square_list[square_num - 1].ycor()
            self.square_list[square_num].goto(new_x, new_y)
        self.square_list[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.square_list[0].heading() != 270:
            self.square_list[0].setheading(90)

    def down(self):
        if self.square_list[0].heading() != 90:
            self.square_list[0].setheading(270)

    def left(self):
        if self.square_list[0].heading() != 0:
            self.square_list[0].setheading(180)

    def right(self):
        if self.square_list[0].heading() != 180:
            self.square_list[0].setheading(0)
