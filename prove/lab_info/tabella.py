# Scrivere le istruzioni Python per eseguire le seguenti operazioni con una tabella di r righe e c colonne (dimensioni inserite da tastiera):
# I. inizializzare la tabella con valori pari a zero (0);
# II. riempire le caselle alternando 0 e 1 in uno schema a scacchiera;
# III. riempire di 0 solo le caselle della riga superiore e di quella inferiore, lasciando invariato il resto della tabella;
# IV. riempire con 1 solo le caselle della colonna di destra e di sinistra, lasciando invariato il resto della tabella;
# V. calcolare e stampare la somma di tutti gli elementi.

tab = []

righe = int(input("numero righe: "))
colonne = int(input("numero colonne: "))

def inizializzazione():
    for r in range(righe):
        riga = []
        for c in range(colonne):
            riga.append(0)
        tab.append(riga)
        
    print("inizializzazione: \n", tab)
        
def scacchiera():
    for r in range(righe):
        riga = []
        for c in range(colonne):
            if r%2 == 0:
                if c%2 == 0:
                    tab[r][c] = 0
                else:
                    tab[r][c] = 1
            else:
                if c%2 == 0:
                    tab[r][c] = 1
                else:
                    tab[r][c] = 0
    print("scacchiera: \n", tab)
        
def sup_inf():
    for c in range(colonne):
        tab[0][c] = 0
        tab[righe-1][c] = 0
    print("sup_inf: \n",tab)
    
def dx_sx():
    for r in range(righe):
        tab[r][0] = 1
        tab[r][colonne-1] = 1
    print("dx_sx: \n", tab)
    
def somma():
    somma = 0
    for r in range(righe):
        for c in range(colonne):
            somma += tab[r][c]
    print("somma: ",somma)
        
                    
inizializzazione()
scacchiera()
sup_inf()
dx_sx()
somma()