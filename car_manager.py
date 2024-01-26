import random
import turtle as tu
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
GAP_BETWEEN_LINES=2
GAP_BETWEEN_CARS=4
X_CORD=list(range(-200,200))
Y_CORD=list(range(-200,200))

class CarManager(tu.Turtle):

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.shape("square")
        self.shapesize(1, 2)


    def car(self):
        self.penup()

        rand1 = random.randint(0, 5)
        self.color(COLORS[rand1])

        rand_x = random.choice(X_CORD)
        rand_y = random.choice(Y_CORD)
        self.goto(rand_x, rand_y)


        # print ("xcord is:", self.xcor(), "and ycord is: ", self.ycor())

    def create_cars(self):
        for _ in (10):
            x= self.car()
            self.car_list.append(x)

    def move_car(self):
        self.backward(30)

        # new_x= self.xcor()+10
        # self.goto(new_x,self.ycor())
        print(f"new x and y: {self.xcor(),self.ycor()}")
        print (self.distance(300,300))



