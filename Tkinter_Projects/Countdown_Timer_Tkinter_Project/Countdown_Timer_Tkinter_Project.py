from tkinter import *
from playsound import playsound
import time

root = Tk()
root.title("Timer")
root.geometry("400x600")
root.config(bg="black")
root.resizable(False,False)

heading = Label(root, text="Timer", font="Arial 32 bold", bg="black", fg= "#23aea3")
heading.pack(pady=10)


#clock
Label(root, font=("Arial",15,"bold"),text="Current time:",bg="#e4f9f6").place(x=65,y=70)

def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000,clock)
        
current_time=Label(root,font=("arial",15,"bold"),text="",fg="black",bg="white")
current_time.place(x=190,y=70)
clock()


#timer
hrs = StringVar()
Entry(root, textvariable=hrs,width=2,font="arial 50",bg="black",fg="white",bd=0).place(x=30,y=155)
hrs.set("00")

min = StringVar()
Entry(root, textvariable=min,width=2,font="arial 50",bg="black",fg="white",bd=0).place(x=150,y=155)
min.set("00")

sec = StringVar()
Entry(root, textvariable=sec,width=2,font="arial 50",bg="black",fg="white",bd=0).place(x=270,y=155)
sec.set("00")

Label(root,text="hours",font="arial 12",bg="black",fg="white").place(x=105,y=200)
Label(root,text="min",font="arial 12",bg="black",fg="white").place(x=225,y=200)
Label(root,text="sec",font="arial 12",bg="black",fg="white").place(x=345,y=200)

#timing function
def Timer():
    times=int(hrs.get())*3600+int(min.get())*60+int(sec.get())
    
    while times > -1:
        minute, second=(times//60, times%60)
        hour = 0
        if minute > 60:
            hour, minute=(minute//60,minute%60)
            
        sec.set(second)
        min.set(minute)
        hrs.set(hour)
        
        root.update()
        time.sleep(1)
        
        if (times==0):
            playsound("ringtone.wav")
            sec.set("00")
            min.set("00")
            hrs.set("00")
            
        times -=1

#Functions that automatically set the time for the selected activity
def brush():
    hrs.set("00")
    min.set("02")
    sec.set("00")
    
def face():
    hrs.set("00")
    min.set("15")
    sec.set("00")

def eggs():
    hrs.set("00")
    min.set("10")
    sec.set("00")
    
button = Button(root,text="Start",bg="#23aea3",bd=0,fg="white",width=20,height=2,font="arial 10 bold",command=Timer)
button.pack(padx=5,pady=40,side=BOTTOM)

Image1 = PhotoImage(file="brush.png")
button1 = Button(root,image=Image1,bg="black",bd=0,command=brush)
button1.place(x=7,y=300)

Image2 = PhotoImage(file="face.png")
button2 = Button(root,image=Image2,bg="black",bd=0,command=face)
button2.place(x=137,y=300)

Image3 = PhotoImage(file="eggs.png")
button3 = Button(root,image=Image3,bg="black",bd=0,command=eggs)
button3.place(x=267,y=300)



root.mainloop()