"""

ax**2+ bx +c =0

Корни: 

1) формула нахождения квадратных корней
2)с помощью библиотек

"""

def square_root(list):
    a,b,c = list[0], list[1], list[2]
    d = b**2 - (4*a*c)
    print(d)
    if d < 0:
        return None
    elif d == 0:
        return -(b/(2*a))
    if d > 0:
        x_1 = (-(b)+d**0.5)/(2*a)
        x_2 = (-(b)-d**0.5)/(2*a)
        return [x_1, x_2]

abc = [int(i) for i in input().split()]
print(square_root(abc))

    