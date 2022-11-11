
def gsd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return (a+b)

def lcm(a, b):
    return int((a*b)/gsd(a,b))

n = [int(i) for i in input().split()]
print(lcm(n[0], n[1]))
