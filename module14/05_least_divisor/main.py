def dev(n):
    for i in range(2, n+1, 1):
        if n % i == 0:
            return i

n = int(input('Введите число: '))

print('Наименьший делитель, отличный от единицы:', dev(n))

# TODO оформить код по правилам PEP8
