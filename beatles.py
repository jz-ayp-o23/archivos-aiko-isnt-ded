with open("data/beatles.txt", "r", encoding="utf8") as file:
    for line in file:
        print(line.strip())