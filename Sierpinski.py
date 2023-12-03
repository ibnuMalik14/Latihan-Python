import turtle

def draw_sierpinski(length, depth):
    """
    Recursively draws a Sierpinski triangle using turtle graphics.

    Parameters:
        length (float): The length of the sides of the triangle.
        depth (int): The depth or level of recursion to draw the triangle.

    Returns:
        None
    """
    if depth == 0:
        turtle.begin_fill()
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
        turtle.end_fill()
    else:
        draw_sierpinski(length / 2, depth - 1)
        turtle.forward(length / 2)
        draw_sierpinski(length / 2, depth - 1)
        turtle.backward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        draw_sierpinski(length / 2, depth - 1)
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)


turtle.speed(0)
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
turtle.color('black')

draw_sierpinski(400, 4)

turtle.hideturtle()
turtle.done()