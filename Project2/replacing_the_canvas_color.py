import tkinter as tk

'''Функция выбора цвета'''
def change_bg_color():
    color = entry.get()
    canvas.config(bg=color)

'''Функция очистки поля entry'''
def clear():
  entry.delete(0,'end')


'''Интерфейс'''

root = tk.Tk()
root.geometry('300x300')
root.title("Выбор цвета")
root.resizable(False, False)

canvas = tk.Canvas(root, width=200, height=200, bg='white')
canvas.pack()

entry = tk.Entry(root)
entry.pack()
