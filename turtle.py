from turtle import *
pencolor('red')
penup()
goto(-200,0)#设置画笔开始画的位置
speed(0)#加速
pendown()
a=15#设置太阳花角的度数，必须能被360整除
fillcolor('yellow')#填充颜色 黄色
begin_fill()#开始填充
for i in range(int(360/a)):#循环次数
  forward(400)#太阳花宽度
  left(180-a)
end_fill()#结束填充