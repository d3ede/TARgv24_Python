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

#Ülesanne 4
print("Läbimõõdu leidmine ")
#l-ümbermõõt
l=float(input("Ümbermõõt: "))
d=l/pi
print(f"Läbimõõdu suurus on {round(d,2)}")
