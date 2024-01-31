# I used car as a sub-class of Turtle. Angela did not do it that way (see comments below).
# It was getting confusing so I will create car and main separately.
import random
import turtle as tu

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
X_CORD=280
Y_CORD=list(range(-230,250))

class Car():

    def __init__(self):
        self.car_list = []
        self.speed=10
        self.count=30


    def create_car(self):
        rand1= random.randint(1,7) #only if it meets the condition, the car will be created. Otherwise, too many cars
        if rand1==1:
            car = tu.Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.goto(X_CORD, random.choice(Y_CORD))

            self.car_list.append(car)

    def move_car(self):
        for car_in_list in self.car_list:
            car_in_list.backward(self.speed)

    def cars_on_screen_control_logic(self):
        for x in self.car_list:
            if x.xcor()< -280:
                x.goto(X_CORD, random.choice(Y_CORD))
            else:
                pass





