from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
WIDTH = 20
LENGTH = 40

# class CarManager(Turtle): carmanger isnt a turtle, the cars are
class CarManager():
    def __init__(self):
        super().__init__()
        self.car_fleet = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.goto(x=300, y=random.randint(-250, 250))
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=WIDTH/20, stretch_len=LENGTH/20)
        self.car_fleet.append(new_car)

    def move_cars(self, speed):
        for car in self.car_fleet:
            x_position = car.xcor() - STARTING_MOVE_DISTANCE - (MOVE_INCREMENT * (speed -1))
            car.goto(x=x_position, y=car.ycor())

    def clear_fleet(self):
        self.car_fleet.clear()