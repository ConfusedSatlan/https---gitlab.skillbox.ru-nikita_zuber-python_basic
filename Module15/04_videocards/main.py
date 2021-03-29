video_list = [3070, 2060, 3090, 3070, 3090]
max_m = 0

print('Кол-во видеокарт: 5')
for i in range(0, 5, 1):
    print(i+1, 'Видеокарта:', video_list[i])

max_m = video_list[0]
for i in range(1, 5, 1):
    if video_list[i-1] < video_list[i]:
        max_m = video_list[i]

new_list = []
for i in range(0, 5, 1):
    if video_list[i] != max_m:
        new_list.append(video_list[i])

print('\nСтарый список видеокарт:', video_list)
print('Новый список видеокарт:', new_list)
