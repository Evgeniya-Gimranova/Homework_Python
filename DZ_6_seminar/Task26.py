# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# # Пример:

# # - 6782 -> 23
# # - 0,56 -> 11

# num = input('Введите число с плавающей точкой ')
# sum = 0
# for i in num:
#      if i != '.':
#          sum += int(i)
# print(sum)

from random import uniform

n = round(uniform(1, 100), 3)

def sum_digit(n):
    return sum(map(int, list(str(n).replace('.',''))))

print(n)
print(sum_digit(n))