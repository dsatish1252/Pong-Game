from turtle import Turtle


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0,300)
        self.setheading(90)
        self.pensize(15)
        self.shape("square")
        self.speed("fastest")
        self.color("white")
        for i in range(0, 600):
            self.color("white")
            self.backward(20)
            self.color("black")
            self.backward(20)
