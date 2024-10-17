import os

#with open("prova_txt.txt", "r") as prova:
#    for index, riga in enumerate(prova, start=1):
#        print(f"{index}: {riga.strip()}")


file_path = "animals_sorted.txt"
if os.path.exists(file_path):  # Verifica se il file esiste
    os.remove(file_path)
with open("animals.txt", "r") as animals:
    open(file_path, "x")
    sorted_animals = sorted(animals)
    for riga in sorted_animals:
        open(file_path, "a").write(riga)
