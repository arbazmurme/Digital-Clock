from tkinter import *
from time import strftime

root = Tk()
root.geometry("250x200")
root.resizable(0,0)
root.title('Dijital Clock')
Label(root,text = 'Arbaz Murme :)', font ='arial 20 bold').pack(side=BOTTOM)

def time():
    string = strftime('%H:%M:%S')
    mark.config(text = string)
    mark.after(1000, time)

mark = Label(root, 
            font = ('calibri', 40, 'bold'),
            pady=150,
            foreground = 'black')
mark.pack(anchor = 'center')
time()
 
mainloop()