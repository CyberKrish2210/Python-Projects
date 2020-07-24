import tkinter as tk
from tkinter import *

root=tk.Tk()
root.geometry("270x340")
root.title("Krishna's Calc")
root.config(bg="Dark Grey")
tk.Label(root, text="Krishna's Calc",bg="Dark Grey", font=("Courier New",15,"bold")).grid(row=0,column=1)
text=StringVar()
operator=""

def clickbut(numbers):
    global operator
    operator=operator +str(numbers)
    text.set(operator)

def equlbut():
    global operator
    add=str(eval(operator))
    text.set(add)
    operator=""

def equlbut():
    global operator
    sub=str(eval(operator))
    text.set(sub)
    operator=""

def equlbut():
    global operator
    mul=str(eval(operator))
    text.set(mul)
    operator=""

def equlbut():
    global operator
    div=str(eval(operator))
    text.set(div)
    operator=""

def clrbut():
    text.set(" ")

tk.Entry(root,font=("Courier New",10,'bold'),textvar=text,width=23,bd=3,bg='Light Blue').grid(row=1,column=1)

but1=Button(root,padx=10,pady=10,bd=4,bg="light blue",command=lambda:clickbut(1),text="1").grid(row=3,column=0)
but2=Button(root,padx=10,pady=10,bd=4,bg="light blue",command=lambda:clickbut(2),text="2").grid(row=4,column=0)
but3=Button(root,padx=10,pady=10,bd=4,bg="light blue",command=lambda:clickbut(3),text="3").grid(row=5,column=0)
but4=Button(root,padx=10,pady=10,bd=4,bg="light blue",command=lambda:clickbut(4),text="4").grid(row=3,column=1)
but5=Button(root,padx=10,pady=10,bd=4,bg="light blue",command=lambda:clickbut(5),text="5").grid(row=4,column=1)
but6=Button(root,padx=10,pady=10,bd=4,bg="light blue",command=lambda:clickbut(6),text="6").grid(row=5,column=1)
but7=Button(root,padx=10,pady=10,bd=4,bg="light blue",command=lambda:clickbut(7),text="7").grid(row=3,column=2)
but8=Button(root,padx=10,pady=10,bd=4,bg="light blue",command=lambda:clickbut(8),text="8").grid(row=4,column=2)
but9=Button(root,padx=10,pady=10,bd=4,bg="light blue",command=lambda:clickbut(9),text="9").grid(row=5,column=2)
but0=Button(root,padx=50,pady=10,bd=4,bg="light blue",command=lambda:clickbut(0),text="0").grid(row=6,column=1)
butclr=Button(root,padx=10,pady=10,bd=4,bg="light blue",command=clrbut,text="Clear").grid(row=7,column=1)
butpl=Button(root,padx=10,pady=10,bd=4,bg="light blue",command=lambda:clickbut("+"),text="+").grid(row=6,column=0)
butsub=Button(root,padx=10,pady=10,bd=4,bg="light blue",command=lambda:clickbut("-"),text="-").grid(row=7,column=0)
butml=Button(root,padx=10,pady=10,bd=4,bg="light blue",command=lambda:clickbut("*"),text="*").grid(row=6,column=2)
butdiv=Button(root,padx=10,pady=10,bd=4,bg="light blue",command=lambda:clickbut("/"),text="/").grid(row=7,column=2)
butequalto=Button(root,padx=70,pady=10,bd=4,bg="light blue",command=equlbut,text="=").grid(row=8,column=1)
root.mainloop()