import math # Исправил импорт

print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) # Каст к float
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P) # Исправил '' на ""
di=a*math.sqrt(2) # sqrt, а не sqr
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") # Убрал лишнюю скобку
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) # Каст к float
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) # Каст к float
S=b*c
print('Ristküliku pindala', S) # Добавил недостающую '
P=2*(b+c) # Добавил знак умножения
print("Ristküliku ümbermõõt", P)
di=math.sqrt(b**2+c**2) # Исправил формулу (во 2 степени, а не умножить на 2)
print("Ristküliku diagonaal", round(di, 1)) # Добавил недостающую скобку, сделал round с 1 знаком после запятой
print()
print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus => ')) # Убрал лишние одинарные кавычки, добавил каст к float, убрал лишнюю скобку
d=2*r # Добавил знак умножения
print("Ringi läbimõõt", d) # Добавил запятую перед d
S=math.pi*r**2 # Исправил обращение к math.pi, исправил формулу (r во 2 степени, а не умножить на 2)
print("Ringi pindala", round(S))
C=2*math.pi*r # Добавил знак умножения, исправил обращение к math.pi
print("Ringjoone pikkus", round(C, 2)) # Добавил недостающую скобку, сделал round с 2 знаками после запятой