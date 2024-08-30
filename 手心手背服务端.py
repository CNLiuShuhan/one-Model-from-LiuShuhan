from tkinter import *
from asyncio import *
from tkinter.ttk import *
from tkinter.messagebox import showinfo
statu = Event()
statu.set()
name_list = []
connect_list = []
async def connection(reader,writer):
    try:
        await statu.wait()
        name_list.append((await reader.read(100)).decode())
        while True:
            n = yield
            writer.write(n)
            await writer.drain()
            n = yield (await wait_for(reader.read(100),5))
            writer.write(n.to_bytes())
            await writer.drain()
    finally:
        writer.close()
        await writer.wait_closed()
async def connect(reader,writer):
    try:
        connected = connection(reader,writer)
        await anext(connected)
        connect_list.append(connected)
    except : pass
async def main():
    window = Tk()
    window.title("请输入")
    window.geometry('300x120')
    Label(window, text="服务器的IP地址(不含端口)").pack()
    E1 = Entry(window, show=None)
    E1.pack()
    def on_button_click():
        global ip
        ip = E1.get()
        window.destroy()
    Button(window, text="输入完成", command=on_button_click).pack()
    window.mainloop()
    server = await start_server(connect, ip)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    async with server:
        task = create_task(server.serve_forever())
        running = True
        while running:
            running = False
            window = Tk()
            window.title("接听中")
            window.geometry('300x120')
            Label(window, text=f'开始接听:{addrs}').pack()
            Button(window, text="停止接听", command=window.destroy).pack()
            window.mainloop()
            await sleep(1)
            statu.clear()
            if not name_list : exit()
            showinfo('接听关闭',str(name_list))
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
            wtbls =await gather(*[i.asend(b"game start") for i in connect_list],
                                return_exceptions=True)
            window.mainloop()
            results = [int.from_bytes(i) for i in wtbls if type(i) == bytes]
            if not results : raise Exception("no connection")
            results.append(answer)
            result = sum(results)/len(results)
            if result > 0.5 : result = 1
            elif result < 0.5 : result = 0
            elif result == 0.5 : result = 2
            await gather(*[i.asend(result) for i in connect_list],
                         return_exceptions=True)
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
                statu.set()
            Button(window, text="是", command=on_button_click).pack()
            Button(window, text="否", command=window.destroy).pack()
            window.mainloop()
        await gather(*[i.athrow(Exception("exit")) for i in connect_list],
                     return_exceptions=True)
        task.cancel()
try : run(main())
except : showinfo("手心手背","连接结束")
