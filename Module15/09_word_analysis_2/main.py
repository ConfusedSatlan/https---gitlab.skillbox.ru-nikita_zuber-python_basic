text = input('Введите слово: ')
new_list = list(text)
count = 0

for i in range(0, len(new_list), 1):
    if new_list[i] == new_list[len(new_list)-1-i]:
        count += 1

if count == len(new_list):
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
