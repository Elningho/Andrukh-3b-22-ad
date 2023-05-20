from random import randint

my_list = []

for i in range(10):
    my_list.append(randint(1, 10))
my_list_sum = sum(my_list)

print(my_list)
print(my_list_sum)