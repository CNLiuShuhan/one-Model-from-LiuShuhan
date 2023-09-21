print("""
让我给你讲个故事吧,\n从前有座山，山里有座庙，庙里有个老和尚，老和尚在给小和尚讲故事。\n讲的什么故事呢？(加下一章，请按下回车。）""")
def jiang():
    print("老和尚讲的是：从前有座山,山里有座庙,庙里有个老和尚,老和尚在给小和尚讲故事,讲的是什么呢？")
from turtle import*
setup(22,22)
title("请勿关闭")
listen()
onkeypress(jiang,"Return")
done()
