import turtle
turtle.color("green")
turtle.hideturtle()
def zhongcao(x,y):
   for j in range(0,3):
      turtle.penup()
      turtle.goto(x,y)
      turtle.pendown()
      angle=[-6,2.5,6]
      Pensize=5
      turtle.pensize(Pensize)
      turtle.setheading(90)
      for i in range(0,20):
         turtle.forward(1.5)
         turtle.right(angle[j])
         Pensize=Pensize-0.25
         turtle.pensize(Pensize)
turtle.onscreenclick(zhongcao)
turtle.tracer(0)
turtle.done()
