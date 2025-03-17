import tkinter as tk
import random

class Blackjack:
    def __init__(self, root):
        self.root = root
        self.root.title("Игра 21")
        self.player_name = tk.StringVar()
        self.cards = []
        self.total = 0
        self.history_file = "results.txt"

        tk.Label(root, text="Имя игрока:").pack()
        tk.Entry(root, textvariable=self.player_name).pack()
        
        self.label = tk.Label(root, text="Нажмите 'Начать игру'")
        self.label.pack()

        tk.Button(root, text="Начать игру", command=self.start_game).pack()
        tk.Button(root, text="Взять карту", command=self.draw_card).pack()
        tk.Button(root, text="Стоп", command=self.stop_game).pack()
        tk.Button(root, text="История", command=self.show_history).pack()
    
    def read_card(self):
        return random.randint(2, 11)
    
    def start_game(self):
        self.cards = [self.read_card(), self.read_card()]
        self.total = sum(self.cards)
        self.update_label()
    
    def draw_card(self):
        if self.total < 21:
            self.cards.append(self.read_card())
            self.total = sum(self.cards)
            self.update_label()
            if self.total > 21:
                self.end_game("Проигрыш", self.play_computer())
    
    def stop_game(self):
        computer_total = self.play_computer()
        if computer_total > 21 or self.total > computer_total:
            self.end_game("Победа", computer_total)
        else:
            self.end_game("Проигрыш", computer_total)
    
    def play_computer(self):
        total = 0
        while total < 17:
            total += self.read_card()
        return total
    
    def end_game(self, result, computer_total):
        self.label.config(text=f"{result}! Ваши очки: {self.total}, Очки дилера: {computer_total}")
        self.save_result(result, computer_total)
    
    def save_result(self, result, computer_total):
        with open(self.history_file, "a", encoding="utf-8") as f:
            f.write(f"{self.player_name.get()} - {result}, Очки: {self.total}, Очки дилера: {computer_total}\n")
    
    def show_history(self):
        try:
            with open(self.history_file, "r", encoding="utf-8") as f:
                history = f.read()
        except FileNotFoundError:
            history = "История пуста."
        
        history_window = tk.Toplevel(self.root)
        history_window.title("История игр")
        tk.Label(history_window, text=history).pack()
    
    def update_label(self):
        self.label.config(text=f"Карты: {self.cards}, Очки: {self.total}")

root = tk.Tk()
app = Blackjack(root)
root.mainloop()