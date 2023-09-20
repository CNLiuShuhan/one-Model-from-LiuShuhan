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
        from turtle import *
        try:
            hideturtle()
            a,e=100,0.99
            fillcolor("pink")
            begin_fill()
            pensize(1.5)
            for i in range(0,630):
                e=e+0.01
                r=a*(1-math.sin(e))
                y=r*math.sin(e)
                x=r*math.cos(e)
                goto(x,y)
            end_fill()
        except Terminator :
            pass

    elif mode == 7 :
        import re,math
        from itertools import combinations, combinations_with_replacement
        from tqdm import tqdm
        from treelib import Tree
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
                    yield [
                            [exp_list[g1] for g1 in group1],
                            [exp_list[g2] for g2 in group2]
                            ]
        times = int(input("最大数: "))
        tree = Tree()
        solver = Solver()
        tree.create_node(f"1~{times}", "root")
        for i in tqdm(combinations_with_replacement(range(1, times + 1), 4)):
            tree.create_node(i, i, parent="root")
            solution = solver.solution(i)
            if not solution:
                tree.create_node("没有解", None, parent=i)
                continue
            for j in solution:
                tree.create_node(j.replace("*", "×").replace("/", "÷"), j, parent=i)
        print(tree)

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

    else :
        print("No this mode.")
except TypeError :
    print("Please restart and don't click cancel.")
