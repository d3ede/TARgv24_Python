import math
import time
from datetime import datetime
def summa3(arv1:int,arv2:int,arv3:int)->int:
    #Tagastab kolme täisarvu summa
    summa=arv1+arv2+arv3
    return summa

#Моя версия:
def arithmetic(number1:int,number2:int,operation:str)->int:
    #Операции с числами
    if operation=="+":
        oper=number1+number2
    elif operation=="-":
        oper=number1-number2
    elif operation=="*":
        oper=number1*number2
    elif operation=="/":
        oper=number1/number2
    else:
        print(str("Неизвестная операция"))
    return oper

#Версия учителя:
def arithmetic2(a:float,b:int,t:str)->any:
    if t in ["+","-","*","/"]:
        if b==0 and t=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(a)+t+str(b))
    else:
        vastus="Tundmatu tehe"

    return vastus

#Високосный год кратный 4, если тысячелетие - кратный 400
def is_year_leap(year:int)->str:
    if year%4 == 0:
        return True
    else:
        return False

#Квадрат
def square(side:int)->int:
    p=side*4
    s=side*side
    d=math.sqrt(s+s)
    return p,s,d

#Времена года
def season(num:int)->str:
    winter=[12,1,2]
    spring=[3,4,5]
    summer=[6,7,8]
    autumn=[9,10,11]
    if num in winter:
        return "Winter"
    elif num in spring:
        return "Spring"
    elif num in summer:
        return "Summer"
    elif num in autumn:
        return "Autumn"

#Банковский вклад
def bank(euro:int,years:int)->any:
    procent=1.1 #Процент - 10% годовых
    for i in range(years):
        money=euro*procent
        procent=procent*1.1
    return money

#Простое число или нет
def is_prime(number:int)->str:
    if number > 1000:
        return "Введите число от 1 до 1000"
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

#День, месяц, год
def date(date_str, date_format="%Y-%m-%d"):
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False