#chess board

import turtle

t = turtle.Turtle()

#making  one square
def box(ln):  
    for i in range(4):
        t.forward(ln)
        t.left(90)

t.speed(0.5)
x = 0
y = 0
count = 2

while True:
    t.goto(x,y)
    t.pendown()
    x += 20
    t.begin_fill()  #making colors
    if count % 2 == 0:
        t.fillcolor("black")
    else:
        t.fillcolor("white")    
    count += 1
    box(20)
    t.end_fill()
    if x >= 20*8:
        x = 0
        y += 20
        t.penup()
        count += 1
        
    if y >= 20*8:
        break

t.hideturtle()
turtle.done()
