def crea_griglia(r=6, c=7):
    griglia = []
    for n in range(r):
        colonne = ["-" for n in range(c)]
        griglia.append(colonne)
    
    return griglia


def leggi_mosse(nome_file):
    mosse = []

    try:
        with open(nome_file, "r", encoding="utf-8") as f:
            for riga in f:
                campi = riga.rstrip("\n").split()
                mossa = "O" if campi[0] == "G1" else "X"
                mosse.append((mossa, int(campi[1])))

    except OSError:
        exit(f"Il file {nome_file} non esiste")
    
    return mosse


def gioca_turno(mossa, griglia):

    simbolo, colonna = mossa
    
    for riga in range(len(griglia)-1,-1, -1): # guardo le righe partendo dal basso e prendo la prima cordinata di griglia[riga][colonna] == "-"

        if griglia[riga][colonna] == "-":
            griglia[riga][colonna] = simbolo

            return riga, colonna, simbolo # la funzione modifica la griglia anche senza return, uso il return per ottenere pos e simbolo dell'ultimo turno


def determina_esito(pedina, griglia):
    
    r, c, simbolo = pedina

    # controllo spazio in basso
    if r + 3 < len(griglia):
        # controllo pedine in basso
        if griglia[r+1][c] == simbolo and griglia[r+2][c] == simbolo and griglia[r+3][c] == simbolo:
            return True
    
    # controllo spazio destra
    if c + 3 < len(griglia[r]):
        # controllo pedine destra
        if griglia[r][c+1] == simbolo and griglia[r][c+2] == simbolo and griglia[r][c+3] == simbolo:
            return True
    
    # controllo spazio sinistra
    if c - 3 >= 0:
        # controllo pedine sinistra
        if griglia[r][c-1] == simbolo and griglia[r][c-2] == simbolo and griglia[r][c-3] == simbolo:
            return True
        
    # controllo spazio diagonale basso-destra
    if r + 3 < len(griglia) and c + 3 < len(griglia[r]):
        # controllo pedine diagonale basso-destra
        if griglia[r+1][c+1] == simbolo and griglia[r+2][c+2] == simbolo and griglia[r+3][c+3] == simbolo:
            return True

    # controllo spazio diagonale basso-sinistra
    if r + 3 < len(griglia) and c - 3 < len(griglia[r]):
        # controllo pedine diagonale basso_sinistra
        if griglia[r+1][c-1] == simbolo and griglia[r+2][c-2] == simbolo and griglia[r+3][c-3] == simbolo:
            return True
    
    else: # non ha vinto

        return False
     

def main():

    vinto = False

    griglia = crea_griglia()
    
    print("\nGriglia vuota\n")
    [print(''.join(riga)) for riga in griglia] # griglia vuota

    mosse = leggi_mosse("mosse.txt")

    n_mossa = 0

    while n_mossa < len(mosse) and not vinto:

        mossa = mosse[n_mossa]

        n_mossa += 1

        if mossa[0] == "O":

            print("\nGioca il giocatore G1\n")

            pedina = gioca_turno(mossa, griglia)
            vinto = determina_esito(pedina, griglia)

            if vinto:
                vincitore = ("G1", n_mossa)


        else:

            print("\nGioca il giocatore G2\n")

            pedina = gioca_turno(mossa, griglia)
            vinto = determina_esito(pedina, griglia)

            if vinto:
                vincitore = ("G2", n_mossa)


        [print(''.join(riga)) for riga in griglia] # stampa griglia nuova


    if not vinto:
        print("\nLa partita è sospesa a causa dell'esaurimento delle mosse\n")

    else:
        print(f"\nHa vinto {vincitore[0]} in {vincitore[1]} mosse\n")


main()
