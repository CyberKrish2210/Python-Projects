import random
import tkinter as tk
import pandas as pd
import datetime

# Creating Main Window
root = tk.Tk()
root.geometry("400x200")
root.title("Friendship Calc")
result = 40 + int(pd.datetime.now().second)
root.config(bg = "silver")

# Creating Main Function
def Checkbond():
    global result
    text_area = tk.Text(master = root, height = 2, width = 60, bg = "#FFFF99")
    text_area.pack()
    result = ("Friendship Score is: ", result)
    text_area.insert(tk.END, result)

# Creating GUI
label1 = tk.Label(root, text = " Your Name ", font = ("verdana", 10), fg = "blue")
label1.pack()
entryname1 = tk.Entry(root, width = 20, bd = 5, font = ("verdana", 10))
entryname1.pack()
label2 = tk.Label(root, text = " Other Person's Name ", font = ("verdana", 10), fg = "blue")
label2.pack()
entryname2 = tk.Entry(root, width = 20, bd = 5, font = ("verdana", 10))
entryname2.pack()
button = tk.Button(root, text = " Check Your Bond ", bg = "pink", command = Checkbond)
button.pack()

root.mainloop()