from tkinter import *
from tkinter.ttk import *
from time import strftime

top = Tk()
top.title("Digital Clock")

#function showing current time, updates every second
def time():
    text = strftime(' %H:%M:%S %p ')
    lbl.config(text=text)
    lbl.after(1000,time)    
    
lbl=Label(top, font=('digital-7',70, 'bold'),
          background="black",foreground='turquoise')
lbl.pack(anchor='center')

time()
mainloop()