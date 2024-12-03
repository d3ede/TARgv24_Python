from msilib import PID_LASTPRINTED
from random import * #*-kõik funktsioonid, randint
from math import * #pi kasutamiseks
# #Ülesanne 1
# print("Hello World!")
# nimi=input("Mis on sinu nimi? ").capitalize()
# print("Tere tulemast!", nimi)
# vanus=int(input("Kui vana sa oled? "))
# print("Tere tulemast! Tervitan sind", vanus)

# #Ülesanne 2
# vanus = 18
# eesnimi = "Jaak"
# pikkus = 16.5
# kas_käib_koolis = True
# print(type(vanus))

# #Ülesanne 3
# kokku=randint(1, 1000)
# print(f"Kokku on {kokku} kommi")
# kommi=int(input("Mitu kommi sa tahad? "))
# kokku=kokku-kommi
# print(f"Jääk on {kokku} kommi")

# #Ülesanne 4
# print("Läbimõõdu leidmine ")
# #l-ümbermõõt
# l=float(input("Ümbermõõt: "))
# d=l/pi
# print(f"Läbimõõdu suurus on {round(d,2)}")

# #Ülesanne 5
# N = float(input("Введите длину участка (N) в метрах: "))
# M = float(input("Введите ширину участка (M) в метрах: "))
# diagonal = (N**2 + M**2)**0.5
# print("Диагональ равняется", diagonal)

# #Ülesanne 6
# time = float(input("Сколько часов ушло на дорогу? "))
# distance = float(input("Сколько километров проехали? "))
# speed = distance/time
# print("Ваша скорость была " + str(speed) + " km/h")
# # Ошибка была в измерении скорости, делили время на расстояние, а не наоборот

# #Ülesanne 7
# n1=float(input("Введите число №1"))
# n2=float(input("Введите число №2"))
# n3=float(input("Введите число №3"))
# n4=float(input("Введите число №4"))
# n5=float(input("Введите число №5"))
# mid=(n1+n2+n3+n4+n5)/2
# print("Среднее арифметическое число ваших 5 чисел равняется ", mid)

# #Ülesanne 8
# print("  @..@\n (----)\n( \__/ )\n ^^ "" ^^")

# #Ülesanne 9
# a = int(input("введи a: "))
# b = int(input("введи b: "))
# c = int(input("введи c: "))
# print("периметр: ", a + b + c)

# #Ülesanne 10
# price = 12.9
# tips = price * 0.1
# me_and_my_friend_tips = tips / 2
# print(f"С одного {me_and_my_friend_tips} и с другого {me_and_my_friend_tips}")