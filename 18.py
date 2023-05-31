# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.

import random
temp = int(input(
    "Введите количество элементов в массиве: "))
mas = []
for i in range(temp):
    mas.append(random.randrange(1, 25))
print("Массив:", mas)
x = int(input("Введите число: "))
min = mas[0]
max = mas[0]
for i in range(temp):
    if mas[i] > max:
        max = mas[i]
    elif min > mas[i]:
        min = mas[i]
for i in range(temp):
    if min < mas[i] <= x:
        min = mas[i]
    elif max > mas[i] >= x:
        max = mas[i]
if max - x > x - min:
    print("Ближайшее число:", min)
else:
    print("Ближайшее число:", max)
