file = open("data/beatles.txt", "r", encoding="utf8")
for line in file:
    for caracter in line:
        print(repr(caracter), end=" ")
    print()
file.close()