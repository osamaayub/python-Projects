from tkinter import *
from tkinter import messagebox
import pyspeedtest


def one():
    speed = pyspeedtest.SpeedTest("www.google.com")
    a1 = (str(speed.download())+"[Bytes per Second]")
    messagebox.showinfo("your download speed is", a1)


root = Tk()
root.title(" INTERNET SPEED CHECKER")
root.config(bg="blue")

root.geometry('500x250')

label1 = Label(root, text="  Internet Speed Checker",
               font=("Italics", 30, "bold"), bg="light pink").pack()
button1 = Button(root, text="Click", font=(
    "Arial", 20, "bold"), bg="lightblue", height=1, width=10, command=one).pack()
root.mainloop()
