

import tkinter as tk
from tkinter.filedialog import *
from pytube import *
from tkinter.messagebox import *

# Download Function
def startDownload():
    global file_size
    try:
        url = z.get()
        button.config(text = "Please Wait...")
        button.config(DISABLED)
        path_to_savevideo = askdirectory()
        if path_to_savevideo is None:
            return
        ob = YouTube(url)
        strm = ob.streams.first()
        strm.download(path_to_savevideo)
        print("Done....")
        button.config(text = "Download Again")
        button.config(state = NORMAL)
        showinfo("Download Finished", "Downloaded Successfully")
        url.delete(0, END)


    except Exception as e:
        print(e)
        print("Error!!!")

# creating Object
root = tk.Tk()

# Main Variable
file_size = 0

# UI
root.geometry("400x100")

file = PhotoImage(file = "Youtube Downloader\\image.png")
headingImg = Label(root, image = file)
headingImg.pack(side = LEFT)

icon = root.iconbitmap("Youtube Downloader\\youtubeicon.ico")

x = tk.Label(root, text = "Youtube Video Downloader"
                          " by Krishna")
x.pack()

root.title("My Youtube Downloader")

z = tk.Entry(root, bd = 5, font = ("verdana", 18), justify = CENTER)
z.pack()

button = tk.Button(root, text = "Download", fg = "red", command = startDownload)
button.pack()

# Creating Actual Window
root.mainloop()

