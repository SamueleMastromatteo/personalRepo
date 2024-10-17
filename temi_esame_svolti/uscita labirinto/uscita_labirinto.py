import random


def leggi_labirinto(nome_file):
    labirinto = []

    with open(nome_file, "r", encoding="utf-8") as f:

        pos_partenza = tuple([int(i) for i in (f.readline().rstrip("\n").split(","))])
        pos_arrivo = tuple([int(i) for i in (f.readline().rstrip("\n").split(","))])

        righe = f.readlines()

        for riga in righe:
            valori = []
            for valore in riga.rstrip("\n"):
                valori.append(valore)

            labirinto.append(valori)

    return pos_partenza, pos_arrivo, labirinto


def cerca_movimenti(pos, mappa):

    r, c = pos

    movimenti_possibili = []

    # controllo sotto
    if mappa[r + 1][c] == " ":
        movimenti_possibili.append((r+1, c))

    # controllo sopra
    if mappa[r - 1][c] == " ":
        movimenti_possibili.append((r-1, c))

    # controllo sinistra
    if mappa[r][c - 1] == " ":
        movimenti_possibili.append((r, c-1))

    # controllo destra
    if mappa[r][c + 1] == " ":
        movimenti_possibili.append((r, c + 1))
    
    return movimenti_possibili


def main():
    
    posizione, fine, labirinto = leggi_labirinto("labirinto.txt")
    elenco_movimenti = []
    
    print(f"\nposizione iniziale: {posizione}\n")

    while posizione != fine:

        movimenti_possibili = cerca_movimenti(posizione, labirinto)

        if len(movimenti_possibili) > 0:
             # movimento possibile, ne scelgo uno a caso
             labirinto[posizione[0]][posizione[1]] = "V"
             posizione = random.choice(movimenti_possibili)
             elenco_movimenti.append(posizione)

        else:
            # movimenti non possibili, torno indietro e ripeto
            labirinto[posizione[0]][posizione[1]] = "V"
            posizione = elenco_movimenti[-1]
            elenco_movimenti.pop(-1)
    
    for i, movimento in enumerate(elenco_movimenti):
        print(f"movimento {i+1}: {movimento}")


main()