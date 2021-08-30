import time
from turtle import Screen
import random
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
roadkill = Player()
score_board = Scoreboard()

screen.listen()
screen.onkey(roadkill.up, "Up")

game_is_on = True
Level = 1

while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Random decide to create a car
    if random.random() < 0.1:
        car_manager.create_car()

    car_manager.move_cars(Level)
    for car in car_manager.car_fleet:
        #Detect crash
        #if abs(roadkill.x_position - car.xcor())< 30 and abs(roadkill.y_position - car.ycor())< 20:
        if car.distance(roadkill) < 20:
            game_is_on = False
            score_board.game_over()

    #Detect crossed road
    if roadkill.y_position == 280:
        roadkill.back_to_start()
        score_board.update_scoreboard()
        Level += 1
        car_manager.clear_fleet()
        #for car in car_fleet:
        #    car.clear()
        #car_fleet.clear()







screen.exitonclick()