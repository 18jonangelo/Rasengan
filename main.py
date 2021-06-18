import turtle as t

turt = t.Turtle()


def circle():
    turt.color("#0077CC")
    # turt.speed(0)
    turt.circle(100, 360)


def move():
    turt.speed(0)
    turt.left(10)


for _ in range(360):

    circle()
    move()









screen = t.Screen()
screen.exitonclick()