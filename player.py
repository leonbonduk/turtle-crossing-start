from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.x_position = STARTING_POSITION[0]
        self.y_position = STARTING_POSITION[1]
        self.penup()
        self.goto(x=self.x_position, y=self.y_position)
        self.shape("turtle")
        self.color("black")
        self.setheading(90)

    def up(self):
        self.y_position += MOVE_DISTANCE
        self.goto(x=self.x_position, y=self.y_position)

    def back_to_start(self):
        self.goto(STARTING_POSITION)
        self.x_position = STARTING_POSITION[0]
        self.y_position = STARTING_POSITION[1]