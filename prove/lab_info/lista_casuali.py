# Scrivere un programma che inizializzi una lista con 10 numeri interi casuali tra 1 e 100 e poi visualizzi, su quattro righe 
# successive:
# I. Tutti gli elementi di indice pari;
# II. Tutti gli elementi di valore pari;
# III. Tutti gli elementi in ordine inverso;
# IV. Il primo e l’ultimo elemento.

import random
num = []
indice_pari = []
pari = []
for i in range(10):
    rand = random.randint(1,100)
    num.append(rand)
    
    if i%2 ==0:
        indice_pari.append(rand)
    if rand %2 ==0:
        pari.append(rand)
    

print(indice_pari)
print(pari)
num.reverse()
print(num)
print(num[-1], num[0])