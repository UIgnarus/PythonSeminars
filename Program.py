colors = ["red", "green", "blue"]
data = open("file.txt", "a") # a - дописать, r - считать, w - переписать
data.writelines(colors)
data.close()

with open("file.txt", "w") as data:
    data.write("line 1\n")
    data.write("line 2\n") #автоматически закрывается


path = "file.txt"
data = open(path, "r")
for line in data:
    print(line)
data.close()

exit()