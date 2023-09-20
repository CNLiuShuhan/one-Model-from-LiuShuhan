import turtle as t
from time import sleep

def when_open():
    from tkinter.messagebox import showinfo
    from tqdm import tqdm
    for i in tqdm(range(100)) : sleep(0.01)
    for i in '''||==========---------->>
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
        print(i,end='')
        sleep(0.0036)
    while True :
        try :
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
            break
        except Exception as error : pass
    showinfo('information',
    '''Liushuhan all rights reserved(by Python).
Now program's status is good,started successfully.''')
    print('Loading',end='',flush=True)
    for a in range(6) :
        print('.',end='',flush=True)
        sleep(0.25)
        if a == 0 : del showinfo
        if a == 1 : del tqdm
        if a == 2 : del i,x
    print()#<-进入时特效|运行项目->#

def on_run():
    from tkinter.messagebox import showerror
    from runpy import run_path
    from importlib import reload
    while True :
        if t.TurtleScreen._RUNNING : t.bye()
        reload(t)
        path = t.textinput('Openfile',"File's name?")
        try :
            if not (path == '' or path is None) : run_path(f'./{path}.py')
            else :
                t.bye()
                break
        except FileNotFoundError as error :
            showerror("Can't Open",
f'Cannot find the "{path}",please try again.')
        except Exception as error :
            showerror('Error in Running',
f'''During run the "{path}",have a problem:{error}.
please try again.''')
        else :
            try : a = input('If you want to run next item,press Enter;\n'
'if you want to quit,please answer "q".')
            except KeyboardInterrupt as error : pass
            if a == "q" or a == "Q" :
                t.bye()
                break
            elif a == '' : pass
            else : print('Must answer q or return,no else.')
        finally : sleep(0.3)#<-运行项目|退出时特效->#

def when_exit():
    print('exiting,please wait',end='')
    for a in range(6) :
        print('.',end='',flush=True)
        sleep(0.25)
def main():
    try :
        when_open()
        on_run()
        when_exit()
    except BaseException as error:
        return error
    else :
        return True
    finally :
        raise SystemExit

if __name__ == "__main__":
    main()
