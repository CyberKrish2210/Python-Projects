
# Main Modules
import tkinter as tk
import pyjokes

# Creating Window
root = tk.Tk()
root.geometry("400x180")
root.title("Fun Game")
label = tk.Label(root, text = "Joke Generator By Krishna", fg = "black")
label.pack()
x = tk.Text(root, height = 4, width = 80, bd = 5)
x.pack()

# Creating Function
def GenerateJoke():
    global joke
    joke = pyjokes.get_joke()
    x.insert(tk.END, joke)

z = tk.Button(root, text = "Get Joke", font = ('verdana', 15), command= GenerateJoke)
z.pack()

# Getting Joke after pressing enterkey
def enter(event):
    z.invoke()
root.bind("<Return>", enter)

root.mainloop()