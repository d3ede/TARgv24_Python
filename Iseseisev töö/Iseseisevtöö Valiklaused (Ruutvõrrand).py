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
    angles[i] = int(input(f"Введи число №{i + 1}: "))

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
def zodiac_sign(day, month):
    if (21 <= day <= 31 and month == 3) or (1 <= day <= 19 and month == 4):
        return "Овен"
    elif (20 <= day <= 30 and month == 4) or (1 <= day <= 20 and month == 5):
        return "Телец"
    elif (21 <= day <= 31 and month == 5) or (1 <= day <= 20 and month == 6):
        return "Близнецы"
    elif (21 <= day <= 30 and month == 6) or (1 <= day <= 22 and month == 7):
        return "Рак"
    elif (23 <= day <= 31 and month == 7) or (1 <= day <= 22 and month == 8):
        return "Лев"
    elif (23 <= day <= 31 and month == 8) or (1 <= day <= 22 and month == 9):
        return "Дева"
    elif (23 <= day <= 30 and month == 9) or (1 <= day <= 22 and month == 10):
        return "Весы"
    elif (23 <= day <= 31 and month == 10) or (1 <= day <= 21 and month == 11):
        return "Скорпион"
    elif (22 <= day <= 30 and month == 11) or (1 <= day <= 21 and month == 12):
        return "Стрелец"
    elif (22 <= day <= 31 and month == 12) or (1 <= day <= 19 and month == 1):
        return "Козерог"
    elif (20 <= day <= 31 and month == 1) or (1 <= day <= 18 and month == 2):
        return "Водолей"
    elif (19 <= day <= 29 and month == 2) or (1 <= day <= 20 and month == 3):
        return "Рыбы"
    else:
        return None

day = input("Введите день рождения: ")
month = input("Введите месяц рождения (число): ")

if day.isdigit() and month.isdigit():
    day = int(day)
    month = int(month)
    if 1 <= month <= 12 and 1 <= day <= 31:
        sign = zodiac_sign(day, month)
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

def solve_quadratic(a, b, c):
    # Находим дискриминант (D)
    D = b**2 - 4*a*c
    
    # Есть несколько решений
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return x1, x2
    
    # Есть одно решение
    elif D == 0:
        x = -b / (2*a)
        return x,

    # Нет решений
    else:
        return None

user_input = input("Ты хочешь решить уравнение (да/нет)? ")

if user_input.lower() == 'да':
    a = float(input("Введи a: "))
    b = float(input("Введи b: "))
    c = float(input("Введи c: "))
    
    solutions = solve_quadratic(a, b, c)

    if solutions is None:
        print("Нет решений.")
    else:
        if len(solutions) == 1:
            print(f"Есть только одно решение, x = {solutions[0]:.2f}")
        else:
            print(f"Есть два решения, x1 = {solutions[0]:.2f} и x2 = {solutions[1]:.2f}")
else:
    print("Ну.. тогда нам придётся попрощаться")