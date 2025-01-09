# Leggere un file “estremi.dat” contenente coppie di numeri
# interi (x, y), una coppia per riga e separate da uno spazio, e creare
# un secondo file “differenze.dat” che contenga il valore delle
# differenze x-y, uno per riga.

differenze = []
with open("estremi.dat", "r", encoding="utf-8") as f:
    for riga in f:
        numero = riga.split()
        sottrazione = int(numero[0]) - int(numero[1])
        differenze.append(sottrazione)
    print(differenze)
        
with open("differenze.dat", "w", encoding="utf-8") as f:
    for riga in differenze:
        f.write(f"{riga}\n")
