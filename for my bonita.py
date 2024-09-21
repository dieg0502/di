import math
import turtle

turtle.bgcolor("black")
turtle.pencolor("black")
turtle.shape("triangle")
turtle.speed(0)
turtle.fillcolor("orangered")

# Pre-calculate constant angle
phi = 137.508 * (math.pi / 180.0)

# Turn off screen updates for faster drawing
turtle.tracer(0, 0)

for i in range(180 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()

    if i < 160:
        turtle.stamp()
    else:
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.left(-5)
        turtle.circle(500, 25)
        turtle.right(500, 25)  # Removed redundant angle adjustment
        turtle.end_fill()

# Update the screen to show the final drawing
turtle.update()

turtle.hideturtle()
turtle.done()