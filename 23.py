# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элементас предыдущим номером)

import random
list = []
count = 0
for i in range(10):
    list.append(random.randrange(-10, 20))
print("Массив:", list)
for i in range(9):
    if list[i] < list[i+1]:
        count += 1
print("Чисел больше предыдущего элемента:", count)
