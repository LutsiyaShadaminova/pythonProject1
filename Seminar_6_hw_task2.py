# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

list1 = [random.randint(1, 100) for _ in range(int(input('Введите размер массива: ')))]
print(list1)
maxx = int(input('Введите максимальное число диапазона: '))
minn = int(input('Введите минимальное число диапазона: '))

def check(list1, maxx, minn):
    array = []
    for i in range(len(list1)):
        if maxx >= list1[i] >= minn:
            array.append(i)
    print(array)

check(list1, maxx, minn)
