#Simple Animmation in Python Turtle 
import turtle

#create turtle
t= turtle.Turtle()
s= turtle.Screen()
s.bgcolor("black")
t.speed(0)
c= 0
t.pencolor("white")

#drawing animation
while True:
    for i in range(4):
        t.forward(80)
        t.left(90)
    t.left(5)
    c +=1
    if c>=360/5:
        break
    
t.hideturtle()

turtle.done()