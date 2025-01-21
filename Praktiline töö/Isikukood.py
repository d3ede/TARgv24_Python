import datetime

ikoodid = []
arvud = []

while True:
    id_code = input("Введите личный код (или введите 'STOP' для завершения): ").strip()

    if id_code.lower() == "stop":
        break
    
    # Шаг 1: Проверка длины
    if len(id_code) != 11:
        print("Количество цифр не верное. Повторите ввод.")
        arvud.append(id_code)
        continue
    
    # Шаг 2: Проверка на то, что введены только цифры
    if not id_code.isdigit():
        print("В личном коде должны быть только цифры. Повторите ввод.")
        arvud.append(id_code)
        continue
    
    # Шаг 3: Проверяем корректность первой цифры (пол/век)
    if id_code[0] not in "123456":
        print("Первая цифра кода некорректна. Повторите ввод.")
        arvud.append(id_code)
        continue

    # Шаг 4: Извлекаем дату
    first_digit = int(id_code[0])
    yy = int(id_code[1:3])
    mm = int(id_code[3:5])
    dd = int(id_code[5:7])
    
    if first_digit in [1, 2]:
        century = 1800
    elif first_digit in [3, 4]:
        century = 1900
    elif first_digit in [5, 6]:
        century = 2000
    else:
        arvud.append(id_code)
        continue
    
    year = century + yy
    
    try:
        date_obj = datetime.date(year, mm, dd)
    except ValueError:
        print("Дата рождения некорректна. Повторите ввод.")
        arvud.append(id_code)
        continue

    # Шаг 5: Проверяем контрольный разряд
    weights_stage1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    weights_stage2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    first_10 = id_code[:10]
    sum_stage1 = 0
    for i, digit in enumerate(first_10):
        sum_stage1 += int(digit) * weights_stage1[i]
    
    remainder1 = sum_stage1 % 11
    
    if remainder1 != 10:
        check_digit = remainder1
    else:
        sum_stage2 = 0
        for i, digit in enumerate(first_10):
            sum_stage2 += int(digit) * weights_stage2[i]
        remainder2 = sum_stage2 % 11
        if remainder2 != 10:
            check_digit = remainder2
        else:
            check_digit = 0
    
    if check_digit != int(id_code[-1]):
        print("Контрольная сумма не совпадает. Повторите ввод.")
        arvud.append(id_code)
        continue

    # Определяем пол
    # 1,3,5 — мужчина; 2,4,6 — женщина
    if first_digit in [1, 3, 5]:
        gender = "мужчина"
        pronoun = "его"
    else:
        gender = "женщина"
        pronoun = "ее"

    birth_date_str = date_obj.strftime("%d.%m.%Y")
    hospital_code = int(id_code[7:10])
    
    # Шаг 6: Определяем место рождения
    if 1 <= hospital_code <= 10:
        hospital_name = "Kuressaare Haigla"
    elif 11 <= hospital_code <= 19:
        hospital_name = "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21 <= hospital_code <= 220:
        hospital_name = "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif 221 <= hospital_code <= 270:
        hospital_name = "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271 <= hospital_code <= 370:
        hospital_name = "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif 371 <= hospital_code <= 420:
        hospital_name = "Narva Haigla"
    elif 421 <= hospital_code <= 470:
        hospital_name = "Pärnu Haigla"
    elif 471 <= hospital_code <= 490:
        hospital_name = "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif 491 <= hospital_code <= 520:
        hospital_name = "Järvamaa Haigla (Paide)"
    elif 521 <= hospital_code <= 570:
        hospital_name = "Rakvere, Tapa haigла"
    elif 571 <= hospital_code <= 600:
        hospital_name = "Valga Haigla"
    elif 601 <= hospital_code <= 650:
        hospital_name = "Viljandi Haigла"
    elif 651 <= hospital_code <= 700:
        hospital_name = "Lõuna-Eesti Haigла (Võru), Põlva Haigла"
    else:
        hospital_name = "Неизвестное место рождения"
    
    print(f"Это {gender}, {pronoun} день рождения {birth_date_str} и место рождения {hospital_name}")
    ikoodid.append(id_code)

arvud.sort()
print("\nСписок некорректных кодов (arvud):")
for code in arvud:
    print(code)

women_codes = []
men_codes = []
for code in ikoodid:
    if code[0] in "246":
        women_codes.append(code)
    else:
        men_codes.append(code)

sorted_ikoodid = women_codes + men_codes

print("\nСписок корректных кодов (ikoodid):")
for code in sorted_ikoodid:
    print(code)
