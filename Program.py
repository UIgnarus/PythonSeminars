"""
Задача 2
Найти максимум из 7 чисел
"""

list = []

list1 = [int(i) for i in input().split(' ')]
#list2 = list(map(int, input().split())) #Выходит ошибка
#names = input().split(',')

def max_in_list(_list):
    max = _list[0]
    for i in _list:
        if i > max:
            max = i
    print(max)

max_in_list(list1)
