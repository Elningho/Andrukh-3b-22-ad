number = int(input('Введите число: '))

if number > 1:
    for i in range(2, int(number/2)+1):
        if (number % i) == 0:
            print(number, "- не является простым")
            break
    else:
        print(number, "- простое число")
else:
    print(number, "- не является простым")