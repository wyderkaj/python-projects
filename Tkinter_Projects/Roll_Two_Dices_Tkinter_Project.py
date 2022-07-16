#dice roll gui 
#Program for throwing two dice

from tkinter import *
import random

root = Tk()
root.geometry("700x450")
root.title("Roll Dice")
root.configure(bg="black")

label = Label(root,text="",font=("times",300))

def roll():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685'] #Unicode Character 'Die Face- ' This all indicate 1,2,3,4,5,6 dots
    label.configure(text=f'{random.choice(dice)}{random.choice(dice)}',bg="black",fg="white")
    label.pack()

button = Button(root,text="Let's roll...",width=40,height=5,font=("arial",10,"bold"),bg="white",bd=2,command=roll)
button.pack(padx=10,pady=10)

root.mainloop()