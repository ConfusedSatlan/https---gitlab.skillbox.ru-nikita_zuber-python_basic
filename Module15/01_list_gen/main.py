num = int(input('Введите число для генерации списка: '))
count = 0
number = 1
new_list = []

while count < num:
    new_list.append(number)
    number += 2
    count += 1

print(new_list)
