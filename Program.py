colors = ["red", "green", "blue"]
data = open("file.txt", "a") # a - дописать, r - считать, w - переписать
data.writelines(colors)
data.close()