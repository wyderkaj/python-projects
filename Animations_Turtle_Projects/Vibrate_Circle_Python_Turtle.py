#Vibrate Circle using Python turtle in pycharm

import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("turquoise")
a = 0
b = 0
t.speed(0)

# setting the animation to be drawn in the center of the screen
t.penup()
t.goto(0,200)
t.pendown()

while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 210:
        break
    t.hideturtle()

turtle.done()