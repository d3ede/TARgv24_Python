import random

print("Выберите сложность:")
print("1 - Легкий (числа от 1 до 10)")
print("2 - Средний (числа от 1 до 50)")
print("3 - Сложный (числа от 1 до 100)")
difficulty = int(input("Введите номер сложности (1, 2 или 3): "))
num_questions = int(input("Сколько примеров вы хотите решить? "))

correct_answers = 0

for i in range(num_questions):
    if difficulty == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif difficulty == 2:
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
    else:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
    
    operator = random.choice(['+', '-', '*', '/'])

    if operator == '/':
        num1 = num1 * num2
        question = f"{num1} {operator} {num2}"
        correct_answer = num1 // num2
    elif operator == '+':
        question = f"{num1} {operator} {num2}"
        correct_answer = num1 + num2
    elif operator == '-':
        question = f"{num1} {operator} {num2}"
        correct_answer = num1 - num2
    elif operator == '*':
        question = f"{num1} {operator} {num2}"
        correct_answer = num1 * num2
 
    print(f"Задание {i+1}: {question}")
    user_answer = float(input("Ваш ответ: "))

    if user_answer == correct_answer:
        print("Правильно!")
        correct_answers += 1
    else:
        print(f"Неправильно. Правильный ответ: {correct_answer}")

percentage = (correct_answers / num_questions) * 100
print("\nВы решали", num_questions, "примеров.")
print("Правильных ответов:", correct_answers)
print("Процент правильных ответов:", round(percentage, 2))
if percentage < 60:
    print("Ваша оценка: 2")
elif percentage < 75:
    print("Ваша оценка: 3")
elif percentage < 90:
    print("Ваша оценка: 4")
else:
    print("Ваша оценка: 5")
