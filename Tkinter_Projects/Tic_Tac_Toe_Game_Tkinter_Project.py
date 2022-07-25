#Python Tic Tac Toe game for two players

from tkinter import *
import random


def next_turn(row,column):
    
    global player
    
    #we're going to check to see if the button that we click on is empty
    if buttons[row][column]['text'] == "" and check_winner() is False:
        
        if player == players[0]: #first player
            buttons[row][column]['text'] = player
            
            #checking to see if after placing our text of our player on that button that we click if there is no winner then we're going to swap players
            if check_winner() is False:
                player = players[1] #second player
                #configuring our label so that it displays the next player's turn
                label.config(text=(players[1]+" turn"))
            
            #there is a winner
            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))
            
            #tie
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))
            
        #if its's not player one's turn player at index zero then it's our other player's turn player at index of one
        else:
            buttons[row][column]['text'] = player
            
            if check_winner() is False:
                player = players[0] #first player
                label.config(text=(players[0]+" turn"))
           
            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))
            
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))
        

def check_winner():
    
    #horizontal conditions
    for row in range(3):
        #if all of this buttons are the same and they are not equal to an empty space that means they're all the same 
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            #change color of winnings buttons
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
        
    #vertical win
    for column in range(3):       
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    
    #diagonal conditions
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    
    #check to see if there's any spaces remaining
    elif empty_spaces() is False:
        #color for tie
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="orange")
        return "Tie"
    else:
        return False

def empty_spaces():
    spaces = 9
    
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
                
    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player
    
    player = random.choice(players)
    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
#board
buttons = [[0,0,0],
           [0,0,0,],
           [0,0,0,]]

#display whose turn it is
label = Label(text= player + " turn",font=('consolas',40))
label.pack(side="top")

#button to start new game
reset_button = Button(text="Restart",font=('consolas',20),command=new_game)
reset_button.pack(side="top")


frame = Frame(window)
frame.pack()

#add a button to each spot
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame,text="",font=('consolas',40),width=5,height=2,
                                      command=lambda row=row,column=column:next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)


window.mainloop()