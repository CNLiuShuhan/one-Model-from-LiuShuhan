from __future__ import division
import tkinter.simpledialog
mode=tkinter.simpledialog.askinteger("模式选择","""该模型目前一共有八个模式，分别可以计算
完全数、质数、从一开始的连续自然数之和、斐波那契数列、因数、表白工具，二十四点和汉诺塔
请选择其中一个输入(1-8)：""")

try :
    if mode == 1 :
        c,b,j=tkinter.simpledialog.askinteger("范围选择","在多少以内？"),1,1
        while b < c :
            a = 0
            for i in range(1,b) :
                if b%i == 0 :
                    a += i
            if a == b :
                print(b,end=' ')
            j += 1
            b += j

    elif mode == 2 :
        c=tkinter.simpledialog.askinteger("范围选择","在多少以内？")
        for n in range(2, c):
            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                print(n,end=' ')

    elif mode == 3 :
        c,a=tkinter.simpledialog.askinteger("项数选择","请问多少项？"),0
        for j in range(1,c+1):
            a=a+j
            print(f'第{j}项(从一加到{j})是:{a}')
        print("END")

    elif mode == 4 :
        a,b,c,f = 0,1,tkinter.simpledialog.askinteger("范围选择","在多少以内？"),[]
        while a < c:
            f.append(a)
            a,b=b,a+b
        print(f)

    elif mode == 5 :
        c,b,n=tkinter.simpledialog.askinteger("项数选择","请问多少项？"),1,1
        for j in range(1,c+1):
            a=[]
            for i in range(1,b+1):
                if b%i == 0 :
                    a.append(i)
            if len(a)>n:
                print(f'{j}:{a} {len(a)}--|>')
                n=len(a)
            else:
                print(f'{j}:{a} {len(a)}')
            b=b+1

    elif mode == 6 :
        from turtle import*
        from math import*
        from time import sleep
        try :
            hideturtle()
            penup()
            title('I love you!')
            speed('fast')
            fillcolor("pink")
            begin_fill()
            pensize(1.5)
            for i in range(400):
                x=100*(1-sin(radians(i)))*cos(radians(i))
                y=100*(1-sin(radians(i)))*sin(radians(i))
                goto(x,y)
                if i == 0 : pendown()
            end_fill()
            #heart
            tracer(0,0)
            penup()
            for i in range(-500,100):
                goto(i/100-300,100+i)
                if i==-10 :pendown()
            sleep(1)
            update()
            #I
            penup()
            a=0.4
            for i in range(300):
                goto(a*50-110,1/a*50+60)
                if i==0 :pendown()
                a+=0.01
            sleep(1)
            update()
            #l
            penup()
            a=-3
            for i in range(601):
                goto(a*30+70,sqrt(9-(a*a))*30+150)
                if i==1 :pendown()
                a+=0.01
            a=3
            for i in range(601):
                goto(a*30+70,-1*sqrt(9-(a*a))*30+150)
                if i==1 :pendown()
                a-=0.01
            sleep(1)
            #o
            update()
            for i in range(0,100):
                goto(i,abs(-2*i)+20)
            sleep(1)
            update()
            a=0
            #v
            penup()
            for i in range(0,360):
                goto(-3*abs(sin(radians(i)))*30+150,i*0.7-100)
                if i==0:pendown()
            sleep(1)
            update()
            #e
            penup()
            for i in range(-50,50):
                goto(i*10+300,i**3*10+50)
                if i==-50:pendown()
            #y
            sleep(1)
            update()
            mainloop()      
        except Terminator :
            pass
    elif mode == 7:
        import json,re,zlib
        try:
            with open(r".\result.json",'rb') as f:
                result=json.loads(zlib.decompress(f.read()))
        except FileNotFoundError:
            print('请编译你的JSON文件，见"_help"')
            raise SystemExit
        while True:
            key=input("哪项？格式遵循(n, n, n, n),后面的必须必前面的大。")
            if re.match(r'[(]\d+, \d+, \d+, \d+[)]',key)!=None:
                try:
                    if result[key] != "没有解":
                        print(result[key],len(result[key]))
                    else:
                        print("没有解")
                except KeyError:
                    print('如检查出后面的数确实比前面的大，请拓展你的JSON文件，见"_help"')
            else:
                print('已退出')
                break

    elif mode == 8 :
        x,y = tkinter.simpledialog.askinteger("项数选择","请问多少项？"),1
        find_keys = {'A':list(reversed([i for i in range(1,x+1)])),'B':[],'C':[]}
        def hanoi(n,a='A',b='B',c='C'):
            global y
            if n == 1 :
                find_keys[c].append(find_keys[a][-1:][0])
                find_keys[a][-1:]=[]
                print(y,':',a,'-->',c)
                print('A:',find_keys['A'])
                print('B:',find_keys['B'])
                print('C:',find_keys['C'])
                print('\n')
                y+=1
            else :
                hanoi(n - 1, a, c, b)
                find_keys[c].append(find_keys[a][-1:][0])
                find_keys[a][-1:]=[]
                print(y,':',a,'-->',c)
                print('A:',find_keys['A'])
                print('B:',find_keys['B'])
                print('C:',find_keys['C'])
                print('\n')
                y+=1
                hanoi(n - 1, b, a, c)
        if x <= 12 :
            print('A:',find_keys['A'])
            print('B:',find_keys['B'])
            print('C:',find_keys['C'])
            print('\n')
            hanoi(x)
        print('需要移动',str(2**x-1),'次。')
    elif mode == 9:
        from random import randint
        from time import sleep
        from copy import deepcopy
        WIDTH = 60
        HEIGHT = 20
        nextCells = []
        for x in range(WIDTH):
            column = []
            for y in range(HEIGHT):
                if (x,y) in ((1,0),(2,1),(0,2),(1,2),(2,2)):
                    column.append('#')
                else:
                    column.append(' ')
            nextCells.append(column)
        while True:
            print('_'*WIDTH,flush=True)
            currentCells = deepcopy(nextCells)
            for y in range(HEIGHT):
                for x in range(WIDTH):
                    if currentCells[x][y] == '#':
                        print('█',end='',flush=True)
                    else :
                        print(' ',end='',flush=True)
                print('|')
            for x in range(WIDTH):
                for y in range(HEIGHT):
                    leftCoord = (x-1)% WIDTH
                    rightCoord = (x+1)%WIDTH
                    aboveCoord = (y-1)%HEIGHT
                    belowCoord = (y+1)%HEIGHT
                    numNeighbors = 0
                    if currentCells[rightCoord][aboveCoord] == '#':
                        numNeighbors += 1
                    if currentCells[x][aboveCoord] == '#':
                        numNeighbors += 1
                    if currentCells[leftCoord][aboveCoord] == '#':
                        numNeighbors += 1
                    if currentCells[leftCoord][y] == '#':
                        numNeighbors += 1
                    if currentCells[leftCoord][belowCoord] == '#':
                        numNeighbors += 1
                    if currentCells[x][belowCoord] == '#':
                        numNeighbors += 1
                    if currentCells[rightCoord][belowCoord] == '#':
                        numNeighbors += 1
                    if currentCells[rightCoord][y] == '#':
                        numNeighbors += 1
                    if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                        nextCells[x][y] = '#'
                    elif currentCells[x][y] == ' ' and numNeighbors == 3:
                        nextCells[x][y] = '#'
                    else :
                        nextCells[x][y] = ' '
            sleep(1)
    else :
        print("No this mode.")
except TypeError :
    print("Please restart and don't click cancel.")
