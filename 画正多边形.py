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
'''�ο���
    ���� �߳� ��ɫ
    û����һ����
    û����������
    3 130 deep sky blue
    4 120 deep pink
    5 110 gold
    6 100 coral
    7 100 maroon1
    8 100 green4
    9 90 brown4
    10 80 cyan''')
while True :
    a=input("����")
    if a == '':
        print('��������Ϊ��')
        continue
    if a == '0' or a == '1' or a == '2':
        print('û�и�ͼ��')
        continue
    try :
        a = int(a)
    except (ValueError,TypeError):
        print('���ʹ���,����������')
        continue
    break
while True :
    b=input("�߳�")
    if b == '' :b = 100
    try :
        b = int(b)
    except (ValueError,TypeError):
        print('���ʹ���,����������')
        continue
    break
while True :
    c=input("��ɫ")
    if c == '' :c = 'black'
    try :
        draw(a,b,c)
    except turtle.TurtleGraphicsError :
        print('û�������ɫ')
        continue
    break
        
