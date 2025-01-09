# Una matrice n × n contenente i numeri interi 1,  2,  3, … , n^2 è un “quadrato magico” se la somma 
# dei suoi elementi in ciascuna riga, in ciascuna colonna e nelle due diagonali ha lo stesso valore. 
# Ad esempio, questo è un quadrato magico di dimensione 4:
# __________________
# | 16  3   2   13 |
# | 5   10  11  8  |
# | 9   6   7   12 |
# | 4   15  14  1  |
# ------------------
# Scrivere un programma che acquisisca in ingresso 16 valori, li disponga in una tabella 4 × 4 in ordine,
# una riga alla volta dall’alto in basso, e in ciascuna riga da sinistra a destra, e verifichi se, dopo
# averli disposti, questi formano un quadrato magico. Verificare due proprietà:
# I. Nei dati acquisiti sono presenti tutti e solamente i numeri 1, 2, ..., 16.
# II. Quando i numeri vengono disposti nella tabella, le somme delle righe, delle colonne e delle
# diagonali sono tutte uguali l’una all’altra.

import sys

matrice = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
]

matrice_set = []

# controllo che ci siano tutti i numeri da 1 a 16
for r in range(4):
    for c in range(4):
        matrice_set.append(matrice[r][c])
        matrice_set.sort()
if matrice_set[0] != 1 or matrice_set[15] != 16:
    sys.exit("i valori devono essere tra 1 e 16")

somma = 0
somma_prec = 0
for r in range(4):
    for c in range(4):
        somma += matrice[r][c]
        
        #esegue quando è arrivato all'ultimo valore della riga
        if c==3:
            #controllo se le somme delle righe sono uguali
            if (somma_prec > 0 and somma_prec == somma) or somma_prec == 0:
                somma_prec = somma
                print(somma)
                somma = 0
            else:                    
                sys.exit("le somme non coincidono")

                
for r in range(4):
    for c in range(1):
        somma += matrice[r][c]
        #controllo se le somme delle righe sono uguali
        if somma_prec == somma:
            somma_prec = somma
            print(somma)
            somma = 0
        else:
            sys.exit("le somme non coincidono")
        
        
                
              
              
#somma = matrice[0][0] + matrice[0][1] + matrice[0][2] + matrice[0][3]

#print(somma)