from tkinter import *
import tkinter
from PIL import Image,ImageTk
import json
from difflib import get_close_matches


data=open("data.json",)
data_load=json.load(data)

def search (word):
    if word in data_load:
        meaning_word.delete(1.0,END)
        meaning_word.config(fg="red")
        meaning_word.insert(END,data_load[word])
    elif(len(get_close_matches(word,data_load.keys())))>0:
        meaning_word.config(fg=("red"))
        meaning_word.delete(1.0,END)
        meaning_word.insert(END,"WERE YOU FINDING {}  MEANING OF THAT PARTICULAR WORD:{}.".format(get_close_matches(word,data_load.keys())[0],data_load[get_close_matches(word,data_load.keys())[0]]))
    
    final=get_close_matches(word,data_load.keys())
root=Tk()
root.title("MY DICTIONARY")


image=Image.open('dict.png')
image_picture=ImageTk.PhotoImage(image)
dest_pic=Label(root,image=image_picture)
dest_pic.pack()

a=StringVar()

word_meaning=Entry(root,textvariable=a,background="blue",fg="white",font=("Arial",40,"bold"))
word_meaning.place(relx=.185,rely=.70,relwidth=.75,relheight=.082)

button1=Button(root,text="Search The Word For",command=lambda:search(a.get()),background="red",fg="white",font=('Arial',40,"bold"))
button1.place(relx=.25,rely=.80,relwidth=.50,relheight=.052)

meaning_word=Text(root,background="white",font=("Arial",25,"bold"))
meaning_word.place(relx=.200,rely=.05,relwidth=.63,relheight=.16)


root.mainloop()