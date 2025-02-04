import user_utils

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Регистрация")
        print("2. Авторизация")
        print("3. Изменить имя или пароль")
        print("4. Восстановить пароль")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            user_utils.register()
        elif choice == "2":
            user_utils.login()
        elif choice == "3":
            user_utils.change_credentials()
        elif choice == "4":
            user_utils.reset_password()
        elif choice == "5":
            print("Выход из системы.")
            break
        else:
            print("Ошибка: Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
