from tkinter import *
from Graphics import *
global värv
def värvi_valik():
	global värv
	if tekst.get()!="":
		tekst.configure(bg="yellow")
		värv=tekst.get()
	else:
		tekst.configure(bg="red")
	return värv

def figure():
	global värv
	valik=var.get()
	värv=värvi_valik
	if valik==1:
		vihmavari(värv)
	else:
		vaal(värv)
	pass

# Создание окна
window=Tk() # Создаём окно
window.geometry("400x800") # Задаём окну разрешение
window.title("Graphics") # Называем окно
lbl=Label(window,text="Erinevad piltid Matplotlib abil",font="Bahnschrift 18",fg="orange",bg="black")

# Добавление элементов
var=IntVar()
r1=Radiobutton(window,text="Vihmavari", font="Bahnschrift 16",variable=var,value=1,command=figure) # Создаём радиобокс
r2=Radiobutton(window,text="Vaal", font="Bahnschrift 16",variable=var,value=2,command=figure)
tekst=Entry(window,font="Banhschrift 18",fg="green",bg="yellow",width=100) # Текст
nupp=Button(window,text="Värvi valik",font="Banschrift 16",command=värvi_valik) # Делаем кнопку

lbl.pack()
tekst.pack()
nupp.pack()
r1.pack()
r2.pack()
window.mainloop()