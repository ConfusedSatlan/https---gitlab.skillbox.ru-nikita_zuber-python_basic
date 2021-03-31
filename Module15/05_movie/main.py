films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
new_film_list = []
text = input('Введите название фильма: ')
flag = False

while text != 'end':
    for i in range(0, len(films), 1):  # TODO этот интервал (range) нужно записать короче (три аргумета здесь не нужны)
        if films[i] == text and text not in new_film_list:
            new_film_list.append(films[i])
            flag = True  # TODO если пользователь ввёл дубликат - сообщение должно быть не 'Ошибка! Такого фильма нету!'
    
    if flag is not True:
        print('Ошибка! Такого фильма нету!')

    flag = False
    text = input('\nВведите название фильма: ')

print('\nВаш список любымих фильмов: ', end='')
for i in range(0, len(new_film_list), 1):
    print(new_film_list[i], end=', ')


