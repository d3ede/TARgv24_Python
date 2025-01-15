print("Задание 1")
N = int(input("Сколько чисел хотите ввести? "))
max_num = None

for i in range(N):
    x = float(input(f"Введите число №{i+1}: "))
    if max_num is None or x > max_num:
        max_num = x

print("Максимальное число:", max_num)
print("-" * 50, "\n")

print("Задание 2")
print("Введите целые числа. Для окончания введите 'stop'.")
while True:
    user_input = input("Введите число (или 'stop' для выхода): ")
    if user_input.lower() == "stop":
        print("Выход из цикла ввода чисел.")
        break

    try:
        num = int(user_input)
    except ValueError:
        print("Ошибка: введите целое число или 'stop'.")
        continue

    if num == 13:
        print("77")
    else:
        print(num)

print("-" * 50, "\n")

print("Задание 3")
day_distance = 10.0
total_distance = 0.0

for day in range(1, 8):
    total_distance += day_distance
    day_distance *= 1.1  # * 10%

print(f"Суммарный путь спортсмена за 7 дней: {total_distance:.2f} км")
print("-" * 50, "\n")

print("Задание 4")
M = float(input("Введите исходную длину ткани (метров): "))

while True:
    request = input(
        "Какой длины кусок требуется? (введите число) или 'stop' для выхода: "
    )
    if request.lower() == "stop":
        print("Программа остановлена пользователем.")
        break

    try:
        requested_length = float(request)
    except ValueError:
        print("Ошибка: введите число или 'stop'.")
        continue

    if requested_length <= M:
        M -= requested_length
        print(f"Отрезано {requested_length} м, осталось {M:.2f} м ткани.")
    else:
        print("Материала не хватает!")
        buy_answer = input(f"Хотите выкупить оставшийся кусок {M:.2f} м? (y/n): ")
        if buy_answer.lower() == 'y':
            print(f"Вы купили оставшийся кусок ткани {M:.2f} м.")
            break
        else:
            print("Покупатель отказался. Переходим к следующему покупателю.\n")

print("-" * 50, "\n")

print("Задание 5")
while True:
    choice = input("Вычислить площадь трапеции? (y/n): ")
    if choice.lower() != 'y':
        print("Выход из расчёта площадей трапеции.")
        break

    try:
        a = float(input("Введите длину верхнего основания a: "))
        b = float(input("Введите длину нижнего основания b: "))
        h = float(input("Введите высоту h: "))
    except ValueError:
        print("Ошибка: введите числовые значения.")
        continue

    area = 0.5 * (a + b) * h
    print(f"Площадь трапеции: {area:.2f}")

print("-" * 50, "\n")

print("Задание 6")
try:
    num_for_check = int(input("Введите целое число для проверки деления на 3: "))
    if num_for_check % 3 == 0:
        print("Число делится на 3 без остатка.")
    else:
        print("Число НЕ делится на 3 (с остатком).")
except ValueError:
    print("Ошибка: введите целое число.")

print("Все задачи завершены.")