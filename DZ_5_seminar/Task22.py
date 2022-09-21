# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
from random import randint
import random

text = ['Ваш ход', 'Ваша очередь', 'Берите конфеты']

#def player_vs_player():
candies_total = 2021
max_take = 28
count = 0
player_1 = input('\nКак тебя зовут?: ')
player_2 = input('\nА твоего соперника?: ')

# print(f'\nНу чтож {player_1} и  {player_2} да начнется игра !\n')
# print('\nДля начала опеределим кто первый начнет игру.\n')

x = randint(1, 2)
if x == 1:
    first = player_1
    second = player_2
else:
    first = player_2
    second = player_1
print(f'Поздравляю {first} ты ходишь первым !')

while candies_total > 0:
    if count == 0:
        step = int(input(f'\n{random.choice(text)} {first} = '))
        if step > candies_total or step > max_take:
            step = int(input(
                f'\nНе жадничай можно взять только {max_take} конфет {first}, попробуй еще раз: '))
        candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону еще {candies_total}')
            count = 1
        else:
            print('Все кончились конфетки')

        if count == 1:
            step = int(input(f'\n{random.choice(text)}, {second} '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nНе жадничай можно взять только {max_take} конфет {second}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nна кону еще {candies_total}')
            count = 0
        else:
            print('Баста, карапузик, кончились конфетки')

    if count == 1:
        print(f'{second} ПОБЕДИЛ')
    if count == 0:
        print(f'{first} ПОБЕДИЛ')


#player_vs_player()
