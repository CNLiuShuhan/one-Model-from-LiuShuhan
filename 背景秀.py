from turtle import*
setup(1000,400)
shape("turtle")
fillcolor("white")
pensize(5)
penup()
goto(-400,0)
pendown()
colours=["black","purple","blue","green","yellow","pink","orange","red"]
du=[-400,-300,-200,-100,0,100,200,300]
for color in colours:
  pencolor(color)
  forward(100)
#画彩虹桥
penup()
goto(450,0)
pencolor("black")
def setcolor():
  x = xcor()
  for i in range(0,8):
    if du[i] < x < du[i]+100:
      bgcolor(colours[i])
    if x==450 or x==-450:
      bgcolor("white")
#走彩虹桥的准备
def moveright():
  setheading(0)
  x = xcor()
  if x<450:
    forward(100)
    setcolor()
def moveleft():
  setheading(180)
  x = xcor()
  if x>-450:
    forward(100)
    setcolor()
listen()
onkeypress(moveright,"Right")
onkeypress(moveleft,"Left")
#在彩虹桥上走起来
done()
