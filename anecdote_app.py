import tkinter as tk
import random

# Функция для загрузки анекдотов из файла
def load_anecdots(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

# Функция для отображения случайного анекдота
def show_random_anecdote():
    random_anecdote = random.choice(anecdotes)
    text_widget.config(state=tk.NORMAL)  # Разрешаем редактирование виджета Text
    text_widget.delete(1.0, tk.END)  # Очищаем виджет Text
    text_widget.insert(tk.END, random_anecdote)  # Вставляем случайный анекдот
    text_widget.config(state=tk.DISABLED)  # Запрещаем редактирование виджета Text

# Создание главного окна
root = tk.Tk()
root.title("Случайный анекдот")

# Загрузка анекдотов из файла
anecdotes = load_anecdots("anecdotes.txt")

# Создание кнопки и виджета Text
button = tk.Button(root, text="Случайный анекдот", command=show_random_anecdote)
text_widget = tk.Text(root, wrap=tk.WORD, width=40, height=10)
text_widget.config(state=tk.DISABLED)  # Начинаем с запрета редактирования виджета Text

# Размещение виджетов в главном окне
button.pack(pady=10)
text_widget.pack()

# Запуск главного цикла приложения
root.mainloop()
