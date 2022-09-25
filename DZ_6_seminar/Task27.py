# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите число N: '))
# factorial = 1
# for i in range(1, n+1):
#    factorial *= i
# print(factorial, end=' ')

from itertools import accumulate
import operator

N = int(input('Введите число: '))

def get_prods(N):
    return list(accumulate([x for x in range(1, N + 1)], operator.mul))

print(get_prods(N))