# 2020-06-01
# Посчитать количество вхождений каждого символа в файле
file = open("text.txt", "r")

symbols = {}

while True:
    char = file.read(1)
    if not char:
        break
    if char not in symbols:
        symbols[char] = 0
    symbols[char] += 1

for x in symbols:
    print("[", x, "]", ord(x), ": ", symbols[x])
