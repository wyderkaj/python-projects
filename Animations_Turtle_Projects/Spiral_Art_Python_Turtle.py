#spiral art using python and turtle

import turtle

#define colors
colors = ["red", "yellow", "green", "purple", "blue", "orange"]

#set up the turtle and set the background color
t = turtle.Turtle()
turtle.bgcolor("black")

#setting the animation
for x in range(200):
    #set the color
    t.pencolor(colors[x%6])
    #set the width
    t.width(x/100+1)
    #move the turtle
    t.forward(x)
    #rotate the turtle
    t.left(59)
    
