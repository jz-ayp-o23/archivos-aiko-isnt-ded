file = open("data/beatles.txt", "r", encoding="utf8")
for line in file:
    print(line)
file.close()