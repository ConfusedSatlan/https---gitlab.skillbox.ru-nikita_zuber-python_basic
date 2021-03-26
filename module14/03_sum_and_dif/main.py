
def n_sum(n):
    n_new = 0
    while True:
        if n // 10 != 0:
            n_new = n_new +  (n % 10)
            n //= 10
        else:
            n_new += n % 10
            return n_new
            break  # TODO эта строка не нужна

def n_count(n):
    n_count = 0
    while True:
        if n // 10 != 0:
            n_count += 1
            n //= 10
        else:
            n_count += 1
            return n_count
            break  # TODO эта строка не нужна



n = int(input('Введите число: '))

a = n_sum(n)
b = n_count(n)


print('Сумма цифр:', a)
print('\nКол-во цифр в числе:', b)
print('\nРазность суммы и кол-ва цифр:', (a-b))

# TODO оформить код по правилам PEP8
