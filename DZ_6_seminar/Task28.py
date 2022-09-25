# # Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input('Введите значение N '))
# sum = 0
# for i in range(1, n+1):
#     sum+=(1+1/i)**i

# print(f"Сумма последовательности равна {round(sum, 2)}")

# # 2
# n = int(input("Введите число : "))
# sum = 0
# for i in range (1, n + 1):
#     a = (1 + 1 / i)**i
#     sum += a
#     print(a, end=" ")
# print(f"Сумма равна: {sum}")

from msilib import sequence

n = int(input('Введите число: ')) 

def get_squerence(n):
    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

nums = get_squerence(n)
print(nums)
print(round(sum(nums), 5))