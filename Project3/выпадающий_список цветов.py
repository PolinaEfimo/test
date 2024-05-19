import tkinter
from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry("250x250")
window.title('Цвета')
window.resizable(False, False)

'''функция для очистки поля со списком'''
def clear_combobox():
  combobox.set('')


colors= ['white', 'red', 'yellow', 'green', 'sky blue', 'blue', 'brown', 'grey', 'black']

def change_color(event):
  color = colors[combobox.current()]
  canvas.config(bg=color)

# виджет со списком
var = StringVar()
combobox = ttk.Combobox(window, values=colors, width=10, textvariable=var)
combobox['values'] = colors
combobox['state'] = 'readonly'
combobox.pack(padx=5, pady=5)


combobox.bind('<<ComboboxSelected>>', change_color)


canvas = tkinter.Canvas(window, width=200, height=150)
canvas.pack()

# кнопка для очистки combobox
button = Button(window, text='очистить', command=clear_combobox)
button.pack()


window.mainloop()