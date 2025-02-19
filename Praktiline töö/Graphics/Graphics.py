import numpy as np # Импортируем библиотеку с диапазоном значений
import matplotlib.pyplot as plt

# Кит
def vaal(color:str):
    x1=np.arange(0,10,1)
    y1=(2/27)*x1**2-3

    x2=np.arange(-10,0.5,0.5)
    y2=0.04*x2**2-3

    x3=np.arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+1

    x4=np.arange(-3,9.5,0.5)
    y4=(-1/12)*(x4-3)**2+6

    x5=np.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2

    x6=np.arange(5,8.5,0.5)
    y6=(1/8)*(x6-7)**2+1.5

    x7=np.arange(-13,-8.5,0.5)
    y7=(-0.75)*(x7+11)**2+6

    x8=np.arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3

    x9=np.arange(-15,-10,0.5)
    y9=[1]*len(x9)

    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)

    plt.figure(facecolor=color)
    plt.title("Kit")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    ax=plt.axes()
    ax.set_facecolor("lightblue")
    #colors=["c","m","y","r","g","b","w","k","k","k"] # Подключение цветов
    for i in range(1,11): # Цикл на координаты и цвет
        plt.plot(eval(f"x{i}"),eval(f"y{i}"),color[i-1]+"-*")
    plt.show()
    pass

# Зонт
def vihmavari(color:str):
    x1=np.arange(-12,12.5,0.5)
    x2=np.arange(-4,4.5,0.5)
    x3=np.arange(-12,-4.5,0.5)
    x4=np.arange(4,12.5,0.5)
    x5=np.arange(-4,-0.4,0.1)
    x6=np.arange(-4,0.3,0.1)
    y1=(-1/18)*x1**2+12
    y2=(-1/8)*x2**2+6
    y3=(-1/8)*(x3+8)**2+6
    y4=(-1/8)*(x4-8)**2+6
    y5=2*(x5+3)**2-9
    y6=1.5*(x6+3)**2-10
    plt.figure(facecolor=color)
    plt.title("Vihmavari")
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.grid(True)
    ax=plt.axes()
    ax.set_facecolor("lightblue")
    colors=["r","g","b","r","g","b"] # Подключение цветов
    for i in range(1,7): # Цикл на координаты и цвет
        plt.plot(eval(f"x{i}"),eval(f"y{i}"),colors[i-1]+"-*")
    plt.show()
    pass