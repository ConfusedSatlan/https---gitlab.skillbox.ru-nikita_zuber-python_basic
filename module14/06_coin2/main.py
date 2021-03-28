import math

print('Введите координаты монетки:\n')
x = float(input('X: '))
y = float(input('\nY: '))
r = float(input('\nВведите радиус: '))

if (math.sqrt(x**2 + y**2)) <= r:
    print('\nМонетка где-то рядом!')
else:
    print('\nМонетки здесь нет!')
