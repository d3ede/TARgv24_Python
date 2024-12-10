# Task 1
nimi=input("Mis on sinu nimi? ")
if nimi.isalpha() and nimi.isupper():
    if nimi=="JUKU":
        print("Lähme kinno")
        try:
            vanus=int(input(f"Kui vana sa oled {nimi}? "))
            if vanus<0:
                print("Viga!")
            elif vanus<=6:
                print("Tasuta")
            elif vanus<15:
                print("Lastepilet")
            elif vanus<65:
                print("Täispilet")
            elif vanus<100:
                print("Sooduspilet")
            else:
                print("Nii palju!!!!")
        except:
            print("Täisarv oli vaja sisestada")
    else:
        print("Ootan Juku")
else:
    print("Segatud sõne")

# Task 2
nimi1=input("Mis on nimi num 1")
nimi2=input("Mis on nimi num 2")
# 1 Variant
nimed=["Kirill","Gleb"]
if nimi1.isalpha() and nimi2.isalpha():
    if (nimi1 in nimed) and (nimi2 in nimed):
        print("Nad on pinginaarid")
    else:
        print("Nad ei ole naabrid")
else:
    print("Viga")
# 2 Variant
if nimi1=="Kirill" and nimi2=="Gleb" or nimi2=="Kirill" and nimi1=="Gleb":
    print("Nad on pinginaarid")
else:
    print("Nad ei ole naabrid")

# Task 3
try:
    a=float(input("Toa ikkus:"))
    b=float(input("Toa laius:"))
    S=a*b
    print(f"Põranda pindala on {S} m**2")
    vastus=input("Tas tahad remondi teha? (Jah/Ei or Yes/No)")
    if vastus.upper()=="JAH" or vastus.upper()=="YES":
        print("Remont")
        hind=float(input("Ühe meetri hind: "))
        summa=hind*S
        print(f"Remondi kulud: {summa} EUR")
    elif vastus.upper()=="EI" or vastus.upper()=="NO":
        print("No remont")
    else:
        print("Choose Jah/Yes or Ei/No")
except:
    print

# Task 4
price = int(input("введи цену: "))
if price > 900:
   price = price * 0.7
print("Цена с учетом скидки:", price)

# Task 5
temp = int(input("Какая сейчас температура в градусах по Цельсию?"))
if temp > 18:
    print(f"Температура выше 18 градусов, целых: {temp} градусов по Цельсию")
else:
    print(f"Температура ниже 18 градусов, точнее: {temp} градусов по Цельсию")

# Task 6
height = int(input("Какой у вас рост?\n"))
if height<151:
    print("Вы низкий")
elif height<191:
    print("Вы среднего роста")
else:
    print("Вы высокий")

# Task 7
height = int(input("Какой у вас рост?\n"))
sex = str(input("Какого вы пола? (M/F)"))
if height<151:
    if sex.upper()=="M":
        print("Вы мужчина низкого роста")
    elif sex.upper()=="F":
        print("Вы женщина низкого роста")
    else:
        print("Введите корректные данные")
elif height<191:
    if sex.upper()=="M":
        print("Вы мужчина среднего роста")
    elif sex.upper()=="F":
        print("Вы женщина среднего роста")
    else:
        print("Введите корректные данные")
else:
    if sex.upper()=="M":
        print("Вы мужчина высокого роста")
    elif sex.upper()=="F":
        print("Вы женщина высокого роста")
    else:
        print("Введите корректные данные")

# Task 8