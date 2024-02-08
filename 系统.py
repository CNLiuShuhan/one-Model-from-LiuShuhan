# -*- coding: utf-8 -*-
#开始->
from time import sleep
from tkinter.messagebox import showinfo
#<-初始化工作|进入时特效->#
def when_open():
    import turtle as t
    from tqdm import trange
    for i in trange(100) : pass
    for i in '''\
||==========---------->>
5432122 123456543211 221234
432122 11234567654321 22123
32122 1234567876543211 2212
2122 112345678987654321 221
122 123456789876543211 2212
2122 1123456787654321 22123
32122 12345676543211 221234
432122 112345654321 2212345
|█████████████████████████|
''' :
        print(i,end='',flush=True)
        sleep(0.005)
    t.title('sign')
    t.bgcolor('black')
    t.pencolor('cyan')
    t.goto(300,-30)
    t.speed('fastest')
    x = 200
    while x > 0 :
        t.right(x)
        t.forward(x * 3)
        x -= 1
    showinfo('information','''You can type "_help" ,\
"_copyright" , "_credits" or "_license" for more information.
Program started successfully.''')
    print('Loading',end='')
    for a in range(6) :
        print('.',end='',flush=True)
        sleep(0.2)
    print() ; t.bye()
#<-进入时特效|功能主体->#
def on_run():
    from subprocess import Popen
    from tkinter.simpledialog import askstring
    from os.path import isfile
    while True :
        path = askstring( None , "File's name?" )
        if path == '' or path is None :
            break
        elif isfile(f'./{path}.py') == True :
            try :
                f = Popen(['start',f'./{path}.py'],shell=True)
            except OSError:
                showinfo("We cannot found the runner(Python Software).")
            sleep(1)
        else :
            showinfo('error',"Sorry we can't opened the program.")
        a = askstring('Choose','''\
If you want to run next item , press Enter ;
if you want to quit,please answer "q" plus return.''')
        if a == "q" or a == "Q" or a == None :
            break
        elif a == '' :
            pass
        else :
            showinfo('problem','Please answer q or return,no else.')
#<-功能主体|退出时特效->#
def when_exit():
    print('exiting,please wait',end='')
    for a in range(6) :
        print('.',end='',flush=True)
        sleep(0.2)
#<-退出时特效|生成环境->#
def main():
    try :
        when_open()
        on_run()
        when_exit()
    finally :
        raise SystemExit
if __name__ == "__main__" :
    main()
#<-结束
