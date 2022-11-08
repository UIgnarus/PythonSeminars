"""
Задача №1
Принимает два числа и проверяет 
является ли число квадратом другого
"""

x = int(input("x = "))
y = int(input("y = "))

if (x**2 == y) or (y**2 == x):
    print(True)
else:
    print(False)
