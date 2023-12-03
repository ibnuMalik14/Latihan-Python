from turtle import *
speed(0)
def cantor(x,y, length):
    if length > 5:
        penup()
        pensize(3)
        pencolor('blue')
        setpos(x, y)
        pendown()
        fd(length)
        y -= 60
        cantor(x, y, length / 3)
        cantor(x+2*length/3, y, length / 3)
        penup()
        setpos(x, y + 60)
cantor(-400, 200, 800)