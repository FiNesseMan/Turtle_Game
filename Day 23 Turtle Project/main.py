import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random as rnd

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()

player1 = Player()

car_manager = CarManager()

screen.listen()
screen.onkey(player1.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()

    #Detect colosion
    for car in car_manager.all_cars:
        if car.distance(player1) < 20:
            game_is_on = False
            Scoreboard.game_over()

    # Detect successful crossing:
    if player1.is_at_finish():
        player1.go_to_start()
        car_manager.level_up()
        scoreboard.update_scoreboard()
        scoreboard.increase_level()


screen.exitonclick()