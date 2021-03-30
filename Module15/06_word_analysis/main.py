text = input('Введите слово: ')
text_check = list(text)
text_count = 0
count = 0

for i in text:
    for j in range(0, len(text), 1):
        if i == text_check[j]:
            count += 1
    if count == 1:
        text_count += 1

    count = 0

print('Кол-во уникальных букв:', text_count)

# зачёт! 🚀
