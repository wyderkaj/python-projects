
import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.title("3D Cube")
s.screensize(800,500, bg="black")
t.pencolor("white")
t.pensize(3)

def square():
    for i in range(4):
        t.forward(100)
        t.left(90)
 
def cube():       
    square()
    t.left(45)   #every, left and right- change of direction
    t.forward(100)
    t.right(45) 
    square()
    t.left(90)  
    t.forward(100)
    t.left(90+45)   
    t.forward(100)
    t.right(45+180)
    t.forward(100)
    t.left(45)
    t.forward(100)
    t.right(45+90)
    t.forward(100)
    t.right(90-45)
    t.forward(100)

cube()
turtle.done()