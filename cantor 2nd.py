from turtle import *

def cantor(x, y, length):
    if length > 5:
        penup()
        pensize(3)
        pencolor('blue')
        setpos(x, y)
        pendown()
        fd(length)
        
        # Remove two middle segments
        y -= 60
        cantor(x, y, length / 5)  # Draw the left segment
        cantor(x + 4 * length / 5, y, length / 5)  # Draw the right segment
        
        # Continue with the remaining segments
        cantor(x + 2 * length / 5, y, length / 5)
        cantor(x + 3 * length / 5, y, length / 5)
        
        penup()
        setpos(x, y + 60)

cantor(-400, 200, 800)