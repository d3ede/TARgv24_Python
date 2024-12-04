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