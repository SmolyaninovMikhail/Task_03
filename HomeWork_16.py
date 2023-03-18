# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random
n = int(input('Кол-во элементов массива: '))
list_a = []
for _ in range(n):
    a = random.randint(1, 10)
    list_a.append(a)
print(list_a)
A_num = list(map(int, list_a))
X = int(input('Введите число X, которое необходимо найти в массиве: '))
count = 0
for i in range(n):
    if A_num[i] == X:
        count += 1
print('Число X встречается: ->', count)