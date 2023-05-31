# Напишите программу, которая вычисляет стоимость введенного пользователем слова.

list1 = [{'A': 1}, {'E':1}, {'I':1}, {'O':1}, {'U':1}, {'L':1}, {'N':1}, {'S':1}, {'T':1}, {'R':1}]
list2 = [{'D':2}, {'G':2}]
list3 = [{'B':3}, {'C':3}, {'M':3}, {'P':3}]
list4 = [{'F':4}, {'H':4}, {'V':4}, {'W':4}, {'Y':4}]
list5 = [{'K':5}]
list6 = [{'J':8}, {'X':8}]
list7 = [{'Q':10}, {'Z':10}]
list = (list1, list2, list3, list4, list5, list6, list7)
slovo = input("Enter a word: ").upper()
price = 0
for i in slovo:
    for j in list:
        for k in j:
            temp = k
            for c in temp:
                if i == c:
                    price += temp[c]
print("Стоимость:", price)
