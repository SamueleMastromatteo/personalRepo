def leggi_mappa(nome_file):
    mappa = []
    with open(nome_file, "r", encoding="utf-8") as f:
        righe = f.readlines()
        for riga in righe:
            valori = []
            for valore in riga.rstrip("\n"):

                if valore == "_":
                    valori.append(0)
                elif valore.isnumeric():
                    valori.append(int(valore))
                else:
                    exit("c'è un errore nel formato del file")

            mappa.append(valori)

    return mappa

def calcola_ombelico(mappa):

    somma_righe = [sum(mappa[r]) for r in range(len(mappa))]
    somma_colonne = []

    for c in range(len(mappa[0])):
        somma_colonna = 0
        for r in range(len(mappa)):
            somma_colonna += mappa[r][c]
        somma_colonne.append(somma_colonna)

    pos_max_riga = somma_righe.index(max(somma_righe))
    pos_max_colonna = somma_colonne.index(max(somma_colonne))

    return pos_max_riga, pos_max_colonna
        
def sposta_tempesta(mappa):
    mappa_nuova = []
    for riga in mappa:
        copia_riga = list(riga)
        pos = len(copia_riga)-1
        while pos > 0 and copia_riga[pos] == 0:
            pos -= 1
        if copia_riga[pos] != 0:
            copia_riga[pos] -= 1
        riga_nuova = [0] + copia_riga[:-1]
        mappa_nuova.append(riga_nuova)

    return mappa_nuova

def stampa_tempesta(mappa):
    for riga in mappa:
        copia_riga = list(riga)
        riga_stampa = [str(n) if n!=0 else "_" for n in copia_riga]
        print("".join(riga_stampa))
    print("\n")


def tempesta_esaurita(mappa):
    for riga in mappa:
        for valore in riga:
            if valore != 0:
                return False
    else:
        return True

def main():
    mappa = leggi_mappa("mappa.txt")

    pos_max_riga, pos_max_colonna = calcola_ombelico(mappa)

    print(f"\nOmbelico: riga {pos_max_riga}, colonna {pos_max_colonna}, intensità {mappa[pos_max_riga][pos_max_colonna]}\n")

    esaurita = False

    while not esaurita:
       stampa_tempesta(mappa)
       nuova = sposta_tempesta(mappa)
       esaurita = tempesta_esaurita(nuova)
       mappa = nuova

main()