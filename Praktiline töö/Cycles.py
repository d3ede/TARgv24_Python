# Task 2
while True:
	try:
		a = int(input("Sisesta A:"))
		break
	except:
		print("On vaja naturaalne arv")
summa = 0
if a>0:
	for i in range(1,a+1,1):
		summa+=i
		print(f"{i}. samm summa={summa}")
print(f"Vastus {summa}")