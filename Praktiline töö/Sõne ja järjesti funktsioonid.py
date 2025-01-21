while True:
    print("")
    print("1. Поиск подстроки в строке (.find)")
    print("2. Замена подстроки (.replace)")
    print("3. Разбиение строки по разделителю (.split)")
    print("4. Преобразование строки к верхнему регистру (.upper)")
    print("5. Преобразование строки к нижнему регистру (.lower)")
    print("6. Сборка строки из списка с разделителем (.join)")
    print("7. Удаление пробелов в начале и/или конце строки (.strip)")
    print("8. «Обратная» смена регистра (.swapcase)")
    print("9. Преобразование строки так, чтобы каждое слово начиналось с заглавной буквы (.title)")
    print("10. Пример работы со списком: добавление, удаление элементов и т.д.")
    print("0. Выход")
    
    choice = input("Выберите пункт меню (0-10): ")
    
    if choice == "0":
        print("Выход из программы.")
        break
    
    elif choice == "1":
        # Метод .find возвращает индекс первого вхождения подстроки или -1, если подстрока не найдена.
        example_string = "Hello world! Это пример для поиска."
        substring = "пример"
        index = example_string.find(substring)
        print(f"\nСтрока: {example_string}")
        print(f"Ищем подстроку '{substring}'...")
        if index != -1:
            print(f"Подстрока найдена по индексу: {index}")
        else:
            print("Подстрока не найдена.")
    
    elif choice == "2":
        # Метод .replace заменяет все вхождения указанного фрагмента на другой.
        text = "Python - отличный язык программирования."
        replaced_text = text.replace("Python", "JavaScript")
        print(f"\nИсходная строка: {text}")
        print(f"После замены 'Python' на 'JavaScript': {replaced_text}")
    
    elif choice == "3":
        # Метод .split возвращает список, разделяя строку по заданному разделителю.
        text = "яблоко;груша;слива;вишня"
        split_list = text.split(";")
        print(f"\nИсходная строка: {text}")
        print(f"Результат split по ';': {split_list}")
    
    elif choice == "4":
        # Метод .upper преобразует все буквы в строке в верхний регистр.
        text = "hello world"
        upper_text = text.upper()
        print(f"\nИсходная строка: {text}")
        print(f"В верхнем регистре: {upper_text}")
    
    elif choice == "5":
        # Метод .lower преобразует все буквы в строке в нижний регистр.
        text = "HELLO WORLD"
        lower_text = text.lower()
        print(f"\nИсходная строка: {text}")
        print(f"В нижнем регистре: {lower_text}")
    
    elif choice == "6":
        # Метод .join объединяет элементы списка, вставляя между ними указанный разделитель.
        fruits_list = ["яблоко", "груша", "слива", "вишня"]
        joined_string = ", ".join(fruits_list)
        print(f"\nСписок: {fruits_list}")
        print(f"Объединение через запятую и пробел: {joined_string}")
    
    elif choice == "7":
        # .strip() — удаляет пробельные символы слева и справа.
        # .lstrip() — удаляет пробельные символы слева.
        # .rstrip() — удаляет пробельные символы справа.
        text = "   Python - это круто!   "
        print(f"\nИсходная строка (с пробелами): '{text}'")
        print(f"strip(): '{text.strip()}'")
        print(f"lstrip(): '{text.lstrip()}'")
        print(f"rstrip(): '{text.rstrip()}'")
    
    elif choice == "8":
        # Метод .swapcase преобразует символы нижнего регистра в верхний, а верхнего — в нижний.
        text = "PyThOn iS FuN!"
        swapped_text = text.swapcase()
        print(f"\nИсходная строка: {text}")
        print(f"swapcase(): {swapped_text}")
    
    elif choice == "9":
        # Метод .title делает каждое слово с заглавной буквы.
        text = "hello world! это python."
        titled_text = text.title()
        print(f"\nИсходная строка: {text}")
        print(f"title(): {titled_text}")
    
    elif choice == "10":
        # Пример работы со списком: добавление, удаление элементов
        my_list = [10, 20, 30, 40, 50]
        print(f"\nИсходный список: {my_list}")
        
        # Добавляем элемент в конец списка
        my_list.append(60)
        print(f"После добавления (append) 60: {my_list}")
        
        # Вставка элемента по индексу
        my_list.insert(2, 25)
        print(f"После вставки (insert) 25 в позицию 2: {my_list}")
        
        # Удаление элемента по значению
        if 40 in my_list:
            my_list.remove(40)
            print(f"После удаления (remove) 40: {my_list}")
        
        # Удаление последнего элемента
        popped_value = my_list.pop()
        print(f"После pop() - извлекли {popped_value}, список стал: {my_list}")
        
        # Сортировка списка
        my_list.sort()
        print(f"После сортировки (sort): {my_list}")
    
    else:
        print("Неверный выбор. Пожалуйста, повторите попытку.")

print("Программа завершена.")
