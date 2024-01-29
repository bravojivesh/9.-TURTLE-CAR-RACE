import time
from turtle import Screen
from player import Player
from car2 import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

tu1=Player()
main_car_list=[] #becuase of sub-class, I had to create a list here in the main.

screen.onkey(tu1.move_up,"Up")

game_is_on = True

# while game_is_on == True:
for _ in range(10):
    time.sleep(0.6)
    screen.update()
    car1 = Car() #first i kept this outside--only created flickering cars. Spent days thinking aboyt this issue.
    car1.create_car()
    main_car_list.append(car1) #the main list is outside the loop.
    # Else, it will only create a list of one object everytime.

    # db: print(main_car_list)
    car1.move_car(main_car_list)



# while game_is_on:



        # while car1.xcor()> -350:
        #     time.sleep(0.6)
        #     screen.update()
        #     car1.move_car()

