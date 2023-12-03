from turtle import *
speed(0)
def kochCurve(length, level):
    if level == 0:
        forward(length)
        return
    kochCurve(length/3, level-1)
    lt(60)
    kochCurve(length/3, level-1)
    rt(120)
    kochCurve(length/3, level-1)
    lt(60)
    kochCurve(length/3, level-1)
kochCurve(300,4)