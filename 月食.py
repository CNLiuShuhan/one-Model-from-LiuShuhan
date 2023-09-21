from turtle import *
hideturtle()
bgcolor("black")
color("yellow")
dot(300)
penup()
#画整月
a = 300
def hua(long,color):
    global a
    goto(a,0)
    pencolor(color)
    dot(long)
def chi():
    global a
    if a>0:
        hua(350,"black")
    elif a==0:
        hua(300,"red2")
    elif a<0 and a>-350:
        goto(0,0)
        pencolor("yellow")
        dot(300)
        hua(350,"black")
        tracer(0,0)
    else:
        print("月食已结束!")
        exit()
    a=a-10
listen()
onkey(chi,"space")
#被吃掉
done()

