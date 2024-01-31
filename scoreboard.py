#Angela did this by using subclass

import turtle


FONT = ("Courier", 20, "normal")

from turtle import Turtle

class Scoreboard: #Angela did this by using subclass

    def __init__(self): #Angela did this by using subclass. I am doing by calling module inside the constructor.
        self.level=0
        tu=Turtle()
        self.turtle_from_init = tu
        tu.hideturtle()
        tu.color("black")
        tu.penup()
        tu.goto(-230,255)
        self.update_score()


    def update_score(self):
        self.turtle_from_init.clear()
        self.level += 1
        self.turtle_from_init.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.turtle_from_init.goto(0,0)
        self.turtle_from_init.write(f"GAME OVER", align="center", font=FONT)


