"""
Задача 3
Принимает число N и выводит числа от -N до N

"""

n = int(input("N = "))
for i in range(-n, n + 1):
    print(i, end = ' ')