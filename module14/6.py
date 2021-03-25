


print('Введите координаты монетки:\n')
x = float(input('X: '))
y = float(input('\nY: '))
r = float(input('\nВведите радиус: '))

if x < r and y < r:
    print('\nМонетка где-то рядом!')
else:
    print('\nМонетки здесь нет!')