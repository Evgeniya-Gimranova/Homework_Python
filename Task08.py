# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите значение N '))
sum = 0
for i in range(1, n+1):
    sum+=(1+1/i)**i

print(f"Сумма последовательности равна {round(sum, 2)}")



#n = int(input('Введите число: ')) 



# def sequence(n):

#     return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
# print(sequence(n))
# print('Сумма последовательности =', round(sum(sequence(n))))
