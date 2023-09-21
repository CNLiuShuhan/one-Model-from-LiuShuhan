name = input("我叫Python，你叫什么呢？")
answer = input("我很高兴认识你,"+name+"。你愿意学习Python我吗？请回答”愿意”或”不愿意”。")
if answer == "愿意" or answer=="yes":
    print("真棒，我很开心，那我们开始吧！在开始之前，我送你个东西：")
    import math
    from turtle import*
    hideturtle()
    pensize(1.5)
    fillcolor("pink")
    setup(500,500)
    begin_fill() 
    e=0.99
    for i in range(0,630):
        e=e+0.01
        r=100*(1-math.sin(e))
        y=r*math.sin(e)
        x=r*math.cos(e)
        goto(x,y)
    end_fill()
elif answer =="不愿意" or answer=="no":
    answer=input("有点小遗憾，真的不尝试一下吗？请回答'那好吧'或'算了吧'？")
    if answer == "那好吧" or answer=="ok":
        print("真棒，我很开心，那我们开始吧！")
    elif answer =="算了吧" or answer=="no":
        print("好吧,"+name+",这可有点遗憾哦。")
    else:
        print("重新运行程序，请按要求回答'那好吧'或'算了吧'。")
else:
    print("重新运行程序，请按要求回答‘愿意’或者‘不愿意’。")
