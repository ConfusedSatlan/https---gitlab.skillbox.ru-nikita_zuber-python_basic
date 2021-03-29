import random

n = int(input('Кол-во клеток: '))
new_list = []

for i in range(0, n, 1):
    new_list.append(random.randint(0, 10))

for i in range(0, n, 1):
    print('Эффективность', i+1, 'клетки:', new_list[i])

print('\nНеподходящие значения: ', end='')
for i in range(0, n, 1):
    if new_list[i] < i:
        print(new_list[i], end=' ')
