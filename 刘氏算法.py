from tkinter.simpledialog import askinteger
from sys import argv
DEBUG = False
try :
    if len(argv) > 1 :
        mode = int(argv[1])
    else : mode = askinteger("模式选择","""这是一个数学模型，目前有
1完全数、2质数、3从一开始的连续自然数之和、4斐波那契数列、5因数、6表白工具、7二十四点、
8汉诺塔、9Conway生命游戏、10杨辉三角和11正方形及三角形数12A*寻路13解数独十三种功能，
请选择其中一个输入(1-13)：""")

    if mode == 1 :
        a,b,j = askinteger("范围选择","在多少以内？"),1,1
        while b < a :
            c = 0
            for i in range(1,b) :
                if b % i == 0 :
                    c += i
            if c == b :
                print(b,end=' ')
            j += 1
            b += j

    elif mode == 2 :
        from math import sqrt
        a = askinteger("范围选择","在多少以内？")
        b,c,d = list(range(2,a)),2,[]
        while c*c <= b[-1]:
            d.append(c)
            for i in b:
                if i % c == 0 : b.pop(b.index(i))
            c = b[0]
        print(*(d+b))

    elif mode == 3 :
        a,c = askinteger("范围选择","在多少以内？"),0
        for j in range(1,a):
            c += j
            print(f'第{j}项(从一加到{j})是:{c}')
        print("结束")

    elif mode == 4 :
        a,b,c,f = askinteger("范围选择","在多少以内？"),1,0,[]
        while c < a:
            f.append(c)
            c,b = b,c+b
        print(f)

    elif mode == 5 :
        a,b,n = askinteger("范围选择","在多少以内？"),1,0
        for j in range(1,a):
            c = []
            for i in range(1,b+1):
                if b%i == 0 :
                    c.append(i)
            if len(c) > n:
                n = len(c)
                print(f'{j}:{c} {n}--|>')
            else:
                print(f'{j}:{c} {len(c)}')
            b += 1

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
            a = input('请用本格式("+"替换为空格)：第一个数字+第二个数字+第三个数字+第四个数字\t：')
            if re.match(findobj,a):
                x = solver.solution(tuple(str(no) for no in a.split()))
                print(x,len(x))
            elif a == 'close' or a == 'quit' or a == 'exit':
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
        a = askinteger("项数选择","请问多少项？")
        for x in range(WIDTH):
            column = []
            for y in range(HEIGHT):
                if randint(0,1) == 1:
                    column.append('#')
                else:
                    column.append(' ')
            nextCells.append(column)
        for i in range(a):
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

    elif mode == 12 :
        WIDTH = 10
        HEIGHT = 10
        START = (0,0)
        END = (WIDTH-1 , HEIGHT-1)
        MAZE = [[int(j) for j in (input(f'第{i+1}行:')[:10])] for i in range(10)]
        MAZE[START[1]][START[0]] = 0
        MAZE[END[1]][END[0]] = 0
        def a_star_search(start, end):
            open_list = []
            close_list = []
            open_list.append(start)
            while len(open_list) > 0:
                current_grid = find_min_gird(open_list)
                open_list.remove(current_grid)
                close_list.append(current_grid)
                neighbors = find_neighbors(current_grid, open_list, close_list)
                for grid in neighbors:
                    if grid not in open_list:
                        grid.init_grid(current_grid, end)
                        open_list.append(grid)
                for grid in open_list:
                    if (grid.x == end.x) and (grid.y == end.y):
                        return grid
            return None
        def find_min_gird(open_list=None):
            if open_list is None:
                open_list = []
            temp_grid = open_list[0]
            for grid in open_list:
                if grid.f < temp_grid.f:
                    temp_grid = grid
            return temp_grid
        def find_neighbors(grid, open_list=None, close_list=None):
            if close_list is None:
                close_list = []
            if open_list is None:
                open_list = []
            grid_list = []
            if is_valid_grid(grid.x, grid.y - 1, open_list, close_list):
                grid_list.append(Grid(grid.x, grid.y - 1))
            if is_valid_grid(grid.x, grid.y + 1, open_list, close_list):
                grid_list.append(Grid(grid.x, grid.y + 1))
            if is_valid_grid(grid.x - 1, grid.y, open_list, close_list):
                grid_list.append(Grid(grid.x - 1, grid.y))
            if is_valid_grid(grid.x + 1, grid.y, open_list, close_list):
                grid_list.append(Grid(grid.x + 1, grid.y))
            return grid_list
        def is_valid_grid(x, y, open_list=None, close_list=None):
            if close_list is None:
                close_list = []
            if open_list is None:
                open_list = []
            if x < 0 or x >= len(MAZE) or y < 0 or y >= len(MAZE[0]):
                return False
            if MAZE[x][y] == 1:
                return False
            if contain_grid(open_list, x, y):
                return False
            if contain_grid(close_list, x, y):
                return False
            return True
        def contain_grid(grids, x, y):
            for grid in grids:
                if (grid.x == x) and (grid.y == y):
                    return True
            return False
        class Grid:
            def __init__(self, x, y):
                self.x = x
                self.y = y
                self.f = 0
                self.g = 0
                self.h = 0
                self.parent = None
            def init_grid(self, parent, end):
                self.parent = parent
                if parent is not None:
                    self.g = parent.g + 1
                else:
                    self.g = 1
                self.h = abs(self.x - end.x) + abs(self.y - end.y)
                self.f = self.g + self.h
        start_grid = Grid(*START)
        end_grid = Grid(*END)
        result_grid = a_star_search(start_grid, end_grid)
        path = []
        while result_grid is not None:
            path.append(Grid(result_grid.x, result_grid.y))
            result_grid = result_grid.parent
        for i in range(0, len(MAZE)):
            for j in range(0, len(MAZE[0])):
                if contain_grid(path, i, j):
                    print("*  ", end='')
                else:
                    print(str(MAZE[i][j]) + "  ", end='')
            print()

    elif mode == 13:
        from copy import deepcopy
        from random import choice
        whole_set = {1,2,3,4,5,6,7,8,9}
        answers = []
        inputa = []
        i = 1
        while True:
            entry = [int(j) for j in input(f'第{i}行:')[:9]]
            if len(entry) < 9 : i -= 1
            else : inputa.append(entry)
            i += 1
            if i > 9 : break
        def check(a,/):
            rows = [set(i) for i in a]
            columns = [set(i) for i in zip(*a)]
            blocks = [set([i for j in a[y:y+3] for i in j[x:x+3]])
                      for y in range(0,7,3) for x in range(0,7,3)]
            return {(x,y):whole_set-(rows[y]|columns[x]|blocks[x//3+y//3*3])
                    for y in range(9) for x in range(9) if a[y][x] == 0}
        def main(*,locala):
            while True:
                point = check(locala)
                if point == {}:
                    if len(answers) < 10 :
                        answers.append(deepcopy(locala))
                    else : raise Exception('"Answers" is full.')
                for i,a in point.items():
                    if len(a) == 0 : return
                    elif len(a) == 1 :
                        locala[i[1]][i[0]] = a.pop()
                        break
                else : break
            for i,a in point.items():
                while True:
                    change = choice(list(a))
                    a -= {change}
                    locala[i[1]][i[0]] = change
                    main(locala = deepcopy(locala))
                    if not a : return
        try:
            rows = [i for i in inputa]
            columns = [list(i) for i in zip(*inputa)]
            blocks = [[i for j in inputa[y:y+3] for i in j[x:x+3]]
                      for y in range(0,7,3) for x in range(0,7,3)]
            for y in range(9):
                for x in range(9):
                    i = inputa[y][x]
                    row = deepcopy(rows[y])
                    row.remove(i)
                    column = deepcopy(columns[x])
                    column.remove(i)
                    block = deepcopy(blocks[x//3+y//3*3])
                    block.remove(i)
                    if i != 0 and (i in row or i in column or i in block):
                        raise Exception("抱歉，数独存在问题")
            print("输入:")
            for i in inputa : print(i)
            try : main(locala = inputa)
            except Exception : pass
            if not answers : raise Exception("抱歉，数独存在问题")
            for i,outputa in enumerate(answers,start=1):
                print(f"输出{i}:")
                for j in outputa : print(j)
        except Exception as error : print(error)

    else :
        if not mode == None or mode == '' :
            print("此模型正在开发中......")
except Exception as error:
    if DEBUG is True:
        raise error
    elif DEBUG is False:
        pass
    else:
        assert False
else :
    input()
