from tkinter import *
from tkinter import messagebox
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image, ImageTk


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
            label5.configure(text=f"D > 0 --> 2 решения: \n x1 = {x1}\n x2 = {x2}")
            Graph2x(x1,x2)

        elif D == 0:
            x =round((-b / (2*a)), 2)
            label5.configure(text=f"D = 0 --> 1 решение: \n x = {x}")
            Graph1X()


        else:
            label5.configure(text="Решений нет")
        
    except:
        messagebox.showerror("Error")

def entryColor(event):
    i=entryA.get()
    if i == "":
        entryA.configure(bg="red")
    else:
        entryA.configure(bg="#ffe6f0")

    i=entryB.get()
    if i == "":
        entryB.configure(bg="red")
    else:
        entryB.configure(bg="#ffe6f0")
    i=entryC.get()
    if i == "":
        entryC.configure(bg="red")
    else:
        entryC.configure(bg="#ffe6f0")

def Graph1X():
    a = float(entryA.get())
    b = float(entryB.get())
    c = float(entryC.get())
    x=np.linspace(-20, 20, 100)
    y = a * x**2 + b * x + c 

    plt.plot(x, y, label=f"{a}x² + {b}x + {c}")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid()
    plt.legend()
    plt.show()


def Graph2x(x1,x2):
    a = float(entryA.get())
    b = float(entryB.get())
    c = float(entryC.get())
    x=np.linspace(x1 - 2, x2 + 2, 100)
    y = a * x**2 + b * x + c 

    plt.plot(x, y, label=f"{a}x² + {b}x + {c}")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid()
    plt.legend()
    plt.show()




root=Tk()
root.geometry("900x400")
root.resizable(False,False)
root.title("Решение квадратного уравнения")

label1 = Label(root, text = "Решение квадратного уравнения", font=("beer money", 20), bg= "#ffccff")
label1.pack(pady="20")

entryA= Entry(root, font=("beer money", 40), bg="#ffe6f0")
entryA.place(x=40,y=180, width=100)
entryA.bind("<KeyRelease>" ,entryColor)

label2=Label(root, font=("beer money", 40), text="x^2 +", bg="white")
label2.place(x=150, y=180)

entryB= Entry(root, font=("beer money", 40), bg="#ffe6f0")
entryB.place(x=275,y=180, width=100)
entryB.bind("<KeyRelease>" ,entryColor)

label3=Label(root, font=("beer money", 40), text="x +", bg="white")
label3.place(x=385, y=180)

entryC= Entry(root, font=("beer money", 40), bg="#ffe6f0")
entryC.place(x=465,y=180, width=100)
entryC.bind("<KeyRelease>" ,entryColor)

label4=Label(root, font=("beer money", 40), text="=0", bg="white")
label4.place(x=575, y=180)


button1=Button(root,text="Решить",font=("beer money", 45), command= Solve, bg="#ffe6e6")
button1.place(x=650, y = 140)


label5=Label(root, text="Ответ...",bg = "#ddccff", compound="center",)
label5.place(x=120, y= 290, width=600, height=90)



root.mainloop()