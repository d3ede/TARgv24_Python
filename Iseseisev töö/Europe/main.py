import tkinter as tk
from tkinter import messagebox, simpledialog
import random

countries_file = 'list.txt'

class CountryCapitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Словарь стран и столиц")
        
        self.data = self.load_data()
        
        self.label = tk.Label(root, text="Введите страну или столицу:")
        self.label.pack(pady=5)
        
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)
        
        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.pack(pady=5)
        
        self.search_button = tk.Button(root, text="Поиск", command=self.search)
        self.search_button.pack(pady=2)

        self.add_button = tk.Button(root, text="Добавить/Исправить", command=self.add_or_correct)
        self.add_button.pack(pady=2)
        
        self.quiz_button = tk.Button(root, text="Проверка знаний", command=self.start_quiz)
        self.quiz_button.pack(pady=10)

    def load_data(self):
        try:
            with open(countries_file, "r", encoding="utf-8") as file:
                return dict(line.strip().split("-") for line in file if "-" in line)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(countries_file, "w", encoding="utf-8") as file:
            for country, capital in self.data.items():
                file.write(f"{country}-{capital}\n")

    def search(self):
        query = self.entry.get().strip()
        if query in self.data:
            self.result_label.config(text=f"Столица: {self.data[query]}")
        elif query in self.data.values():
            country = [k for k, v in self.data.items() if v == query][0]
            self.result_label.config(text=f"Страна: {country}")
        else:
            if messagebox.askyesno("Не найдено", "Добавить новую запись?"):
                self.add_or_correct(query)

    def add_or_correct(self, existing_key=None):
        country = existing_key or simpledialog.askstring("Добавить", "Введите страну:")
        if not country:
            return
        capital = simpledialog.askstring("Добавить", f"Введите столицу для {country}:")
        if not capital:
            return
        self.data[country] = capital
        self.save_data()
        messagebox.showinfo("Готово", f"{country} - {capital} добавлены!")

    def start_quiz(self):
        if not self.data:
            messagebox.showwarning("Ошибка", "Словарь пуст, добавьте страны и столицы!")
            return

        correct = 0
        total = len(self.data)
        for _ in range(5):
            country, capital = random.choice(list(self.data.items()))
            answer = simpledialog.askstring("Викторина", f"Какая столица {country}?")
            if answer and answer.lower() == capital.lower():
                correct += 1
        
        percentage = (correct / 5) * 100
        messagebox.showinfo("Результат", f"Вы ответили верно на {correct} из 5 ({percentage:.0f}%)")

root = tk.Tk()
app = CountryCapitalApp(root)
root.mainloop()
