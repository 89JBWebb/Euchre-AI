import tkinter
m = tkinter.Tk()
from PIL import ImageTk, Image

m.title("Euchre GUI")
img = ImageTk.PhotoImage(Image.open("./images/30.gif"))
label1 = tkinter.Label(image=img)
label1.place(x=0,y=0)
m.mainloop()