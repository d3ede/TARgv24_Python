import random
import string

# Списки для логина/пароля:
users = ["admin"]
passwords = ["Admin123!"]

def generate_password():
    chars = string.ascii_letters + string.digits + ".,:;!_*-+()/#¤%&"
    return ''.join(random.choice(chars) for _ in range(12))

def is_strong_password(password):
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(char in "@.,:;!_*-+()/#¤%&" for char in password)
    
    return has_digit and has_upper and has_lower and has_special

def register():
    username = input("Введите новое имя пользователя: ")
    if username in users:
        print("Ошибка: Это имя уже занято!")
        return

    print("Выберите способ создания пароля:")
    print("1. Автоматическая генерация")
    print("2. Ввести вручную")

    choice = input("Введите 1 или 2: ")

    if choice == "1":
        password = generate_password()
        print(f"Ваш сгенерированный пароль: {password}")
    elif choice == "2":
        while True:
            password = input("Введите новый пароль: ")
            if is_strong_password(password):
                break
            print("Пароль слишком слабый! Должен содержать цифры, заглавные и строчные буквы, спецсимволы.")

    users.append(username)
    passwords.append(password)
    print("Регистрация успешна!")

def login():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    if username in users and passwords[users.index(username)] == password:
        print("Вход выполнен успешно!")
    else:
        print("Ошибка: Неверное имя пользователя или пароль.")

def change_credentials():
    username = input("Введите имя пользователя: ")
    if username not in users:
        print("Ошибка: Пользователь не найден.")
        return

    index = users.index(username)
    
    print("Что хотите изменить?")
    print("1. Имя пользователя")
    print("2. Пароль")
    choice = input("Введите 1 или 2: ")

    if choice == "1":
        new_username = input("Введите новое имя: ")
        if new_username in users:
            print("Ошибка: Это имя уже занято!")
        else:
            users[index] = new_username
            print("Имя пользователя успешно изменено!")
    
    elif choice == "2":
        while True:
            new_password = input("Введите новый пароль: ")
            if is_strong_password(new_password):
                passwords[index] = new_password
                print("Пароль успешно изменен!")
                break
            print("Пароль слишком слабый!")

def reset_password():
    username = input("Введите имя пользователя: ")
    if username in users:
        index = users.index(username)
        new_password = generate_password()
        passwords[index] = new_password
        print(f"Ваш новый пароль: {new_password}")
    else:
        print("Ошибка: Пользователь не найден.")
