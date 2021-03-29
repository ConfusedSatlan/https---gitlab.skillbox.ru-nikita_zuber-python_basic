n = int(input('Введите размер списка: '))

new_list = []

for _ in range(0, n, 1):
    num = int(input('Введите число: '))
    new_list.append(num)

k = int(input('\nСдвиг: '))
main_list = []

for i in range(k-1, -1, -1):
    main_list.append(new_list[n-1-i])

for i in range(0, n-k, 1):
    main_list.append(new_list[i])

print('Изначальный список:', new_list)
print('Сдвинутый список', main_list)
