vowels = 0
consonants = 0
vowels_set = set('aeiou')
consonants_set = set('bcdfghjklmnpqrstvwxyz')

word = input('Введите любое слово на английском: ')
for i in range(len(word)):
    if word[i] in vowels_set:
            vowels += 1
    if word[i] in consonants_set:
            consonants += 1

print(f'В строке {vowels} гласных и {consonants} согласных')
