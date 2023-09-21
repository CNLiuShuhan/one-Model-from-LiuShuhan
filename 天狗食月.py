import turtle
turtle.bgcolor("black")
turtle.color("yellow")
turtle.hideturtle()
turtle.dot(300)
def chi(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color("black")
    turtle.dot(75)
turtle.onscreenclick(chi)
turtle.done()
