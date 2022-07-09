#Python Turtle Project

import turtle 

turtle.bgcolor("black") 
turtle.pensize(2,5) 
turtle.speed(0.5) 

color = ["red", "green", "yellow", "blue"]    #list of color used to draw animation

for x in range(9): 
    for i in color:
        turtle.color(i)
        turtle.circle(150)      #radius 150
        turtle.right(10)    # direction and angel 10 of animation
        
turtle.mainloop()
