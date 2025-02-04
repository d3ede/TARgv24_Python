import id_code_utils

def main():
    ikoodid = []
    arvud = []

    while True:
        id_code = input("Введите личный код (или введите 'STOP' для завершения): ").strip()

        if id_code.lower() == "stop":
            break
        
        if not id_code_utils.is_valid_length(id_code):
            print("Количество цифр не верное. Повторите ввод.")
            arvud.append(id_code)
            continue

        if not id_code_utils.is_digits_only(id_code):
            print("В личном коде должны быть только цифры. Повторите ввод.")
            arvud.append(id_code)
            continue

        if not id_code_utils.is_valid_first_digit(id_code):
            print("Первая цифра кода некорректна. Повторите ввод.")
            arvud.append(id_code)
            continue

        birth_date, century = id_code_utils.extract_birth_date(id_code)
        if not birth_date:
            print("Дата рождения некорректна. Повторите ввод.")
            arvud.append(id_code)
            continue

        if not id_code_utils.is_valid_control_digit(id_code):
            print("Контрольная сумма не совпадает. Повторите ввод.")
            arvud.append(id_code)
            continue

        gender, pronoun = id_code_utils.get_gender_info(id_code)
        hospital_name = id_code_utils.get_birth_hospital(id_code)

        print(f"Это {gender}, {pronoun} день рождения {birth_date} и место рождения {hospital_name}")
        ikoodid.append(id_code)

    arvud.sort()
    print("\nСписок некорректных кодов (arvud):")
    for code in arvud:
        print(code)

    sorted_ikoodid = id_code_utils.sort_id_codes(ikoodid)

    print("\nСписок корректных кодов (ikoodid):")
    for code in sorted_ikoodid:
        print(code)

if __name__ == "__main__":
    main()
