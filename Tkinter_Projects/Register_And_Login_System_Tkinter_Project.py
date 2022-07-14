from tkinter import *
import os

def delete2(): #functions to close the windows
    screen3.destroy()
    
def delete3():
    screen4.destroy()
    
def delete4():
    screen5.destroy()


    
def login_success(): 
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login success", fg="green", font=("Calibri", 11)).pack()
    Button(screen3, text="OK", command= delete2).pack()
    
def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Wrong password", fg="red", font=("Calibri", 11)).pack()
    Button(screen4, text="OK", command= delete3).pack()
    
def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User not found",fg="red", font=("Calibri", 11)).pack()
    Button(screen5, text="OK", command= delete4).pack()
    



def register_user():
    username_info = username.get()
    password_info = password.get()
    
    #open a text file and write information 
    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    
    #clear the field after successful user registration
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    Label(screen1, text="Registration Success", fg="green", font=("Calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verity.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines() #read the file and ignore line breaks
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    
    global username, password, username_entry, password_entry
    username = StringVar()
    password = StringVar()
    
    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack() #making space
    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable= username)
    username_entry.pack()
    Label(screen1, text="Password *").pack()
    password_entry = Entry(screen1, textvariable= password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width= 10, height=1, command= register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()
    
    global username_verify, password_verity, username_entry1, password_entry1
    username_verify = StringVar()
    password_verity = StringVar()
    
    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable= username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable= password_verity)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command= login_verify).pack()
    

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Register And Login")
    Label(text="Register And Login", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack() #making space
    Button(text="Login", width="30", height="2", command= login).pack()
    Label(text="").pack()
    Button(text="Register", width="30", height="2", command= register).pack()
    
    screen.mainloop()
    
main_screen()
    