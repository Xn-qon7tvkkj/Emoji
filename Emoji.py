import turtle

so = turtle.Turtle()
me = turtle.Turtle()
et = turtle.Turtle()
ca = turtle.Turtle()

turtle.bgcolor("blue")

def circle(side):
    for size in range(95):
        so.forward(10)
        so.left(4)


def eye1(side):
    for size in range(95):
        me.forward(3)
        me.left(4)


def eye2(side):
    for size in range(95):
        et.forward(3)
        et.left(4)


def mouth(side):
    for size in range(4):
        ca.right(90)
        ca.forward(25)


def pupil1(side):
    for size in range(65):
        so.forward(3)
        so.left(8)


def pupil2(side):
    for size in range(65):
        me.forward(3)
        me.left(8)


so.fillcolor("yellow")
so.penup()
so.goto(0, 0)
so.pendown()
so.pencolor("black")
so.begin_fill()
circle(1)
so.end_fill()

me.fillcolor("white")
me.penup()
me.goto(70, 100)
me.pendown()
me.pencolor("white")
me.begin_fill()
eye1(1)
me.end_fill()

et.fillcolor("white")
et.penup()
et.goto(-70, 100)
et.pendown()
et.pencolor("white")
et.begin_fill()
eye2(1)
et.end_fill()

ca.fillcolor("red")
ca.penup()
ca.goto(20, 40)
ca.pendown()
ca.pencolor("red")
ca.begin_fill()
mouth(1)
ca.end_fill()

so.fillcolor("black")
so.penup()
so.goto(80, 144)
so.pendown()
so.pencolor("black")
so.begin_fill()
pupil1(1)
so.end_fill()

me.fillcolor("black")
me.penup()
me.goto(-60, 144)
me.pendown()
me.pencolor("black")
me.begin_fill()
pupil2(1)
me.end_fill()

et.penup()
et.fillcolor("pink")
et.goto(-60, 50)
et.pendown()
et.pencolor("pink")
et.begin_fill()
et.circle(25, 360)
et.end_fill()

ca.penup()
ca.fillcolor("pink")
ca.goto(70, 45)
ca.pendown()
ca.pencolor("pink")
ca.begin_fill()
ca.circle(25, 360)
ca.end_fill()

turtle.exitonclick()