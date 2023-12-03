from turtle import *
setheading(90)
penup()
setpos(0,-250)
pendown()
def FractalTreeColor(length, level):
    """
    Generates a fractal tree with colored branches.

    Parameters:
    - length (int): The length of the branch.
    - level (int): The level of recursion for generating the tree.

    Returns:
    - None
    """
    pensize(length/10)
    if length < 20:
        pencolor('green')
    else:
        pencolor('brown')
    speed(0)
    if level > 0:
        fd(length)
        rt(30) # rigth turn 30 degrees
        FractalTreeColor(length*0.7, level-1)
        lt(90) # left  turn 90 degrees
        FractalTreeColor(length*0.5, level-1)
        rt(60) # right turn 60 degrees
        penup()
        bk(length)
        pendown()
FractalTreeColor(200, 10)