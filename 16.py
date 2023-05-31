# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве

import random
temp = int(input("Введите количество элементов в массиве: "))
mas = []
for i in range(temp):
    mas.append(random.randrange( 1, 30))
print("Массив:", mas)
x = int(input("Введите число: "))
count = 0
for i in range(temp):
    if mas[i] == x:
        count += 1
if 1 < count < 5:
    print("Число {} встречается {} раза".format(x, count))
else:
    print("Число {} встречается {} раз".format(x, count))