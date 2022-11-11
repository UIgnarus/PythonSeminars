"""

ax**2+ bx +c =0

Корни: 

1) формула нахождения квадратных корней
2)с помощью библиотек

"""

def square_root(list):
    d = list[1]**2 - (4*list[0] * list[2])
    print(d)
    if d < 0:
        return None
    elif d == 0:
        return -(list[1]/(2*list[0]))
    if d > 0:
        x_1 = (-(list[1])+d**0.5)/(2*list[0])
        x_2 = (-(list[1])-d**0.5)/(2*list[0])
        return [x_1, x_2]


abc = [int(i) for i in input().split()]
print(square_root(abc))

    