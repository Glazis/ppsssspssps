import time 
from tkinter import Tk, Label
from tkinter.constants import E 

root = Tk()
root.title("часы")
root.geometry('+800-500')
root.overrideredirect (True)
Lb = Label(root, bg= 'black',fg= 'white', text= 'я учу питон ', font= 'arial  90')
Lb.pack(ipadx=20, ipady=20)


def gettiem():
    p=':'if int (time.strftime('%S')) % 2 == 0 else ' '
    Lb['text'] = time.strftime(f'%H{p}%M{p}%S')
    Lb.after(1000,gettiem)
#label это наклейка то что отображается на экране

def closing(E):
    root.destroy()

Lb.after_idle(gettiem)
root.bind('<Escape>',closing)

root.mainloop()