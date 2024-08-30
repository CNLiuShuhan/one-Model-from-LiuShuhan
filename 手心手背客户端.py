from asyncio import *
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo
async def main():
    while True:
        window = Tk()
        window.title("请输入")
        window.geometry('300x120')
        Label(window, text="服务器的IP地址(不含端口)").pack()
        E1 = Entry(window, show=None)
        E1.pack()
        Label(window, text="服务器的端口").pack()
        E2 = Entry(window, show=None)
        E2.pack()
        port = ''
        def on_button_click():
            global ip
            nonlocal port
            ip = E1.get()
            port = E2.get()
            window.destroy()
        Button(window, text="输入完成", command=on_button_click).pack()
        window.mainloop()
        try : port = int(port)
        except : exit()
        try : reader,writer = await open_connection(ip, port)
        except : pass
        else : break
    window = Tk()
    window.title("请输入")
    window.geometry('300x120')
    Label(window, text="你的名字").pack()
    E1 = Entry(window, show=None)
    E1.pack()
    def on_button_click():
        global name
        name = E1.get().encode()
        window.destroy()
    Button(window, text="输入完成", command=on_button_click).pack()
    window.mainloop()
    writer.write(name)
    await writer.drain()
    running = True
    while running:
        running = False
        if not (await reader.read(100)) : raise Exception("server exit")
        window = Tk()
        window.title("手心手背")
        window.geometry('300x120')
        def shouxin():
            global answer
            answer = 0
            print("手心")
            window.destroy()
        def shoubei():
            global answer
            answer = 1
            print("手背")
            window.destroy()
        Button(window, text="手心", command=shouxin).pack()
        Button(window, text="手背", command=shoubei).pack()
        window.mainloop()
        writer.write(int.to_bytes(answer))
        await writer.drain()
        result = int.from_bytes(await reader.read(100))
        if result == 2 : showinfo("手心手背","对等")
        elif result == answer : showinfo("手心手背","你赢了")
        else : showinfo("手心手背","你输了")
        window = Tk()
        window.title("手心手背")
        window.geometry('300x120')
        Label(window, text="是否继续").pack()
        def on_button_click():
            nonlocal running
            window.destroy()
            running = True
        Button(window, text="是", command=on_button_click).pack()
        Button(window, text="否", command=window.destroy).pack()
        window.mainloop()
    writer.close()
    await writer.wait_closed()
try : run(main())
except : showinfo("手心手背","连接结束")
