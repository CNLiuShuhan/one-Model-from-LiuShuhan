# -*-coding:gb2312-*-
import turtle
def draw(lines,length,colours):
    turtle.pensize(2)
    turtle.fillcolor(colours)
    turtle.begin_fill()
    for i in range(0,lines):
        turtle.forward(length)
        turtle.left(360/lines)
    turtle.end_fill()
    turtle.hideturtle()
    return 'done'
print(
'''参考：
    边数 边长 颜色
    没有正一边形
    没有正二边形
    3 130 deep sky blue
    4 120 deep pink
    5 110 gold
    6 100 coral
    7 100 maroon1
    8 100 green4
    9 90 brown4
    10 80 cyan''')
while True :
    a=input("边数")
    if a == '':
        print('边数不能为空')
        continue
    if a == '0' or a == '1' or a == '2':
        print('没有该图形')
        continue
    try :
        a = int(a)
    except (ValueError,TypeError):
        print('类型错误,请重新输入')
        continue
    break
while True :
    b=input("边长")
    if b == '' :b = 100
    try :
        b = int(b)
    except (ValueError,TypeError):
        print('类型错误,请重新输入')
        continue
    break
while True :
    c=input("颜色")
    if c == '' :c = 'black'
    try :
        draw(a,b,c)
    except turtle.TurtleGraphicsError :
        print('没有这个颜色')
        continue
    break
        
