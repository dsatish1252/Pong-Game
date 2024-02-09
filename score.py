from turtle import Turtle

FONT = ("Arial", 60, "bold")
ALIGN = "center"

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.ls = 0
        self.rs = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.display()


    def update_score(self):
        self.clear()
        self.display()

    def display(self):
        self.goto(0,210)
        self.write(f"{self.ls}     {self.rs}", align=ALIGN, font=FONT)