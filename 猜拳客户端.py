import asyncio
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
async def tcp_echo_client():
    window = Tk()
    window.title("猜拳客户端")
    window.geometry('300x120')
    Label(window, text="请输入服务器的IP地址(不含端口)").pack()
    E1 = Entry(window, show=None)
    E1.pack()
    Label(window, text="请输入服务器的端口").pack()
    E2 = Entry(window, show=None)
    E2.pack()
    def on_button_click():
        global ip,port
        ip = E1.get()
        port = int(E2.get())
        window.destroy()
    Button(window, text="输入完成", command=on_button_click).pack()
    window.mainloop()
    async with asyncio.timeout(2):
        reader, writer = await asyncio.open_connection(ip, port)
        message = 'Hello world!'                                 
        writer.write(message.encode())
        await writer.drain()
        data = await reader.read(100)
    if message == data.decode():
        showinfo('猜拳客户端',"开始连接")
        running = True
        while running:
            window = Tk()
            window.title("猜拳客户端")
            window.geometry('250x100')
            def on_button_clicked_0():
                global data_2,answer_2
                answer_2 = "石头"
                data_2 = "0"
                window.destroy()
            def on_button_clicked_1():
                global data_2,answer_2
                answer_2 = "剪刀"
                data_2 = "1"
                window.destroy()
            def on_button_clicked_2():
                global data_2,answer_2
                answer_2 = "布"
                data_2 = "2"
                window.destroy()
            Label(window,text='请问你出"石头"、"剪刀"还是"布"呢？').pack()
            Button(window, text="石头",
                   command=on_button_clicked_0).pack(side='left')
            Button(window, text="剪刀",
                   command=on_button_clicked_1).pack(side='left')
            Button(window, text="布",
                   command=on_button_clicked_2).pack(side='left')
            window.mainloop()
            writer.write((answer_2+','+data_2).encode())
            await writer.drain()
            status,answer_1 = (await asyncio.wait_for(
                reader.read(100),10)).decode().split(',')
            translate = {'win':'你输了','lose':'你赢了','same':'平局'}
            showinfo('猜拳客户端',f"{translate[status]}{(answer_2,answer_1)}")
            print(f"{translate[status]}{(answer_2,answer_1)}")
            window = Tk()
            window.title("猜拳客户端")
            window.geometry('250x100')
            Label(window, text="是否继续").pack()
            def on_button_clicked_no():
                nonlocal running
                running = False
                window.destroy()
            Button(window, text="是", command=window.destroy).pack(anchor='s')
            Button(window, text="否", command=on_button_clicked_no
                   ).pack(anchor='s')
            window.mainloop()
    else:
        showinfo('猜拳客户端',"连接异常")
    writer.close()
    await writer.wait_closed()
    showinfo('猜拳客户端','断开连接')
try:
    asyncio.run(tcp_echo_client())
except:
    showinfo('猜拳客户端','连接结束')
