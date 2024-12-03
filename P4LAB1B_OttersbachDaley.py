# Daley Ottersbach
# 12/3/2024
# P4LAB1B
# Draws initials

import turtle

turtle.speed(0)
turtle.pencolor((1.0, 0.5, 0.1))
turtle.setheading(-90)

turtle.forward(100)
turtle.setheading(0)
turtle.circle(50, 180)

turtle.penup()
turtle.setpos(turtle.xcor() + 110, turtle.ycor())
turtle.pendown()
turtle.circle(50, 360)