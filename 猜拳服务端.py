import asyncio
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    writer.write(message.encode())
    await writer.drain()
    showinfo('猜拳服务端',f"开始连接:{addr!r}")
    await asyncio.sleep(1)
    running = True
    while running:
        window = Tk()
        window.title("猜拳服务端")
        window.geometry('250x100')
        def on_button_clicked_0():
            global answer_1,data_1
            answer_1 = "石头"
            data_1 = 0
            window.destroy()
        def on_button_clicked_1():
            global answer_1,data_1
            answer_1 = "剪刀"
            data_1 = 1
            window.destroy()
        def on_button_clicked_2():
            global answer_1,data_1
            answer_1 = "布"
            data_1 = 2
            window.destroy()
        Label(window, text='请问你出"石头"、"剪刀"还是"布"呢？').pack()
        Button(window, text="石头", command=on_button_clicked_0).pack(side='left')
        Button(window, text="剪刀", command=on_button_clicked_1).pack(side='left')
        Button(window, text="布", command=on_button_clicked_2).pack(side='left')
        window.mainloop()
        try : answer_2,data_2 = (await asyncio.wait_for(
            reader.read(100),10)).decode().split(",")
        except : raise KeyboardInterrupt
        data_2 = int(data_2)
        match (data_1,data_2):
            case (0,0) : status = 'same'
            case (1,1) : status = 'same'
            case (2,2) : status = 'same'
            case (0,1) : status = 'win'
            case (1,2) : status = 'win'
            case (2,0) : status = 'win'
            case (1,0) : status = 'lose'
            case (2,1) : status = 'lose'
            case (2,1) : status = 'lose'
        writer.write((status+','+answer_1).encode())
        translate = {'win':'你赢了','lose':'你输了','same':'平局'}
        showinfo('猜拳服务端',f"{translate[status]}{(answer_1,answer_2)}")
        print(f"{translate[status]}{(answer_1,answer_2)}")
        await writer.drain()
        window = Tk()
        window.title("猜拳服务端")
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
    writer.close()
    await writer.wait_closed()
    showinfo('猜拳服务端',"断开连接")
async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1')
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    showinfo('猜拳服务端',f'开始接听:{addrs}')
    async with server:
        try : await server.serve_forever()
        except : showinfo('猜拳服务端',"停止服务")
try : asyncio.run(main())
except : pass
