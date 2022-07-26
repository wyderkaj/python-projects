#Snake game 

from tkinter import *
import random


#Game settings
GAME_WIDTH = 650
GAME_HEIGHT = 650
SPEED = 100
SPACE_SIZE = 25
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"


class Snake:
    
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):      #list of coordinates
            self.coordinates.append([0,0])  #coordinates at the start of the game 

        #create squares, the head of the snake will be in the top left corner
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tag= "snake")
            self.squares.append(square)

class Food:
    
    def __init__(self):
        #range between 0 and, game board/space size, this should be exclusive so -1, convert this to pixels *space size
        x = random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x,y]
        
        #draw food object on canvas, starting corner where x and y is and an ending  x and y plus our space size  
        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    
    x, y = snake.coordinates[0]     #unpack the head of the snake, the coordinates will be stored in x and y
    
    if direction == "up":   
        y -= SPACE_SIZE     
    elif direction == "down":
        y += SPACE_SIZE   
    elif direction == "left":    
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
        
    snake.coordinates.insert(0, (x,y))  #update the coordinates for the head of snake
    
    #create a new graphic for the head of the snake square, 
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    
    snake.squares.insert(0, square)     #update snake list of squares

    if x == food.coordinates[0] and y == food.coordinates[1]:   #when head meet food object
        global score
        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")   #delete food object
        food = Food()   #create new food object
        
    else:       
        del snake.coordinates[-1]   #delete the last body part of snake when it did not eat a food object   
        canvas.delete(snake.squares[-1])    #update canvas       
        del snake.squares[-1]   #delete last element of snake list of squares
        
    #collision
    if check_collisions(snake):
        game_over()
    else: 
        window.after(SPEED, next_turn, snake, food) #call the next turn function again for the next turn


def change_direction(new_direction):
    global direction
    
    if new_direction == 'left':
        if direction != 'right': #snake can't go backwards and do a 180 degree turn
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake): 
    x, y = snake.coordinates[0]
    
    #check if we cross the left or right border, and up and down
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    #if snake touches its tail or another body part
    for body_part in snake.coordinates[1:]: #everything after the head of the snake
        if x == body_part[0] and y == body_part[1]:
            return True
    
    return False
    
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70,"bold"),text="GAME OVER",fill="red",tag="gameover")


#game window
window = Tk()
window.title("Snake Game")
window.resizable(False,False)

#Score label
score = 0
direction = 'down'

label = Label(window,text="Score: {}".format(score),font=('consolas',40))
label.pack()

#canvas
canvas = Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()


#control keys
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))


snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()