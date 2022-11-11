def find_min_and_max(list):
    mini = list[0]
    maxi = list[0]
    for i in range(1,len(list)):
        if list[i] > maxi:
            maxi = list[i]
        if list[i] < mini:
            mini = list[i]
    return([mini,maxi])
list = [int(i) for i in input().split()]
values = find_min_and_max(list)
print(f"min = {values[0]}, max = {values[1]}")