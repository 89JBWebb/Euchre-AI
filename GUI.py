import tkinter
from PIL import ImageTk, Image

def a():
    imgs = []
    labels = []
    imgs += [ImageTk.PhotoImage(Image.open("./images/12.gif"))]
    labels += [tkinter.Label(image=imgs[-1])]
    labels[-1].place(x=0,y=0)

m = tkinter.Tk()
m.title("Euchre GUI")
m.minsize(400,100)
a()
m.mainloop()
