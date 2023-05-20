def calculator(a, b, operation):
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if b != 0:
            result = a / b
        else:
            print('Ошибка: Нельзя делить на ноль')
            return
    print(result)

a = int(input('Введите первое число: '))
operation = input('Введите одну из операций(+ - * /): ')
b = int(input('Введите второе число: '))

calculator(a, b, operation)