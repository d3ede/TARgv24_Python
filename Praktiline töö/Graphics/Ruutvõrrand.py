from tkinter import *
from tkinter.tix import Tree
import matplotlib.pyplot as plt
import numpy as np
def Lahenda():
    pass
def Graafik():
    pass

def aken():
    aken=Tk()
    aken.geometry("650x260")
    aken.title("Ruutvõrrand")
    f1=Frame(aken,width=650,height=260)
    f1.pack()
    lbl=Label(f1,text="Ruutvõrrandite lahendamine", font="Calibri 26",fg="green",bg="lightblue")
    lbl.pack(side=TOP)
    lbl_vastus=Label(f1,text="Lahendamine",height=4,width=60,bg="yellow")
    lbl_vastus.pack(side=BOTTOM)
    lbl_a=Entry(f1,font="Calibri 26",fg="green",bg="lightblue", width=3)
    lbl_a.pack(side=LEFT)
    x2=Label(f1,text="x^2+",font="Calibri 26",fg="green",padx=10)
    x2.pack(side=LEFT)
    lbl_b=Entry(f1,font="Calibri 26",fg="green",bg="lightblue", width=3)
    lbl_b.pack(side=LEFT)
    x=Label(f1,text="x+",font="Calibri 26",fg="green",padx=10)
    x.pack(side=LEFT)
    lbl_c=Entry(f1,font="Calibri 26",fg="green",bg="lightblue", width=3)
    lbl_c.pack(side=LEFT)
    y=Label(f1,text="=0",font="Calibri 26",fg="green",padx=10)
    y.pack(side=LEFT)
    btn_lahenda=Button(f1,text="Lahenda",font="Calibri 26",fg="green",command=Lahenda)
    btn_lahenda.pack(side=LEFT)
    btn_graafik=Button(f1,text="Graafik",font="Calibri 26",fg="green",command=Graafik)
    btn_graafik.pack(side=LEFT)
    aken.mainloop()

global D, x1, x2, x, i, y
def Solve():
    try:
        a = float(entryA.get())
        b = float(entryB.get())
        c = float(entryC.get())

        D = b**2 - 4* a * c

        if D>0:
            x1=round((-b+(D**(1/2)))/(2*a),2)
            x2=round((-b-(D**(1/2)))/(2*a),2)
            label5.configure(text=f"D > 0 --> 2 Решения: \n x1 = {x1}\n x2 = {x2}")
            Graph2x(x1,x2)
    
        elif D == 0:
            x = round((-b / (2*a)), 2)
            label5.configure(text=f"D = 0 --> Решение: \n x = {x}")

        else:
            label5.configure(text="Решений нет")
    except:
        messagebox.showerror("error")
aken()