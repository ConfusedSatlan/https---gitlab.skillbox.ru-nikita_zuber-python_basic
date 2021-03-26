def func(year_one, year_two):
    n = 0
    n_new = 0
    n_count = 0
    n_max = 0
    # TODO некоторые из переменных выше не нужны

    for i in range(year_one, year_two+1, 1):
        n = i
        while True:
            n_max = n % 10
            n //= 10

            n_new = i
            for j in range(0, 4, 1):
                if n_max == n_new % 10:
                    n_count += 1
                n_new //= 10
            
            if n_count == 3:
                print(i, '\n')
                break

            n_count = 0

            if int(n) == 0:
                break
            
year_one = int(input('Введите первый год: '))
year_two = int(input('Введите второй год: '))

func(year_one, year_two)

# TODO оформить код по правилам PEP8
