from turtle import* 
shape("turtle")
color("black","gold")
pensize(20)
bgcolor("skyblue")
setup(600,600)
speed(5)
#准备工作
for w in range(1,13):
  for i in range(0,2):
    forward(w*45)
    left(90)
forward(540)
dot(30)
penup()
goto(20,20)
#画迷宫
print("Don't cross the black line!")
speed(2)
def right():
    setheading(0)
    forward(45)
    y = ycor()
    x = xcor()
    if x==289.99999999999943 and y==-250.00000000000054:
      print("You are win!")
def left():
    setheading(180)
    forward(45)
def up():
    setheading(90)
    forward(45)
def down():
    setheading(270)
    forward(45)
listen()
onkeypress(up,"Up")
onkeypress(left,"Left")
onkeypress(down,"Down")
onkeypress(right,"Right")
#走迷宫
done()
