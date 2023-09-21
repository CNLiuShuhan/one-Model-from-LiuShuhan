from turtle import*
setup(400,600)
shape("turtle")
#准备工作
color("brown4")
begin_fill()
goto(20,0)
goto(20,-280)
goto(-20,-280)
goto(-20,0)
end_fill()
color("Spring Green4")
dy=[120,160,220]
dx=[160,120,80]
dy2=[-120,0,100]
for i in range(0,3):
    up()
    goto(0,dy[i])
    down()
    begin_fill()
    goto(-dx[i],dy2[i])
    goto(dx[i],dy2[i])
    goto(0,dy[i])
    end_fill()
#画树
color("red")
dot(30)
x=[-80,80,-40,40,0,-40,40,0,0]
y=[-80,-80,-40,-40,0,40,40,100,160]
colour=["cyan","cyan","deep pink","deep pink","deep sky blue","yellow","yellow","IndianRed2","magenta2"]
for h in range(0,9):
    up()
    goto(x[h],y[h])
    down()
    color(colour[h])
    dot(20)
#画球
speed(6)
wx=[-90,70,-130,115,-160,165]
wy=[100,100,10,10,-105,-110]
wc=["pink","pink","purple","purple","orange","orange"]
for z in range(0,6):
    up()
    goto(wx[z],wy[z])
    down()
    color(wc[z])
    begin_fill()
    for d in range(0,5):
        forward(25)
        left(144)
    end_fill()
    right(30)
#画星
speed(3)
addshape("D:\liushuhan\program\picture\Merry Christmas.gif")
up()
goto(0,255)
shape("D:\liushuhan\program\picture\Merry Christmas.gif")
stamp()
#写字
hideturtle()
done()
