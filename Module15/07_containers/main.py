n = int(input('Кол-во контейнеров: '))
list_container = []

while len(list_container) < n:
    num = int(input('Введите вес контейнера: '))
    if num < 200:
        list_container.append(num)
    else:
        print('Вес слишком огромный, его принять мы не можем, положите другой контейнер')

for i in range(0, len(list_container), 1):
    for j in range(i, len(list_container), 1):
        if list_container[i] < list_container[j]:
            temp = list_container[i]
            list_container[i] = list_container[j]
            list_container[j] = temp

num = int(input('Введите вес нового контейнера: '))
new_list = []
count = 0

for i in range(0, len(list_container), 1):
    if list_container[i] >= num:
        new_list.append(list_container[i])
    else:
        new_list.append(num)
        num = 0
        count = i+1

if count == 0:
    new_list.append(num)
    count = n+1

print('Номер, куда встанет новый контейнер', count)

# зачёт! 🚀
