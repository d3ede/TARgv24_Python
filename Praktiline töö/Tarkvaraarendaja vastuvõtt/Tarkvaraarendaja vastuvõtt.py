import random

def load_questions(filename):
    questions = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if ":" in line:
                question, answer = line.strip().split(":", 1)
                questions[question] = answer
    return questions

def ask_questions(name, questions):
    selected_questions = random.sample(list(questions.keys()), 5)
    score = 0
    
    print(f"\n{name}, вам будет задано 5 вопросов.")
    for question in selected_questions:
        answer = input(f"{name}, {question} ")
        if answer.strip().lower() == questions[question].strip().lower():
            score += 1
    
    return score

def save_results(accepted, rejected):
    with open("vastuvõetud.txt", "w", encoding="utf-8") as file:
        for name, score in sorted(accepted, key=lambda x: -x[1]):
            file.write(f"{name}: {score}\n")
    
    with open("eisoobi.txt", "w", encoding="utf-8") as file:
        for name in sorted(rejected):
            file.write(f"{name}\n")

def main():
    questions = load_questions("kusimused_vastused.txt")
    accepted = []
    rejected = []
    
    while len(accepted) < 5:
        name = input("Введите ваше имя: ")
        score = ask_questions(name, questions)
        
        if score >= 3:
            accepted.append((name, score))
            print(f"Поздравляем, {name}, вы приняты!\n")
        else:
            rejected.append(name)
            print(f"{name}, к сожалению, вы не прошли.\n")
    
    save_results(accepted, rejected)
    
    print("\nПринятые кандидаты:")
    for name, score in sorted(accepted, key=lambda x: -x[1]):
        print(f"{name}: {score} верных ответов")
    
    print("\nНе прошедшие кандидаты:")
    for name in sorted(rejected):
        print(name)

if __name__ == "__main__":
    main()