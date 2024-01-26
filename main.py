import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

tu1=Player()
car1=CarManager()

screen.onkey(tu1.move_up,"Up")

game_is_on = True

for _ in range(10):
    time.sleep(0.6)
    screen.update()
    car1.create_cars()


# while game_is_on:
for _ in range(10):
    pass
    # time.sleep(0.6)
    # screen.update()
    #
    # car1.create_car()
    # print ("new car")
    # car_list.append((car1))
    # print ("Added to the list")
    # print ("list lenght:", len(car_list),"last car's cords:", car_list[-1].xcor(),car_list[-1].ycor())
    # # car1.multiple_cars()


        # while car1.xcor()> -350:
        #     time.sleep(0.6)
        #     screen.update()
        #     car1.move_car()

