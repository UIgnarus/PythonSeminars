# import name as c

# c.funcs(x,y)


def cont(*parms):
    res: str = ""
    return (parms)


print(cont("1", "2"))


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)

