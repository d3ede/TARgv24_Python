import datetime

def is_valid_length(id_code: str) -> bool:
    return len(id_code) == 11

def is_digits_only(id_code: str) -> bool:
    return id_code.isdigit()

def is_valid_first_digit(id_code: str) -> bool:
    return id_code[0] in "123456"

def extract_birth_date(id_code: str):
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
        return None, None

    year = century + yy

    try:
        date_obj = datetime.date(year, mm, dd)
        return date_obj.strftime("%d.%m.%Y"), century
    except ValueError:
        return None, None

def is_valid_control_digit(id_code: str) -> bool:
    weights_stage1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    weights_stage2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    
    first_10 = id_code[:10]
    sum_stage1 = sum(int(digit) * weights_stage1[i] for i, digit in enumerate(first_10))
    
    remainder1 = sum_stage1 % 11
    if remainder1 != 10:
        check_digit = remainder1
    else:
        sum_stage2 = sum(int(digit) * weights_stage2[i] for i, digit in enumerate(first_10))
        remainder2 = sum_stage2 % 11
        check_digit = remainder2 if remainder2 != 10 else 0

    return check_digit == int(id_code[-1])

def get_gender_info(id_code: str):
    first_digit = int(id_code[0])
    if first_digit in [1, 3, 5]:
        return "мужчина", "его"
    return "женщина", "ее"

def get_birth_hospital(id_code: str) -> str:
    hospital_code = int(id_code[7:10])

    if 1 <= hospital_code <= 10:
        return "Kuressaare Haigla"
    elif 11 <= hospital_code <= 19:
        return "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
    elif 21 <= hospital_code <= 220:
        return "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigла, Loksa haigла"
    elif 221 <= hospital_code <= 270:
        return "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif 271 <= hospital_code <= 370:
        return "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigла"
    elif 371 <= hospital_code <= 420:
        return "Narva Haigла"
    elif 421 <= hospital_code <= 470:
        return "Pärnu Haigла"
    elif 471 <= hospital_code <= 490:
        return "Pelgulinna Sünнitusmaja (Tallinn), Haapsalu haigла"
    elif 491 <= hospital_code <= 520:
        return "Järvamaa Haigла (Paide)"
    elif 521 <= hospital_code <= 570:
        return "Rakvere, Tapa haigла"
    elif 571 <= hospital_code <= 600:
        return "Valga Haigла"
    elif 601 <= hospital_code <= 650:
        return "Viljandi Haigла"
    elif 651 <= hospital_code <= 700:
        return "Lõuna-Eesti Haigла (Võru), Põlva Haигла"
    else:
        return "Неизвестное место рождения"

def sort_id_codes(ikoodid: list) -> list:
    women_codes = [code for code in ikoodid if code[0] in "246"]
    men_codes = [code for code in ikoodid if code[0] in "135"]
    return women_codes + men_codes
