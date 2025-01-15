# #Task 1
# import string
# vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
# konsonanti="qwrtpsdfghklzxcvbnm"
# markid=string.punctuation # %&'()*+,-./:;<=>?@[\]ˇ_^{|}~
# while True:
#     v=k=m=t=0
#     text=input("Sisesta mingi tekst: ").lower()
#     if text.isdigit():
#         break
#     else:
#         text_list=list(text)
#         print(text_list)
#         for taht in text_list:
#             if taht in vokaali:
#                 v+=1
#             elif taht in konsonanti:
#                 k+=1
#             elif taht in markid:
#                 m+=1
#             elif taht ==" ":
#                 t+=1
#     print("Vokaali: ", v)
#     print("Konsonanti: ", k)
#     print("Markid: ", m)
#     print("Tühikud: ", t)

# #Task 2
# nimed=[]
# for i in range(5):
#     nimi=input(f"{i+1}.Nimi: ")
#     nimed.append(nimi)
# print("Enne sorteerimist:")
# print(nimed)
# nimed.sort()
# print("Sorteerimise pärast:")
# print(nimed)
# print(f"Viimasena lisatud nimi on: {nimed[4]}, {nimed[-1]}, {nimi}")
# v=input("Kas muudame nimeid?: ").lower()
# if v=="jah":
#     v=input("Nimi või positsioon: N/P").upper()
#     if v=="p":
#         print("Sisesta nime asukoht")
#         v=int(input())
#         uus_nimi=input("Uus nimi: ")
#         nimed[v-1]=uus_nimi
#         print(nimed)
#     else:
#         print("Sisesta nimi")
#         vana_nimi=input("Vana nimi: ")
#         v=nimed.index(vana_nimi)
#         uus_nimi=input("Uus nimi: ")
#         nimed[v]=uus_nimi
# doublta=list(set(nimed))
# print(doublta)

# vanused=[]
# for i in range(7):
#     vanus=int(input(f"{i+1}. Vanus: "))
#     vanused.append(vanus)
# print(f"Sisestatus vanused: {vanused}")
# print(max(vanused))
# print(min(vanused))
# print(sum(vanused)/len(vanused))

# #Task 3
# Värtused=[11,24,5,68,17]
# read=int(input("Reade kogus: "))
# for i in range(read):
#     arv=int(input("Arv"))
#     Värtused.append(arv)
# print("Värtused")
# s=input("Sümbol: ")
# for vartus in Värtused:
#     print(vartus*s)

#Task 4
indexid="Tallinn","Narva Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa Lääne-Virumaa Jõgevamaa","Tartu linn","Tartumaa Põlvamaa Võrumaa Valgamaa","Viljandimaa Järvamaa Harjumaa Raplamaa","Pärnumaa","Läänemaa Hiiumaa Saaremaa"
mask=[4,5,6,7,8,9]
home=[1,2,3]
while True:
    try:   
        index=int(input("Your index? "))
        if len(str(index)) == 5:
            break
        else:
            print("Index 5 numbers")
    except:
        print("Error")
print("Posttindeksi analüüs:")
index_list=list(str(index))
s1=int(index_list[0])
print(f" Postiindeks {index} on {index_list[s1-1]} piirkond")