import tkinter
from tkinter import *
import wikipedia as Wk


window=Tk()
window.title("My Wikipedia")
window.config(bg="black")
f1_heading=Frame(window)
f2_frame=Frame(window)
f3_frame=Frame(window)


Label(f1_heading,text="Wikipedia",font=("Times",30,"bold"),bg="White").pack(side=TOP)
Label(f2_frame,text="Search",font=("Times",20,"bold"),bg="lightgreen").pack(side=LEFT)
Label(f3_frame,text="Searched Result",font=("Times",25,"bold"),bg="orange").pack(side=LEFT)

entry_box=Entry(f2_frame,width=40,font=("Times",20,"bold"))
entry_box.pack(side=LEFT,fill=BOTH,expand=5)
entry_box.focus_set()

query=' '
text=Text(window,font=("Times",17,"bold"),bg="lightpink",pady=10,padx=55)

def text_Search():
    global query
    query=entry_box.get()
    try:
        txt_summary=Wk.summary(query)
        text.insert('1.0',txt_summary)
    except:
        txt_summary=Wk.summary(query)
        text.insert('1.0',txt_summary)

button1=Button(f2_frame,text="Search",command=text_Search,font=("Times",20,"bold"),bg="Blue",fg="Purple")
button1.pack(side=RIGHT)

f1_heading.pack()
f2_frame.pack(side=TOP)
f3_frame.pack(side=TOP,pady=20,padx=50)
text.pack()
window.mainloop()