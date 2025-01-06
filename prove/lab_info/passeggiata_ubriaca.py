# Una persona ubriaca si trova in una griglia di strade. A ciascun incrocio, sceglie a caso una delle quattro direzioni, cammina 
# fino all’incrocio successivo, e ripete la stessa scelta casuale. 
# Scrivere un programma che rappresenti le posizioni sulla griglia di strade come coppie di interi (x, y). 
# Implementare la camminata della persona ubriaca considerando 100 incroci e (0, 0) come posizione di partenza.

import random

x = 0
y = 0



for i in range(100):
    rand = random.randint(1, 4)
    if rand == 1:
        x += 1
    elif rand == 2:
        x -= 1
    elif rand == 3:
        y += 1
    else:
        y -= 1
    print(f"{x}, {y}")
    
print(f"posizione finale: {x}, {y}")