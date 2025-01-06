# Leggere una sequenza di numeri interi conclusa da una riga vuota. Stampare la posizione dei massimi locali (numeri maggiori 
# sia del valore precedente che di quello successivo) se ce ne sono, altrimenti stampare il messaggio 'Non ci sono massimi 
# locali'. 
# Se sono presenti più coppie di massimi locali, individuare i due massimi locali più vicini fra loro e stampare la loro 
# posizione.

list = [1, 5, 3, 4, 2, 8, 8, 10, 4]
massimi = []

for i in range(len(list)-2):
    
    for num in range(3):
        if list[num-1] or list[num+1] is not None:
            list_3 = [list[num-1], list[num], list[num+1]]
            print(list_3)
    
#print(massimi)
    