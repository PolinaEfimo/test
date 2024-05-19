import tkinter as tk
import random

''' Функция для определения победителя в игре'''
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Ничья"
    elif (player_choice == "камень" and computer_choice == "ножницы" or
         player_choice == "ножницы" and computer_choice == "бумага" or
         player_choice == "бумага" and computer_choice == "камень"):
        return "Победа"
    else:
        return "Проигрыш"

'''Функция для обновления счетчиков'''
def update_counters(result):
    if result == "Ничья":
        ties_counter.set(ties_counter.get() + 1)
    elif result == "Победа":
        player_wins_counter.set(player_wins_counter.get() + 1)
    else:
        player_losses_counter.set(player_losses_counter.get() + 1)

'''Функция для обработки выбора игрока'''
def player_choice_handler(choice):
    computer_choices = ["камень", "ножницы", "бумага"]
    computer_choice = random.choice(computer_choices)
    result = determine_winner(choice, computer_choice)
    update_counters(result)
    result_label.config(text=f"Игрок выбрал: {choice}\nКомпьютер выбрал: {computer_choice}\nРезультат: {result}")

''' Создание графического интерфейса'''
root = tk.Tk()
root.title("Камень, ножницы, бумага")
root.geometry('350x350')
root.resizable(False, False)

'''Счетчики'''
ties_counter = tk.IntVar()
player_wins_counter = tk.IntVar()
player_losses_counter = tk.IntVar()

'''Интерфейс'''


result_label = tk.Label(root, text="Начало игры")
result_label.place(x=150, y=20)


'''кнопки'''
choices = ['камень', "ножницы", "бумага"]
buttons = []
for i, choice in enumerate(choices):
    button = tk.Button(root, text=choice, width=10, background='sky blue', command=lambda c=choice: player_choice_handler(c))
    button.place(x=50 + i*100, y=250)
    buttons.append(button)
'''Счетчики'''
tk.Label(root, text="Счет: ", font=("Times new Roman", 16), fg='brown').place(x=5, y=80)
tk.Label(root, text="Ничьи: ", font=('Times new Roman', 10, 'bold'), fg='grey').place(x=5, y=110)
tk.Label(root, textvariable=ties_counter).place(x=80, y=110)
tk.Label(root, text="Победы:", font=('Times new Roman', 10, 'bold'), fg='green').place(x=5, y=130)
tk.Label(root, textvariable=player_wins_counter).place(x=80, y=130)
tk.Label(root, text="Проигрыши:", font=('Times new Roman', 10, 'bold'), fg='red').place(x=5, y=150)
tk.Label(root, textvariable=player_losses_counter).place(x=80, y=150)

root.mainloop()
