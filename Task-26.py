def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    print(f'Наименьший общий множитель введенных чисел равен: {m // (a + b)}')

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
lcm1 = lcm(number_1, number_2)