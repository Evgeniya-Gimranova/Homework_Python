# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input("Введите число N: "))
list= [i for i in range(-n, n+1)]

print(list)
prod=1
with open('file.txt') as file:
    for pos in file:
        if int(pos)<len(list):
            prod*= list[int(pos)]
        else: prod*=1
print(prod)