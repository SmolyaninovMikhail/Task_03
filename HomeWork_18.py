# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
n = int(input('Кол-во элементов массива: '))
list_a = []
for _ in range(n):
    a = random.randint(1, 10)
    list_a.append(a)
print(list_a)
A_num = list(map(int, list_a))
X = int(input('Введите число X: '))
min = abs(X - A_num[0])
index = 0
for i in range(1, n):
    count = abs(X - A_num[i])
    if count < min:
        min = count
        index = i
print('Самый близкий по величине элемент к заданному числу X: -> ', A_num[index])