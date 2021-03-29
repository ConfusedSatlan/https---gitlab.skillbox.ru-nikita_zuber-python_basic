n = int(input('Введите размер списка: '))
list_container = []

while len(list_container) < n:
    num = int(input('Введите число: '))
    list_container.append(num)

print('\nИзначальный список: ', list_container)

for i in range(0, len(list_container), 1):
    for j in range(i, len(list_container), 1):
        if list_container[i] > list_container[j]:
            temp = list_container[i]
            list_container[i] = list_container[j]
            list_container[j] = temp

print('\nОтсортированный список: ', list_container)
