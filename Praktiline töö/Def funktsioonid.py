from def_funktsioon import *

#Test
a=int(input("Sisesta arv1:"))
b=int(input("Sisesta arv2:"))
c=int(input("Sisesta arv3:"))
vastus=summa3(a, b, c)
print(vastus)

#Task 1
num1=int(input("Введите число 1:"))
num2=int(input("Введите число 2:"))
op=str(input("Введите операцию с числами:"))
operat=arithmetic(num1, num2, op)
print(operat)

#Task 2
year=int(input("Введите год:"))
y=is_year_leap(year)
print(y)

#Task 3
side=int(input("Введите сторону квадрата:"))
sq=square(side)
print("Периметр, площадь и диагональ равняются: ", sq)

#Task 4
number=int(input("Введите номер месяца: "))
seas=season(number)
print(seas)

#Task 5
euro=int(input("Введите количество денег "))
today=int(input("Какой сейчас год? "))
years=int(input("Введите количество лет "))
money=bank(euro,years)
print(f"Количество денег на вашем счету {money} к {today+years} году")

#Task 6
number=int(input("Введите число от 1 до 1000 "))
number2=is_prime(number)
print(number2)

#Task 7
d=input("Введите дату (Год-Месяц-День) ")
verification=date(d)
print(verification)