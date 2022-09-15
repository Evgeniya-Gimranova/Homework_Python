#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите натуральное число n:\n'))

def get_prime_factors(n):
    factors = list()
    divisor = 2
    while (divisor<= n):
        if (n % divisor == 0):
            factors.append(divisor)
            n=n/divisor
        else:
            divisor+=1
    return factors

prime_factors = get_prime_factors(n)
print(f'Список простых множителей числа {n} - {prime_factors}')


