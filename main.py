import time
from turtle import Screen
from turtle import  textinput
from player import Player
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

tu1=Player()
score=Scoreboard()

car1=Car()

screen.onkey(tu1.move_up,"Up")

game_is_on = True
total_cars_on_screen = 0

while game_is_on == True:
    time.sleep(0.1)
    screen.update()

    # if total_cars_on_screen <car1.count:
    #     car1.create_car()
    #     total_cars_on_screen= len(car1.car_list)

    car1.create_car()
    car1.move_car()

    for car in car1.car_list:
        # db:print (tu1.distance((car)))
        if tu1.distance(car) <30: #detect collision
            # db: print (tu1.distance(car))

            game_is_on= False
            score.game_over()
            user_input = textinput("Message Box", "GAME OVER")


    if tu1.ycor() >260: #when crosses the finish line
        print ("Level complete")
        tu1.reset()
        car1.speed+=5 #we can also do this by creating a method in car class to update just the speed
        score.update_score()



screen.exitonclick()