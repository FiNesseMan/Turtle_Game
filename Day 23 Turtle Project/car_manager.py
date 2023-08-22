from turtle import Turtle
import random as rnd
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
my_list = list(range(-300, 301))
car_list = range(0,50)
number_of_cars = (rnd.choice(car_list))
y_choice = rnd.choice(my_list)

class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    
    def create_car(self):
        random_chance = rnd.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shape("square")
            new_car.color(rnd.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.penup()
            y_position = rnd.randint(-250, 250)
            new_car.goto(x = 285, y = y_position)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        

            


    # def create_cars(self):
    #     for i in range(0,25):
    #         self.cars()


