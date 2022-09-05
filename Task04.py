#Напишите программу, которая принимает на вход координаты двух точек 
#и находит расстояние между ними в 2D пространстве.

#Пример:

#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21


from turtle import distance


print('Введите координаты точки А ')
x = float(input('x = ')) 
y = float(input('y = ')) 
print('Введите координаты точки B ')
x1 = float(input('x1 = ')) 
y1 = float(input('y1 = ')) 

distance = (((x1 - x) ** 2 + (y1 - y) ** 2)**0.5)
print(f'Расстояние между двумя точками на плоскости равно {round(distance, 2)}')