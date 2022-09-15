# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

list = [randint(1,10) for i in range (1,16)]
print(list)

def get_unical_elements(list):
    return [i for i in set(list)]
new_list= get_unical_elements(list)
print(new_list)
