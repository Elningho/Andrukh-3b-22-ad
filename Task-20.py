from random import randint

my_list = []

for i in range(10):
    my_list.append(randint(1, 100))
max_number = max(my_list)
min_number = min(my_list)

print(my_list)
print(f'Максимальное число: {max_number}, Минимальное число: {min_number}')