# I used car as a sub-class of Turtle. Angela did not do it that way (see comments below).
# It was getting confusing so I create separately.
import random
import turtle as tu
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
X_CORD=list(range(-200,200))
Y_CORD=list(range(-200,200))

class Car(tu.Turtle): #no need to create a subclass.

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.shape("square")
        self.shapesize(1, 2)

    def create_car(self):
        self.penup()
        rand1 = random.randint(0, 5)
        self.color(COLORS[rand1])
        rand_x = random.choice(X_CORD)
        rand_y = random.choice(Y_CORD)
        self.goto(rand_x, rand_y)
        # self.car_list.append(self)
        # print (self.car_list)
        # print ("xcord is:", self.xcor(), "and ycord is: ", self.ycor())


    def move_car(self,list): # no need a param of list actually.
        for x in list:
            print ("Before", x.xcor(), x.ycor())
            x.backward(30)
            print("After", x.xcor(), x.ycor())
        # new_x= self.xcor()+10
        # self.goto(new_x,self.ycor())
        # print(f"new x and y: {self.xcor(),self.ycor()}")
        # print (self.distance(300,300))



