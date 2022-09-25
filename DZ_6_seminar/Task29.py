# # Задайте список из нескольких чисел.
# #  Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# # Пример:

# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [2, 3, 5, 9, 3]
# print (list)
# def sum_Odd_Index(list):
#     sum = 0
#     for i in range(len(list)):
#         if i %2 == 1:
#             sum+=list[i]
#     print(f'Сумма равна {sum}')   
  
# sum_Odd_Index(list)

# #2
# st = [2, 3, 5, 9, 3]
# print(sum(list[1:5:2]))

from random import randint

def get_list(n, frst, last):
    return [randint(frst, last) for i in range(n)]

def sum_odd_position(mylist):
    return sum(mylist[1::2])

n = 10
frst = 1
last = 10

mylist = get_list(n, frst, last)
print(mylist)
print(sum_odd_position(mylist))

