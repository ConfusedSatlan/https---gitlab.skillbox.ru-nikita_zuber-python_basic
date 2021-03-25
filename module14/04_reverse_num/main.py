def res(n):
    n_count = 0
    n_new = ''
    n_main = ''

    while True:
        if n % 10 != 0:
            n_count += 1
            n *= 10
        else:
            n /=10
            n_count -= 1
            break

    while n_count > 0: 
        n_new = n_new + str(int(n%10))
        n //= 10
        n_count -= 1

    while True:
        if n // 10 != 0:
            n_main = n_main + str(int(n%10))
            n //= 10
        else:
            n_main = n_main + str(int(n%10))
            break
    
    summ = n_main + '.' + n_new
    return float(summ)
      
n_one = float(input('Введите первое число: '))
n_two = float(input('Введите второе число: '))

print('Первое число наоборот:', res(n_one))
print('\nВторое число наоборот:', res(n_two))
print('\nСумма:', (res(n_one)+res(n_two)))