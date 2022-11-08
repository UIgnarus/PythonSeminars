
str1 = input("str1 = ")
str2 = input("str2 = ")

def count_in_str(_str1, _str2):
    count = 0
    for i in _str1:
        if i == _str2:
            count+=1
    return count

print(count_in_str(str1, str2))

