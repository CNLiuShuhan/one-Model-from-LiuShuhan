from tkinter.simpledialog import askinteger
from sys import argv
try :
    if len(argv) > 1 :
        mode = int(argv[1])
    else : mode = askinteger("模式选择","""该模型用于计算数学规律，目前有
1完全数、2质数、3从一开始的连续自然数之和、4斐波那契数列、5因数、6表白工具、7二十四点、\
8汉诺塔、9Conway生命游戏、10杨辉三角和11正方形及三角形数十一种功能，
请选择其中一个输入(1-11)：""")

    if mode == 1 :
        c,b,j = askinteger("范围选择","在多少以内？"),1,1
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
        a = askinteger("范围选择","在多少以内？")
        for n in range(2, a):
            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                print(n,end=' ')

    elif mode == 3 :
        a,c = askinteger("范围选择","在多少以内？"),0
        for j in range(1,a):
            c=c+j
            print(f'第{j}项(从一加到{j})是:{c}')
        print("结束")

    elif mode == 4 :
        a,b,c,f = 0,1,askinteger("范围选择","在多少以内？"),[]
        while a < c:
            f.append(a)
            a,b=b,a+b
        print(f)

    elif mode == 5 :
        c,b,n = askinteger("范围选择","在多少以内？"),1,1
        for j in range(1,c):
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
        setup(0.9,0.9)
        hideturtle()
        title('I LOVE YOU!')
        speed('fast')
        pensize(1.5)
        fillcolor("pink")
        penup()
        begin_fill()
        for i in range(0,380):
            goto(100*(1-sin(radians(i)))*cos(radians(i)),
                100*(1-sin(radians(i)))*sin(radians(i)))
            if i == 0 : pendown()
        end_fill()
        tracer(0,0)
        penup()
        for i in range(0,160):
            goto(i/100-500,i+80)
            if i==0 :pendown()
        sleep(1)
        update()
        penup()
        a=0.25
        for i in range(0,350):
            goto(a*40-370,1/a*40+70)
            if i==0 :pendown()
            a+=0.01
        sleep(1)
        update()
        penup()
        a=60
        for i in range(0,600):
            goto(a-175,sqrt(3600-a*a)+150)
            if i==0 :pendown()
            a-=0.2
        a=-60
        for i in range(0,600):
            goto(a-175,-sqrt(3600-a*a)+150)
            if i==0 :pendown()
            a+=0.2
        sleep(1)
        update()
        penup()
        for i in range(-100,100):
            goto(i*0.6-50,abs(-2*i)*0.7+80)
            if i==-100 :pendown()
        sleep(1)
        update()
        penup()
        for i in range(0,360):
            goto(-3*abs(sin(radians(i)))*25+100,i/2*0.9+70)
            if i==0 :pendown()
        sleep(1)
        update()
        penup()
        a=-5
        for i in range(0,105):
            goto(a*15+250,a**3*0.7+100)
            if i==0 :pendown()
            a+=0.1
        sleep(1)
        update()
        penup()
        a=-60
        for i in range(0,600):
            goto(a+400,sqrt(3600-a*a)+150)
            if i==0 :pendown()
            a+=0.2
        a=60
        for i in range(0,600):
            goto(a+400,-1*sqrt(3600-a*a)+150)
            if i==0 :pendown()
            a-=0.2
        sleep(1)
        update()
        penup()
        for i in range(-15,16):
            goto(i*4+520,i*i*0.5+100)
            if i==-15 :pendown()
        sleep(1)
        update()
        mainloop()      

    elif mode == 7 :
        import re
        from itertools import combinations, combinations_with_replacement
        class Solver:
            target = 24
            ops = ['+', '-', '*', '/', '--', '//']
            def __init__(self, precise_mode=False):
                self.precise_mode = precise_mode
            def solution(self, nums):
                result = []
                groups = self.dimensionality_reduction(self.format(nums))
                for group in groups:
                    for op in self.ops:
                        exp = self.assemble(group[0], group[1], op)['exp']
                        if self.check(exp, self.target) and exp not in result:
                            result.append(exp)
                return [exp + '=' + str(self.target) for exp in result]
            def dimensionality_reduction(self, nums):
                result = []
                if len(nums) > 2:
                    for group in self.group(nums, 2):
                        for op in self.ops:
                            new_group = [self.assemble(group[0][0], group[0][1], op)] + group[1]
                            result+=self.dimensionality_reduction(new_group)
                else:
                    result = [nums]
                return result
            def assemble(self, exp1, exp2, op):
                if op == '--' or op == '//':
                    return self.assemble(exp2, exp1, op[0])
                if op in r'*/':
                    exp1 = self.add_parenthesis(exp1)
                    exp2 = self.add_parenthesis(exp2)
                if self.precise_mode:
                    if op == '-':
                        exp2 = self.add_parenthesis(exp2)
                    elif op == '/':
                        exp2 = self.add_parenthesis(exp2, True)
                exp = self.convert(exp1['exp'] + op + exp2['exp'], op)
                return {'op': op, 'exp': exp}
            @staticmethod
            def add_parenthesis(exp, is_necessary=False):
                if (is_necessary and not exp['exp'].isdigit()) or exp['op'] in r'+-':
                    result = {'exp': '(' + exp['exp'] + ')','op': exp['op']}
                else:
                    result = exp
                return result
            @staticmethod
            def check(exp, target, precision=0.0001):
                try:
                    return abs(eval(exp) - target) < precision
                except ZeroDivisionError:
                    return False
            @staticmethod
            def convert(exp, op):
                    if op in r'+-':
                        pattern = r'([\+\-]((\(.+\)|\d+)[\*\/](\(.+\)|\d+)|\d+))'
                        exp = '+' + exp
                    else:
                        pattern = r'([\*\/](\(.+?\)|\d+))'
                        exp = '*' + exp
                    result = ''.join(sorted([i[0] for i in re.findall(pattern, exp)]))
                    if len(result) != len(exp):
                        result = exp
                    return result[1:]
            @staticmethod
            def format(nums):
                return [{'op': ' ', 'exp': str(num)} for num in nums]
            @staticmethod
            def group(exp_list, counter):
                index_list = [i for i in range(len(exp_list))]
                combination = list(combinations(index_list, counter))
                for group1 in combination:
                    group2 = list(set(index_list) - set(group1))
                    yield [[exp_list[g1] for g1 in group1],[exp_list[g2] for g2 in group2]]
        solver = Solver()
        findobj = re.compile(r'^\d+ \d+ \d+ \d+$')
        while True:
            key = input('请用本格式("+"替换为空格)：第一个数字+第二个数字+第三个数字+第四个数字\t：')
            if re.match(findobj,key):
                x = solver.solution(tuple(str(no) for no in key.split()))
                print(x,len(x))
            else:
                print('已退出')
                break

    elif mode == 8 :
        a,y = askinteger("项数选择","请问多少项？"),1
        find_keys = {'A':list(reversed([i for i in range(1,a+1)])),'B':[],'C':[]}
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
                y += 1
                hanoi(n - 1, b, a, c)
        if a <= 12 :
            print('A:',find_keys['A'])
            print('B:',find_keys['B'])
            print('C:',find_keys['C'])
            print('\n')
            hanoi(a)
        print('需要移动',str(2**a-1),'次。')

    elif mode == 9:
        from random import randint
        from time import sleep
        from copy import deepcopy
        WIDTH = 30
        HEIGHT = 10
        nextCells = []
        number = askinteger("项数选择","请问多少项？")
        for x in range(WIDTH):
            column = []
            for y in range(HEIGHT):
                if randint(0,1) == 1:
                    column.append('#')
                else:
                    column.append(' ')
            nextCells.append(column)
        for i in range(number):
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

    elif mode == 10 :
        a = askinteger("项数选择","请问多少项？")
        triangle = [[1], [1, 1]]
        for i in range(2, a):
            pre = triangle[i - 1]
            cul = [1]
            for j in range(i - 1):
                cul.append(pre[j] + pre[j + 1])
            cul.append(1)
            triangle.append(cul)
        if a < 21 :
            for i in range(a):
                s = "   " * (a - i - 1)
                for j in triangle[i]:
                    s = s + str(j).ljust(5) + " "
                print(s)
        else:
            print(triangle)

    elif mode == 11 :
        a = askinteger("项数选择","请问多少项？")
        for i in range(a):
            print(f'{int(i*(i-1)/2)}+{int(i*(i+1)/2)}={i*i}')

    else :
        if not mode == None or mode == '' :
            print("此模型正在开发中......")
except Exception as error:
    pass
else :
    input()
