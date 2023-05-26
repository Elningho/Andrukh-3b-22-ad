def reverse(string):
    if len(string) == 0:
        return string
    else:
        return string[::-1]

string_input = str(input('Введите строку: '))
print(reverse(string_input))