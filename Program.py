
str1 = input("str1 = ")
str2 = input("str2 = ")


start = 0
end = len(str1)
count = 0
while str1.find(str2,start, end) != -1:
    start = str1.find(str2, start, end) + len(str2)
    count += 1
print(count)

