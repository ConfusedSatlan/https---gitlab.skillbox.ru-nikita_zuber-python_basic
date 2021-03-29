films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
new_film_list = []
text = input('Введите название фильма: ')
flag = False

while text != 'end':
    for i in range(0, len(films), 1):
        if films[i] == text:
            new_film_list.append(films[i])
            flag = True

    if flag != True:
        print('Ошибка! Такого фильма нету!')

    flag = False
    text = input('\nВведите название фильма: ')

print('\nВаш список любымих фильмов: ', end='')
for i in range(0, len(new_film_list), 1):
    print(new_film_list[i], end=', ')
