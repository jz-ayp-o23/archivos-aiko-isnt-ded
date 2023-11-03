import os.path

file = "data/beatles.txt"
if os.path.isfile(file):
    print(f"El archivo '{file}' existe.")
else:
    print(f"El archivo '{file}' no existe.")