file = "text.txt"

with open(file, 'r') as f:
    text = f.read()

text = text.split()
for i in range(len(text)):
    if "абв" in text[i]:
        if not text[i].isidentifier():
            text[i] = text[i][-1]
        else: 
            text[i] = ''
text = " ".join(text)
with open(file, "w") as f:
    f.write(text)
