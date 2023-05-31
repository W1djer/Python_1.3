# Напишите программу для печати всех уникальных значений в словаре.
list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII":"S007"}]
empty = []
for i in list:
    temp = i
    for j in temp:
        empty.append(temp[j])
clear = set(empty)
print(clear)