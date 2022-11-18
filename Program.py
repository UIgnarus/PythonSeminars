string = [str(i) for i in input().split()]
turn_1 = [3, 4]
turn_2 = [1, 2]
result = 0

for i in range(len(string)):
    if string[i] == "+":
        turn_2.append(("+", i))
    elif string[i] == "-":
        turn_2.append(("-", i))
    elif string[i] == "*":
        turn_1.append(("*", i))
    elif string[i] == "/":
        turn_1.append(("/", i))

for i in turn_1:
    if i[0] == "*":
        result = int(string[i[1]-1]) * int(string[i[1]+1])

    elif i[0] == "/":
        result = int(string[i[1]-1]) / int(string[i[1]+1])



for i in turn_2:
    if i[0] == "+":
        result = int(string[i[1]-1]) + int(string[i[1]+1])

    elif i[0] == "-":
        result = int(string[i[1]-1]) - int(string[i[1]+1])



print(result)


    