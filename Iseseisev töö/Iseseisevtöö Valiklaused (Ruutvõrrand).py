# Task 1
num = int(input("Число: "))
if num > 0:
    print(f"Число {num} положительное и {'четное' if num % 2 == 0 else 'нечетное'}")
elif num < 0:
    print(f"Число {num} отрицательное")
else:
    print(f"Число {num} - ноль")

# Task 2
angles = []
for i in range(3):
    angles.append(int(input(f"Введи число №{i + 1}: ")))

if all(angle > 0 for angle in angles):
    if sum(angles) == 180:
        print("Указанные числа могут быть углами одного треугольника")
    
        if angles[0] == angles[1] == angles[2]:
            print("Треугольник равносторонний")
        elif angles[0] == angles[1] or angles[1] == angles[2] or angles[0] == angles[2]:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")
    else:
        print("Эти числа не могут быть углами одного прямоугольника")
else:
    print("Все углы должны быть положительными числами")

# Task 3
answer = input("Ты хочешь указать номер дня недели? ")
if answer.lower() == 'да':
    day_index = int(input("Введи день недели: "))
    if day_index in range(1, 7):
        days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
        print(f"Название дня недели: {days[day_index - 1]}")
    else:
        print("Это не день недели")
else:
    print("Мое дело предложить, твое - отказаться")

# Task 4
day = input("Введите день рождения: ")
month = input("Введите месяц рождения (число): ")

if day.isdigit() and month.isdigit():
    day = int(day)
    month = int(month)
    if 1 <= month <= 12 and 1 <= day <= 31:
        sign = None
        if (21 <= day <= 31 and month == 3) or (1 <= day <= 19 and month == 4):
            sign = "Овен"
        elif (20 <= day <= 30 and month == 4) or (1 <= day <= 20 and month == 5):
            sign = "Телец"
        elif (21 <= day <= 31 and month == 5) or (1 <= day <= 20 and month == 6):
            sign = "Близнецы"
        elif (21 <= day <= 30 and month == 6) or (1 <= day <= 22 and month == 7):
            sign = "Рак"
        elif (23 <= day <= 31 and month == 7) or (1 <= day <= 22 and month == 8):
            sign = "Лев"
        elif (23 <= day <= 31 and month == 8) or (1 <= day <= 22 and month == 9):
            sign = "Дева"
        elif (23 <= day <= 30 and month == 9) or (1 <= day <= 22 and month == 10):
            sign = "Весы"
        elif (23 <= day <= 31 and month == 10) or (1 <= day <= 21 and month == 11):
            sign = "Скорпион"
        elif (22 <= day <= 30 and month == 11) or (1 <= day <= 21 and month == 12):
            sign = "Стрелец"
        elif (22 <= day <= 31 and month == 12) or (1 <= day <= 19 and month == 1):
            sign = "Козерог"
        elif (20 <= day <= 31 and month == 1) or (1 <= day <= 18 and month == 2):
            sign = "Водолей"
        elif (19 <= day <= 29 and month == 2) or (1 <= day <= 20 and month == 3):
            sign = "Рыбы"
        if sign:
            print(f"Ваш знак зодиака: {sign}.")
        else:
            print("Вы ввели некорректную дату.")
    else:
        print("День или месяц вне допустимых пределов.")
else:
    print("Введите числа для дня и месяца!")

# Task 5
value = input("Введите число или текст: ")

if value.replace('.', '', 1).isdigit():
    num = float(value)
    if num.is_integer():
        print(f"Это целое число. 50% от него: {num * 0.5}.")
    else:
        print(f"Это дробное число. 70% от него: {num * 0.7}.")
elif value.isalpha():
    print(f"Это текст: {value}.")
else:
    print("Не удалось определить тип введенного значения.")

# Task 6
import math
user_input = input("Ты хочешь решить уравнение (да/нет)? ")

if user_input.lower() == 'да':
    a = float(input("Введи a: "))
    b = float(input("Введи b: "))
    c = float(input("Введи c: "))

    solutions = None

    D = b**2 - 4*a*c
    x1 = None
    x2 = None

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
    elif D == 0:
        x1 = -b / (2*a)

    if x1 is None:
        print("Нет решений.")
    else:
        if x2 is None:
            print(f"Есть только одно решение, x = {x1:.2f}")
        else:
            print(f"Есть два решения, x1 = {x1:.2f} и x2 = {x2:.2f}")
else:
    print("Ну.. тогда нам придётся попрощаться")
