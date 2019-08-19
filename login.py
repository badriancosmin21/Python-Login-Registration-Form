import tkinter as tk
import csv
from tkinter import messagebox
from PIL import Image, ImageTk

win = tk.Tk()
win.title("Login")
win.resizable(False, False)

xPos = int(win.winfo_screenwidth()/2 - win.winfo_reqwidth())
yPos = int(win.winfo_screenheight()/2 - win.winfo_reqheight())
win.geometry("+{}+{}".format(xPos, yPos))
win.geometry("400x400")

image = Image.open("C:/Users/zbirl/Desktop/PYTHON/python.png")
image = image.resize((400, 110), Image.ANTIALIAS)
pic = ImageTk.PhotoImage(image)
tk.Label(win, image=pic).pack()

frame1 = tk.Frame(win)
frame1.pack()
frame2 = tk.Frame(win)
frame2.pack()
frame3 = tk.Frame(win)
frame3.pack()

tk.Label(frame1, text="Username: ", font=("arial", 15, "bold")).pack()
tk.Label(frame2, text="Password: ", font=("arial", 15, "bold")).pack()
entry_user = tk.Entry(frame1, width=20)
entry_user.pack()
entry_pass = tk.Entry(frame2, width=20)
entry_pass.pack()


def login():
    file = open("login.txt", "r")
    file_reader = csv.reader(file)

    k = 0
    for row in file_reader:
        if entry_user.get() == row[0] and entry_pass.get() == row[1]:
            k = 1
            break
    if k == 0:
        messagebox.showinfo("Login", "Wrong Username/Password!")
    else:
        messagebox.showinfo("Login", "Success!!")
    file.close()


def register():
    file = open("login.txt", "a")

    if len(entry_user.get()) < 6:
        messagebox.showinfo("Register", "Username must be at least 6 characters long!")
    elif len(entry_pass.get()) < 6:
        messagebox.showinfo("Register", "Password must be at least 6 characters long!")
    elif not any(c.islower() for c in entry_pass.get()):
        messagebox.showinfo("Register", "Password must have at least one lowercase letter!")
    elif not any(c.isupper() for c in entry_pass.get()):
        messagebox.showinfo("Register", "Password must have at least one uppercase letter!")
    elif not any(c.isdigit() for c in entry_pass.get()):
        messagebox.showinfo("Register", "Password must have at least one number!")
    else:
        file.write(entry_user.get() + "," + entry_pass.get() + "\n")
        messagebox.showinfo("Register", "Registration Successful!")

    file.close()


tk.Button(frame3, text="Login", font=("arial", 20, "bold"), bg="blue", command=login).pack()
tk.Button(frame3, text="Register", font=("arial", 20, "bold"), bg="red", command=register).pack()
win.mainloop()
