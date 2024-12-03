# Задание 1: Вычисления дат

from datetime import date
from calendar import monthrange

# Текущая дата
today = date.today()
print(f"Täna on {today}")

# Разные форматы даты
print("Erinevad formaadid:")
print(today.strftime("%d/%m/%Y"))  # 27/12/2022
print(today.strftime("%B %d, %Y"))  # December 27, 2022
print(today.strftime("%m/%d/%y"))  # 12/27/22
print(today.strftime("%b-%d-%Y"))  # Dec-27-2022

# Количество дней до конца месяца и года
day, month, year = today.day, today.month, today.year
month_days = monthrange(year, month)[1]
days_to_month_end = month_days - day
days_to_year_end = (date(year + 1, 1, 1) - today).days

print(f"Päevi kuu lõpuni: {days_to_month_end}")
print(f"Päevi aasta lõpuni: {days_to_year_end}")

# Задание 2: Операции с правильными и неправильными скобками
try:
    result_with_brackets = 3 + 8 / (4 - 2) * 4  # Правильные скобки
    print(f"Tulemus sulgudega: {result_with_brackets}")
except ZeroDivisionError:
    print("Viga: Nulliga jagamine sulgudes.")

try:
    result_without_brackets = 3 + 8 / 4 - 2 * 4  # Без правильных скобок
    print(f"Tulemus ilma korrektsete sulgudeta: {result_without_brackets}")
except Exception as e:
    print(f"Viga: {e}")

# Задание 3: Вычисления с окружностью
import math

# Данные
radius = float(input("Sisesta ringi raadius: "))
square_side = 2 * radius

# Вычисления
square_area = square_side ** 2
square_perimeter = 4 * square_side
circle_area = math.pi * radius ** 2
circle_circumference = 2 * math.pi * radius

# Вывод
print(f"Ruudu pindala: {square_area}")
print(f"Ruudu ümbermõõt: {square_perimeter}")
print(f"Ringi pindala: {circle_area}")
print(f"Ringi ümbermõõt: {circle_circumference}")

# Задание 4: Покрытие окружности Земли монетами по экватору

# Данные
earth_radius = 6378  # км
coin_diameter = 0.02575  # м (монета 2 евро)
pi = math.pi

# Окружность Земли
earth_circumference = 2 * pi * earth_radius * 1000  # в метрах
number_of_coins = earth_circumference / coin_diameter

print(f"Maa ümbermõõdu katmiseks ekvaatoril on vaja {number_of_coins:.0f} 2-eurost münti.")

# Задание 5: Killadi-koll
word = "Kill-Koll"
pattern = f"{word} {word} Killadi-Koll {word} {word} Killadi-Koll {word} {word} {word} {word}\n{word}"
print(pattern.upper())

# Задание 6: Текст песни
song = """
Rong see sõitis tsuhh tsuhh tsuhh,
Piilupart oli rongijuht.
Rattad tegid rat tat taa,
Rat tat taa ja tat tat taa.
Aga seal rongi peal,
Kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
Piilupart oli rongijuht.
Rattad tegid kill koll koll,
Kill koll koll ja kill koll kill.
"""

print(song.upper())

# Задание 7: Прямоугольник
try:
    side_a = float(input("Sisesta ristküliku esimese külje pikkus: "))
    side_b = float(input("Sisesta ristküliku teise külje pikkus: "))
    perimeter = 2 * (side_a + side_b)
    area = side_a * side_b
    print(f"Ristküliku ümbermõõt: {perimeter}")
    print(f"Ristküliku pindala: {area}")
except ValueError:
    print("Sisesta numbreid!")

# Задание 8: Расход топлива
try:
    fuel_used = float(input("Sisesta tankitud kütuse kogus (liitrites): "))
    kilometers_driven = float(input("Sisesta läbitud kilomeetrid: "))
    fuel_consumption = fuel_used / kilometers_driven * 100
    print(f"Kütusekulu: {fuel_consumption:.2f} l/100km")
except ZeroDivisionError:
    print("Viga: Kilomeetrite arv ei saa olla 0!")
except ValueError:
    print("Viga: Palun sisesta numbriline väärtus.")

# Задание 9: Роллер
try:
    speed = 29.9  # км/ч
    minutes = int(input("Sisesta aeg minutites: "))
    distance = speed * minutes / 60
    print(f"Rulluisutaja jõuab {distance:.2f} km kaugusele {minutes} minutiga.")
except ValueError:
    print("Palun sisesta korrektne arv.")

# Задание 10: Конвертация времени
try:
    minutes = int(input("Sisesta aeg minutites: "))
    hours = minutes // 60
    remaining_minutes = minutes % 60
    print(f"Aeg: {hours}:{remaining_minutes}")
except ValueError:
    print("Sisesta korrektne arv!")
