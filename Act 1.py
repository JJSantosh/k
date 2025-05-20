from tkinter import *
from PIL import Image, ImageTk
window=Tk()
window.title("first widget")
window.geometry("400x400")
l1=Label(text="Welcome to my widget",fg="white",bg="black",height=1,width=300)
l2=Label(text="Enter your name",fg="white",bg="black",height=2,width=300)
name=Entry()
def display():
    n=name.get()
    global msg
    msg="Hello" + n + "Nice to meet you"
    tb.insert(END,msg)

tb=Text(height=3)
b=Button(text="click",command=display,height=1)
lab_img=Image.open("bg.jpeg")
img1=ImageTk.PhotoImage(lab_img)
label=Label(window,image=img1,height=200,width=300)
label.pack()

l1.pack()
l2.pack()
name.pack()
tb.pack()
b.pack()
window.mainloop()
